# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from __future__ import annotations

import dataclasses as dtcl
from enum import Enum as enum_t
from typing import Any, Dict, Sequence, Union

import numpy as nmpy
import pca_b_stream as pcst
import scipy.ndimage as spim
import skimage.feature as ftre
from cell_tracking_BC.standard.uid import Identity
from PIL import Image as pil_image_t

array_t = nmpy.ndarray


class compartment_id_t(enum_t):
    CELL = 0
    CYTOPLASM = 1
    NUCLEUS = 2


@dtcl.dataclass(repr=False, eq=False)
class compartment_t:
    centroid: array_t = None  # In frame coordinates
    bb_slices: tuple[slice, slice] = None  # bb=bounding box; In frame coordinates
    touches_border: bool = None
    map_stream: bytes = None  # Built from a numpy.bool_ array
    area: int = None
    features: Dict[str, Any] = dtcl.field(init=False, default_factory=dict)

    @classmethod
    def NewFromMap(cls, map_: array_t, /, *, is_plain: bool = True) -> compartment_t:
        """
        is_plain: Means "has no holes"
        """
        if is_plain:
            centroid = CompartmentReference(map_)
        else:
            # Average coordinates should be a good enough approximation of the reference pixel of the filled map
            pixels = nmpy.nonzero(map_)
            centroid_as_it = (nmpy.mean(_per_dim) for _per_dim in pixels)
            centroid = nmpy.fromiter(centroid_as_it, dtype=nmpy.float64)

        map_as_pil = pil_image_t.fromarray(map_)
        auto_crop_lengths = map_as_pil.getbbox()
        # auto_crop_lengths[2 and 3] already include the +1 for slices
        bb_slices = (
            slice(auto_crop_lengths[1], auto_crop_lengths[3]),
            slice(auto_crop_lengths[0], auto_crop_lengths[2]),
        )
        touches_border = (
            (auto_crop_lengths[0] == 0)
            or (auto_crop_lengths[1] == 0)
            or (auto_crop_lengths[2] == map_.shape[1])
            or (auto_crop_lengths[3] == map_.shape[0])
        )

        cropped = map_as_pil.crop(auto_crop_lengths)
        # Dtype must be boolean to allow the use as array indexing
        map_stream = pcst.PCA2BStream(nmpy.array(cropped, dtype=nmpy.bool_))

        instance = cls(
            centroid=centroid,
            bb_slices=bb_slices,
            touches_border=touches_border,
            map_stream=map_stream,
            area=nmpy.count_nonzero(map_),
        )

        return instance

    def AddFeature(self, name: str, value: Any, /) -> None:
        """"""
        self.features[name] = value

    @property
    def available_features(self) -> Sequence[str]:
        """"""
        return sorted(self.features.keys())

    def BBMap(self) -> array_t:
        """
        BB=Bounding box=Map limited to the compartment bounding box. Dtype: numpy.bool_
        """
        return pcst.BStream2PCA(self.map_stream)

    @staticmethod
    def EmptyMap(
        shape: Sequence[int], /, *, as_boolean: bool = False
    ) -> tuple[array_t, Union[bool, int]]:
        """"""
        if as_boolean:
            dtype = nmpy.bool_
            one = True
        else:
            dtype = nmpy.int8  # Do not use uint8 to allow map subtraction
            one = 1

        return nmpy.zeros(shape, dtype=dtype), one

    def Map(
        self, shape: Sequence[int], /, *, as_boolean: bool = False, margin: float = None
    ) -> array_t:
        """"""
        output, one = compartment_t.EmptyMap(shape, as_boolean=as_boolean)

        output[self.bb_slices][self.BBMap()] = one
        if (margin is not None) and (margin != 0.0):
            output = AdjustedMapWithMargin(output, self.area, margin)

        return output

    def NonZeroPixels(self, shape: Sequence[int], /) -> tuple[array_t, array_t]:
        """"""
        return nmpy.nonzero(self.Map(shape))

    def __hash__(self) -> int:
        """
        Note that (from Python documentation:
            if it defines __eq__() but not __hash__(), its instances will not be usable as items in hashable collections
        """
        return hash((tuple(self.centroid), self.map_stream))

    __repr__ = Identity

    def __str__(self) -> str:
        """"""
        return (
            f"{repr(self)}\n"
            f"    Centroid: {self.centroid}\n"
            f"    BBox slices: {self.bb_slices}\n"
            f"    Stream: {self.map_stream}\n"
            f"    Features: {tuple(self.features.keys())}\n"
        )


def AdjustedMapWithMargin(map_: array_t, area: int, margin: float, /) -> array_t:
    """"""
    dtype = map_.dtype
    if margin > 0.0:
        map_ = nmpy.logical_not(map_)
    elif margin == 0.0:
        return map_

    distance = spim.distance_transform_edt(map_)
    if margin > 0.0:
        thresholds = nmpy.arange(0.0, -nmpy.amax(distance), -1.0)
        distance = 0.1 - distance
    else:
        thresholds = nmpy.arange(0.0, nmpy.amax(distance), 1.0)

    margin_target = abs(margin) / 100.0

    new_map = map_
    for threshold in thresholds[1:]:
        previous_map = new_map
        new_map = distance > threshold
        new_area = nmpy.count_nonzero(new_map)
        if new_area == 0:
            return previous_map.astype(dtype, copy=False)
        if abs(new_area - area) / area >= margin_target:
            return new_map.astype(dtype, copy=False)

    return new_map.astype(dtype, copy=False)


def CompartmentReference(compartment: array_t, /) -> array_t:
    """"""
    # By default, ftre.peak_local_max excludes peaks on the frame border. This can be parameterized otherwise,
    # but this would lead to an "off-center" peak anyway. Instead, the compartment map is padded.
    padded = nmpy.pad(compartment, 1)
    distance_map = spim.distance_transform_edt(padded)
    output = ftre.peak_local_max(distance_map, num_peaks=1)[0] - 1

    return output
