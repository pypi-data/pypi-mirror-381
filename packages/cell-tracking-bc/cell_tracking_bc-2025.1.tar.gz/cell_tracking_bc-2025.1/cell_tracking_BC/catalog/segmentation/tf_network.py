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

from pathlib import Path as path_t
from typing import Callable, Sequence, Union

import keras as kras
import keras.models as modl
import numpy as nmpy
from cell_tracking_BC.task.processing.base import processing_h
from logger_36 import L

array_t = nmpy.ndarray


def InputSizeOfTFNetwork(network_path: Union[str, path_t], /) -> Sequence[int]:
    """
    Input size for single frames = network input layer shape with first (time, which appears as None in network summary)
    and last dimensions (channels, but only one here) removed.
    """
    network = modl.load_model(network_path)
    layer = network.get_layer(index=0)

    return layer.input.shape[1:-1]


def SegmentationsWithTFNetwork(
    frames: Sequence[array_t],
    network_path: path_t | str,
    /,
    *,
    LoadFromWeights: Callable[[int, int, int, str], kras.Model] | None = None,
    threshold: float = 0.9,
    PreProcessed: processing_h | None = None,
    PostProcessed: processing_h | None = None,
) -> tuple[Sequence[array_t], Sequence[array_t]]:
    """
    PostProcessed: Could be used to clear border objects. However, since one might want to segment cytoplasms and
    nuclei, clearing border objects here could lead to clearing a cytoplasm while keeping its nucleus. Consequently,
    clearing border objects here, i.e. independently for each segmentation task, is not appropriate.
    """
    if isinstance(network_path, str):
        network_path = path_t(network_path)

    output_sgm = []
    output_prd = []

    if PreProcessed is not None:
        frames = tuple(PreProcessed(_frm) for _frm in frames)
    if PostProcessed is None:
        PostProcessed = lambda _prm: _prm

    frames = nmpy.array(frames, dtype=nmpy.float32)
    if frames.ndim == 3:
        frames = nmpy.expand_dims(frames, axis=3)

    if network_path.is_file():  # Possible extension(s): h5.
        network = LoadFromWeights(*frames.shape[1:], str(network_path))
    else:
        network = modl.load_model(network_path)
    predictions = network.predict(frames, verbose=1)

    # First dimension is time (needs to be removed for single frame reshape below), last
    # dimension is channels (equal to one, thus removed).
    shape = network.layers[0].input_shape[0][1:-1]

    for t_idx, prediction in enumerate(predictions):
        reshaped = nmpy.reshape(prediction, shape)
        segmentation = reshaped > threshold
        post_processed = PostProcessed(segmentation)
        if nmpy.amax(post_processed.astype(nmpy.uint8)) == 0:
            L.warning(f"Time point {t_idx}: Empty segmentation")

        output_prd.append(reshaped)
        output_sgm.append(post_processed)

    return output_sgm, output_prd


# import tensorflow as tsfl
# import tensorrt as tsrt
# def LogTensorflowDetailsDetails() -> None:
#     """"""
#     system_details = tsfl.sysconfig.get_build_info()
#     L.info(
#         f"TENSORFLOW DETAILS\n"
#         f"          Tensorflow: {tsfl.version.VERSION}\n"
#         f"    Tensorflow Build: {tsfl.sysconfig.get_build_info()}\n"
#         f"            TensorRT: {tsrt.__version__}\n"
#         f"                Cuda: {system_details['cuda_version']}\n"
#         f"               CuDNN: {system_details['cudnn_version']}\n"
#         f"                CPUs: {tsfl.config.list_physical_devices('CPU')}\n"
#         f"                GPUs: {tsfl.config.list_physical_devices('GPU')}"
#     )
