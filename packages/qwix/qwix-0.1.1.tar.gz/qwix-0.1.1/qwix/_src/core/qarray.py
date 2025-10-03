# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Quantized Array."""

import dataclasses
import functools
from typing import Callable, Collection, Mapping, Sequence, TypeAlias
import flax.struct
import jax
from jax import numpy as jnp
from qwix._src.core import numerics


# ---------------------------------------------
# QArray definition and common functions.
# ---------------------------------------------


@flax.struct.dataclass
class QArray:
  """A quantized array implementation with subchannel support.

  The following conditions hold:
    * qvalue.shape == original.shape
    * len(scale.shape) == len(original.shape)
    * len(scale.shape) == len(zero_point.shape)
    * To enable subchannel quantization, scale and zero_point can be
      "generic broadcasted" to original.shape, which means
        all(o % s == 0 for o, s in zip(original.shape, scale.shape))
    * original ≈ (qvalue - zero_point) * generic_broadcast(
        scale, original.shape)

  Attributes:
    qvalue: The quantized value.
    scale: The scale used to quantize the value.
    zero_point: The quantization value that represents the exact floating-point
      value 0, or None if in symmetric quantization.
    qtype: The logical type of the qvalue, which could be different from the
      dtype used for storage in qvalue. If None, the qvalue's dtype will be used
      as the logical type.
  """

  qvalue: jax.Array
  scale: jax.Array
  zero_point: jax.Array | None = None
  qtype: jax.typing.DTypeLike = flax.struct.field(
      pytree_node=False, default=None
  )

  # Array-like methods.
  shape = property(lambda self: self.qvalue.shape)
  ndim = property(lambda self: self.qvalue.ndim)
  T = property(lambda self: self.transpose())

  def reshape(self, *new_shape) -> 'QArray':
    return reshape(self, *new_shape)

  def transpose(self, *args) -> 'QArray':
    return jax.tree.map(lambda x: x.transpose(*args), self)

  def __getitem__(self, idx) -> 'QArray':
    return rewriting_take(self, idx)

  def __post_init__(self):
    if self.qtype is None:
      object.__setattr__(self, 'qtype', self.qvalue.dtype)

  def astype(self, dtype: jax.typing.DTypeLike) -> 'QArray':
    """Cast the dequant type to the given dtype."""
    return dataclasses.replace(self, scale=self.scale.astype(dtype))

  def swapaxes(self, axis1: int, axis2: int) -> 'QArray':
    return jax.tree.map(lambda x: x.swapaxes(axis1, axis2), self)


def reshape(array: QArray, *new_shape) -> QArray:
  """Reshapes the array, which is not always feasible."""
  if len(new_shape) == 1:
    try:
      new_shape = tuple(new_shape[0])
    except TypeError:
      pass

  prod = lambda s: functools.reduce(lambda x, y: x * y, s, 1)

  old_shape = array.shape
  if prod(old_shape) != prod(new_shape):
    raise ValueError(f'Cannot reshape {old_shape} into {new_shape}.')

  # Group the old shape and the new shape. e.g. for (2, 2, 6) -> (4, 1, 3, 2),
  # the groups are (2, 2) -> (4,) and (6,) -> (3, 2) with 1 ignored.
  groups = []
  last_group_old, last_group_new = [], []
  i, j = 0, 0
  while i < len(old_shape) or j < len(new_shape):
    # INVARIANT: if prod(last_group_old) == prod(last_group_new), they
    # must be both empty.
    if prod(last_group_old) < prod(last_group_new):
      last_group_old.append(old_shape[i])
      i += 1
    elif prod(last_group_old) > prod(last_group_new):
      last_group_new.append(new_shape[j])
      j += 1
    elif i < len(old_shape) and (
        j >= len(new_shape) or old_shape[i] <= new_shape[j]
    ):
      last_group_old.append(old_shape[i])
      i += 1
    elif j < len(new_shape):
      last_group_new.append(new_shape[j])
      j += 1
    if prod(last_group_old) == prod(last_group_new):
      groups.append((tuple(last_group_old), tuple(last_group_new)))
      last_group_old, last_group_new = [], []
  assert not last_group_old and not last_group_new

  def reshape_by_groups(x: jax.Array) -> jax.Array:
    i = 0
    target_shape = []
    for old, new in groups:
      actual_shape = x.shape[i : i + len(old)]
      actual_size = prod(actual_shape)
      if actual_shape == old:
        target_shape.extend(new)
      elif actual_size == 1:
        target_shape.extend(1 for _ in new)
      elif actual_size == actual_shape[0] and new[0] % actual_shape[0] == 0:
        # Channelwise-preserving reshape, e.g.
        #   qvalue: (2, 2, 6) -> (4, 3, 2)
        #   scale:  (2, 1, 3) -> (2, 3, 1)  OK
        #   scale:  (1, 2, 2) -> NOT OK
        target_shape.extend([actual_shape[0]] + [1] * (len(new) - 1))
      else:
        raise ValueError(
            f'Cannot reshape {old_shape} into {new_shape} for {x.shape}.'
        )
      i += len(old)
    return x.reshape(target_shape)

  return jax.tree.map(reshape_by_groups, array)


