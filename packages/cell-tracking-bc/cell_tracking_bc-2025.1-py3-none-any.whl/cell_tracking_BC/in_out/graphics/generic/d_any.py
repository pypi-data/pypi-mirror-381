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

from typing import Optional, Sequence

import numpy as nmpy
import skimage.measure as msre
from cell_tracking_BC.type.analysis import analysis_t
from cell_tracking_BC.type.compartment.base import compartment_id_t
from cell_tracking_BC.type.track.multiple.structured import tracks_t

array_t = nmpy.ndarray


def CellContours(
    analysis: analysis_t, with_segmentation: bool, /
) -> Optional[Sequence[Sequence[array_t]]]:
    """"""
    if with_segmentation and (analysis.segmentations is not None):
        output = []
        for segmentation in analysis.segmentations.Compartments(compartment_id_t.CELL):
            output.append(msre.find_contours(segmentation, level=0.5))
    else:
        output = None

    return output


def CellTracks(analysis: analysis_t, with_track_labels: bool, /) -> Optional[tracks_t]:
    """"""
    with_track_labels = with_track_labels and (analysis.tracks is not None)
    if with_track_labels:
        output = analysis.tracks
    else:
        output = None

    return output