def rewriting_take(array: QArray, idx) -> QArray:
  """Returns array[*idx]."""
  try:
    idx = list(idx)
  except TypeError:
    idx = [idx]

  actual_len = sum(i is not None and i is not Ellipsis for i in idx)
  if Ellipsis in idx:
    assert idx.count(Ellipsis) == 1
    index = idx.index(Ellipsis)
    idx[index : index + 1] = [slice(None)] * (array.ndim - actual_len)
  else:
    idx += [slice(None)] * (array.ndim - actual_len)

  def take(x: jax.Array) -> jax.Array:
    actual_idx = []
    i = 0
    for a, b in zip(array.shape, x.shape):
      while idx[i] is None:
        actual_idx.append(None)
        i += 1
      if a == b or idx[i] == slice(None):
        actual_idx.append(idx[i])
      elif isinstance(idx[i], int):
        actual_idx.append(idx[i] // (a // b))
      elif b == 1:
        actual_idx.append(slice(None))
      else:
        raise ValueError(f'Unsupported indexing {idx} for {array.shape}.')
      i += 1
    actual_idx.extend(idx[i:])
    return x[tuple(actual_idx)]

  return jax.tree.map(take, array)


def validate_qarray(array: QArray):
  """Validates the internal consistency of a QArray."""
  if not isinstance(array.qvalue, jax.Array):
    return  # don't check if qvalue is nn.Partitioned, pl.BlockSpec, etc.
  if array.qvalue.ndim != array.scale.ndim:
    raise ValueError(
        f'Scale {array.scale.shape} should have the same rank as qvalue'
        f' {array.qvalue.shape}.'
    )
  if not all(a % b == 0 for a, b in zip(array.qvalue.shape, array.scale.shape)):
    raise ValueError(
        f'Scale {array.scale.shape} should be broadcastable to qvalue'
        f' {array.qvalue.shape}.'
    )
  if array.qvalue.dtype.itemsize > 1:
    raise ValueError(f'{array.qvalue.dtype} is not a valid type for qvalue.')
  if array.scale.dtype not in (jnp.bfloat16, jnp.float32, jnp.float64):
    raise ValueError(f'{array.scale.dtype} is not a valid type for scale.')
  if array.zero_point is not None:
    if array.zero_point.ndim != array.qvalue.ndim:
      raise ValueError(
          f'Zero point {array.zero_point.shape} should have the same rank as'
          f' qvalue {array.qvalue.shape}.'
      )
    if not all(
        a % b == 0 for a, b in zip(array.qvalue.shape, array.zero_point.shape)
    ):
      raise ValueError(
          f'Zero point {array.zero_point.shape} should be broadcastable to'
          f' qvalue {array.qvalue.shape}.'
      )
    if array.zero_point.dtype != array.qvalue.dtype:
      raise ValueError(
          f'Zero point {array.zero_point.dtype} should have the same dtype as'
          f' qvalue {array.qvalue.dtype}.'
      )


# ---------------------------------------------
# Quantization and dequantization of QArray.
# ---------------------------------------------


@dataclasses.dataclass(slots=True, frozen=True, kw_only=True)
class HowToQuantize:
  """Determines how to quantize an array."""

  # The the logical type of the qvalue.
  # E.g. jnp.int8, jnp.int4, jnp.float8_*, nf4, etc.
  # Actual qvalue dtype is determined by the quantization method.
  qtype: jax.typing.DTypeLike
  # Channelwise axes will have individual scales, which has the same effect
  # as setting their tile sizes to 1 in tiled_axes.
  channelwise_axes: Collection[int] = ()
  # Tiled axes have subchannel quantization enabled. The value is a mapping
  # from the tiled axis to the tile size. If the tile size is a float, it has
  # to be "1 / tile_count" and the actual tile size will be
  # round(axis_size * tile_size). Note that 1 and 1.0 have very different
  # meanings: a tile size of 1 means to use per-channel scale, while a
  # tile size of 1.0 means to use shared scale.
  tiled_axes: Mapping[int, int | float] = dataclasses.field(
      default_factory=dict
  )
  # The calibration method to use. The format is <method>[,<args>], e.g.
  # "absmax" or "fixed,-10,10". Check calibrate() for supported methods.
  calibration_method: str = 'absmax'
  # Noise function to use for stochastic rounding.
  noise_fn: numerics.NoiseFn | None = None


ShapeT: TypeAlias = Sequence[int]
MaybeQArray: TypeAlias = jax.Array | QArray


def get_scale_shape(array_shape: ShapeT, how: HowToQuantize) -> ShapeT:
  """Returns the scale shape."""
  if set(how.channelwise_axes) & how.tiled_axes.keys():
    raise ValueError('The same axis cannot be both channelwise and tiled.')
  scale_shape = []
  for axis, dim in enumerate(array_shape):
    if axis in how.channelwise_axes:
      scale_shape.append(dim)
    elif axis in how.tiled_axes:
      tile_size = how.tiled_axes[axis]
      if isinstance(tile_size, float):
        tile_size = round(dim * tile_size)
      if tile_size <= 0 or dim % tile_size != 0:
        raise ValueError(f'{array_shape} cannot be tiled as {how.tiled_axes}.')
      scale_shape.append(dim // tile_size)
    else:
      scale_shape.append(1)
  return tuple(scale_shape)


def transpose_array(
    array: jax.Array, transpose: Sequence[int | None]
) -> jax.Array:
  """Enhanced version of jnp.transpose.

  * It allows missing and new axes in the transpose list. The missing axes will
    be squeezed away, and the new axes will be added with size 1.
  * It's pallas-friendly as it will try to use reshape and simpler transpose
    instead of direct transpose when possible.

  Args:
    array: The array to transpose.
    transpose: The transpose order.

  Returns:
    The transposed array.
  """
  if any(l > 1 for a, l in enumerate(array.shape) if a not in transpose):
    raise ValueError(f'Cannot transpose {array.shape} as {transpose}.')
  used_axes = [a for a in transpose if a is not None and array.shape[a] != 1]
  # If used_axes is already in order, no actual transpose is needed and we can
  # just reshape the array.
  if sorted(used_axes) == used_axes:
    return array.reshape(
        [1 if a is None else array.shape[a] for a in transpose]
    )
  # Because transpose is not generally supported in pallas kernels, we try to
  # avoid complex transposes here by calling squeeze first. For example, for
  # transpose [1, 2, None], instead of just calling transpose(1, 2, 0), we call
  # squeeze(0).expand(2).
  return (
      array.squeeze([a for a in range(array.ndim) if a not in used_axes])
      .transpose([sum(i < a for i in used_axes) for a in used_axes])
      .reshape([1 if a is None else array.shape[a] for a in transpose])
  )


def split_axis(
    array: jax.Array, tiled_axes: Mapping[int, int | float]
) -> jax.Array:
  """Reshape the array where the axis is split into (tile_count, tile_size)."""
  new_shape = []
  for axis, dim in enumerate(array.shape):
    if axis in tiled_axes:
      tile_size = tiled_axes[axis]
      if isinstance(tile_size, float):
        tile_size = round(dim * tile_size)
      if dim % tile_size != 0:
        raise ValueError(f'{array.shape} cannot be tiled as {tiled_axes}.')
      new_shape.append(dim // tile_size)
      new_shape.append(tile_size)
    else:
      new_shape.append(dim)
  return array.reshape(new_shape)


def get_tiled_axes(array: QArray) -> dict[int, int]:
  """Infers the tiled axes from a QArray.

  Args:
    array: The QArray to infer the tiled axes from.

  Returns:
    A dict from tiled axis to tile size.
  """
  tiled_axes = {}
  for i, (j, k) in enumerate(zip(array.qvalue.shape, array.scale.shape)):
    if j != k and k != 1:
      tiled_axes[i] = j // k
  return tiled_axes


def call_with_generic_broadcast(
    op: Callable[[jax.Array, jax.Array], jax.Array], x: jax.Array, y: jax.Array
):
  """Call an element-wise binary op with generic broadcast."""
  assert x.ndim == y.ndim
  x_shape, y_shape, o_shape = [], [], []
  for a, b in zip(x.shape, y.shape):
    o_shape.append(max(a, b))
    if a == b or a == 1 or b == 1:
      x_shape.append(a)
      y_shape.append(b)
    elif a % b == 0:
      x_shape.extend((b, a // b))
      y_shape.extend((b, 1))
    elif b % a == 0:
      x_shape.extend((a, 1))
      y_shape.extend((a, b // a))
    else:
      raise ValueError(f'Cannot broadcast between {x.shape} {y.shape}')
  return op(x.reshape(x_shape), y.reshape(y_shape)).reshape(o_shape)


def calibrate(array: jax.Array, how: HowToQuantize) -> dict[str, jax.Array]:
  """Calibrates the array.

  Args:
    array: The array to calibrate.
    how: How to quantize the array.

  Returns:
    A dict of quantization statistics, e.g. {'min': ..., 'max': ...} for
    asymmetric quantization, or {'absmax': ...} for symmetric quantization.
    Each value in the dict has the same shape as the (expected) scale.
  """
  reduce_axes = []  # axes to calibrate.
  tiled_axes_offset = 0
  for axis, _ in enumerate(array.shape):
    if axis in how.channelwise_axes:
      continue  # no reduce needed.
    if axis in how.tiled_axes:
      tiled_axes_offset += 1  # reduce the tile_size rather than num_tiles.
    reduce_axes.append(axis + tiled_axes_offset)

  # The returned calibration values should have the same shape as the scale.
  shape = get_scale_shape(array.shape, how)
  array = split_axis(array, how.tiled_axes)

  # Parse the calibration method.
  method, *args = how.calibration_method.lower().split(',')
  args = [float(a) for a in args]
  if method == 'minmax':
    min_array = jnp.min(array, axis=reduce_axes, keepdims=True)
    max_array = jnp.max(array, axis=reduce_axes, keepdims=True)
    # Ensure min_array <= 0 <= max_array so that 0 can be accurately quantized.
    min_array = jnp.clip(min_array, max=0)
    max_array = jnp.clip(max_array, min=0)
    if args:  # args[0] is the scale factor.
      min_array = min_array * args[0]
      max_array = max_array * args[0]
    return {'min': min_array.reshape(shape), 'max': max_array.reshape(shape)}
  elif method == 'absmax':
    absmax = jnp.max(jnp.abs(array), axis=reduce_axes, keepdims=True)
    if args:  # args[0] is the scale factor.
      absmax = absmax * args[0]
    return {'absmax': absmax.reshape(shape)}
  elif method == 'rms':
    rms = jnp.sqrt(jnp.mean(jnp.square(array), axis=reduce_axes, keepdims=True))
    if not args:
      raise ValueError('A scale factor is required for RMS calibration.')
    return {'absmax': (rms * args[0]).reshape(shape)}
  elif method == 'fixed':
    if len(args) not in (1, 2):
      raise ValueError('A fixed range is required for fixed calibration.')
    if len(args) == 1:
      args = (-args[0], args[0])
    if args[0] > 0 or args[1] < 0 or args[0] >= args[1]:
      raise ValueError('The range must contain 0 and be non-empty.')
    # Fixed calibration is always per-tensor.
    shape = tuple(1 for _ in shape)
    if args[0] + args[1] == 0:
      return {'absmax': jnp.full(shape, args[1], array.dtype)}
    return {
        'min': jnp.full(shape, args[0], array.dtype),
        'max': jnp.full(shape, args[1], array.dtype),
    }
  else:
    raise ValueError(f'Unsupported calibration: {how.calibration_method}')


def compute_scale_zero_point(
    calibration: Mapping[str, jax.Array], qtype: jax.typing.DTypeLike
) -> tuple[jax.Array, jax.Array | None]:
  """Computes the scale and zero_point from the calibration result.

  Args:
    calibration: The calibration returned by calibrate().
    qtype: The dtype of the qvalue.

  Returns:
    A tuple of the scale and zero_point. The zero_point is None in symmetric
    quantization.
  """
  if 'min' in calibration and 'max' in calibration:
    qmin, qmax = numerics.get_asymmetric_bound(qtype)
    scale = (calibration['max'] - calibration['min']) / (qmax - qmin)
    scale = jnp.where(scale == 0, 1, scale)  # Scale shouldn't be 0.
    zero_point = qmin - calibration['min'] / scale
    zero_point = numerics.convert_to(zero_point, qtype)
  elif 'absmax' in calibration:
    qmax = numerics.get_symmetric_bound(qtype)
    scale = calibration['absmax'] / qmax
    # Maybe adding an epsilon (1e-7) is faster?
    scale = jnp.where(scale == 0, 1, scale)  # Scale shouldn't be 0.
    zero_point = None
  else:
    raise ValueError(f'Unsupported calibration: {calibration}')
  return scale, zero_point


def quantize_with_scale_zero_point(
    array: jax.Array,
    qtype: jax.typing.DTypeLike,
    scale: jax.Array,
    zero_point: jax.Array | None,
    noise_fn: numerics.NoiseFn | None = None,
) -> QArray:
  """Quantizes an array with the given scale and zero_point.

  Args:
    array: The array to quantize.
    qtype: The logical type used for quantization.
    scale: The scale to use.
    zero_point: The zero_point to use.
    noise_fn: The noise function to add to the quantized array for stochastic
      rounding.

  Returns:
    The quantized array.
  """
  if not numerics.should_quantize(array.dtype):
    raise ValueError(f'Refuse to quantize: {array.dtype}')
  if zero_point is not None and zero_point.shape != scale.shape:
    raise ValueError(
        f'Expect zero_point shape {scale.shape} but got {zero_point.shape}'
    )

  # Ensure that the scale has the same dtype as the fp array, because
  # dequantize() uses the scale dtype to reconstruct the original array.
  scale = scale.astype(array.dtype)

  qvalue = call_with_generic_broadcast(jnp.divide, array, scale)
  if zero_point is not None:
    qvalue = call_with_generic_broadcast(
        jnp.add, qvalue, zero_point.astype(qvalue.dtype)
    )
  qvalue = numerics.convert_to(qvalue, qtype, noise_fn)
  return QArray(qvalue, scale, zero_point, qtype)


def quantize(
    array: jax.Array,
    how: HowToQuantize,
) -> QArray:
  """Quantizes an array using a dynamic range."""
  calibration = calibrate(array, how)
  scale, zero_point = compute_scale_zero_point(calibration, how.qtype)
  return quantize_with_scale_zero_point(
      array, how.qtype, scale, zero_point, how.noise_fn
  )


def dequantize(array: QArray) -> jax.Array:
  """Dequantizes an array. The reverse of |quantize|.

  Args:
    array: The quantized array to dequantize.

  Returns:
    The dequantized array, whose dtype is the same as the scale's dtype.
  """
  validate_qarray(array)
  qvalue = numerics.convert_from(array.qvalue, array.qtype)
  qvalue = qvalue.astype(array.scale.dtype)
  if array.zero_point is not None:
    qvalue = call_with_generic_broadcast(
        jnp.subtract, qvalue, array.zero_point.astype(qvalue.dtype)
    )
  return call_with_generic_broadcast(jnp.multiply, qvalue, array.scale)


def clip_to_calibration(
    array: jax.Array,
    calibration: Mapping[str, jax.Array],
    tiled_axes: Mapping[int, int | float],
) -> jax.Array:
  """Clips an array to the calibration range."""
  original_shape = array.shape
  array = split_axis(array, tiled_axes)
  if 'min' in calibration and 'max' in calibration:
    min_array = split_axis(calibration['min'], {a: 1 for a in tiled_axes})
    max_array = split_axis(calibration['max'], {a: 1 for a in tiled_axes})
    array = jnp.clip(array, min_array, max_array)
  elif 'absmax' in calibration:
    absmax = split_axis(calibration['absmax'], {a: 1 for a in tiled_axes})
    array = jnp.clip(array, -absmax, absmax)
  else:
    raise ValueError(f'Unsupported calibration: {calibration}')
  return array.reshape(original_shape)


def get_accumulator_and_result_type(
    *args: MaybeQArray,
    preferred_element_type: jax.typing.DTypeLike | None,
) -> tuple[jax.typing.DTypeLike, jax.typing.DTypeLike]:
  """jnp.result_type for QArray.

  Accumulator type is the dtype used for the dot_general computation.
  Result type is the dtype of the final result.

  Args:
    *args: The arguments to dot_general.
    preferred_element_type: The preferred element type for dot_general.

  Returns:
    A tuple of the accumulator type and the result type.
  """
  qvalue_dtypes, dequant_dtypes = [], []
  for arg in args:
    if isinstance(arg, QArray):
      qvalue_dtypes.append(arg.qvalue.dtype)  # note qtype can be different.
      dequant_dtypes.append(arg.scale.dtype)
    else:
      qvalue_dtypes.append(arg.dtype)
      dequant_dtypes.append(arg.dtype)

  # Result type should only depend on dequant_dtype and preferred_element_type.
  result_type = preferred_element_type
  if result_type is None:
    # There's no dtype promotion path for fp8 or lower, and int4 or lower.
    # We manually upcast them to bf16 or int32.
    for i, t in enumerate(dequant_dtypes):
      if t.itemsize <= 1:
        dequant_dtypes[i] = jnp.int32 if 'int' in t.name else jnp.bfloat16
    result_type = jnp.result_type(*dequant_dtypes)

  # Accumulator type should be the same as result type except for int x int.
  accumulator_type = result_type
  if all('int' in t.name for t in qvalue_dtypes):
    accumulator_type = jnp.int32

  return accumulator_type, result_type
