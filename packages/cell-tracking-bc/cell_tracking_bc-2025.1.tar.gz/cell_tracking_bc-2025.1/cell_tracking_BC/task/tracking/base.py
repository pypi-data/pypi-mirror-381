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

import dataclasses as dtcl
from abc import ABC as abc_t
from abc import abstractmethod
from typing import Iterator, Optional, Sequence

import cell_tracking_BC.in_out.text.progress as prgs
import numpy as nmpy
from cell_tracking_BC.type.compartment.cell import cell_t
from cell_tracking_BC.type.track.multiple.structured import tracks_t
from cell_tracking_BC.type.track.multiple.unstructured import unstructured_tracks_t
from logger_36 import L

array_t = nmpy.ndarray


@dtcl.dataclass(repr=False, eq=False)
class tracker_t(abc_t):
    """
    Latest tracking context: it contains all the information about the cells of frame t required to continue the
    tracking with the cells of frame t+1. When the multiple have been extended to the cells of frame t+1, this context
    will store the information about the cells of frame t+1 to get ready for continuing the tracking with the cells of
    frame t+2. This information is called the permanent storage of the context. By default, the permanent storage is
    defined as the attribute cells, a sequence of cell_t, and the temporary storage is defined as the attribute
    next_cells. Additional permanent and temporary attributes will generally be needed by contexts. Note that all these
    attributes go by pair since the method Advance must at least move all the temporary attributes to their permanent
    counterparts. The default implementation already move next_cells to cells. New contexts are in charge of moving the
    other attributes after calling super().Advance(). Similarly, the method DiscoverNextCells temporarily stores the
    discovered cells in next_cells, and new contexts are in charge of computing and storing the others attributes after
    calling super().DiscoverNextCells(next_cells) (See below for more details about permanent and temporary storages.)

    To keep the class as basic as possible, the shape of the frames the tracker will be run on is not stored here. If
    needed by a specific tracker subclass, the subclass should store it.
    """

    cells: Sequence[cell_t] = dtcl.field(init=False, default=None)
    next_cells: Sequence[cell_t] = dtcl.field(init=False, default=None)

    def DiscoverNextCells(self, next_cells: Sequence[cell_t], /) -> None:
        """
        The tracking has been done up to frame t. This method is called when "discovering" the cells of frame t+1. It
        must "temporarily" store all the information about these cells required to extend the tracking.
        """
        self.next_cells = next_cells

    @abstractmethod
    def PredecessorOfCell(
        self, next_cell: cell_t, next_cell_idx: int, /
    ) -> Optional[tuple[cell_t, float]]:
        """
        This method is called successively for all the cells of frame t+1 to extend the tracking track by track. It
        must look among the cells of frame t described in the permanent storage if one can be considered a predecessor
        of the given cell of frame t+1. If none, then it must return None, meaning that the current track ends.
        Otherwise, it must return the predecessor cell and a tracking_affinity measure for the cell association.
        """
        raise NotImplementedError(
            f"{tracker_t.PredecessorOfCell.__name__}: Must be implemented by trackers"
        )

    def Advance(self) -> None:
        """
        This method is called after PredecessorOfCell has been called for all the cells of frame t+1. It must move the
        temporary storage about the cells of frame t+1 created in DiscoverNextCells to the permanent storage that will
        be used in the next tracking iteration that will deal with frame t+2.
        """
        self.cells = self.next_cells

    def Run(
        self, n_time_points: int, cells_per_time_point: Iterator[Sequence[cell_t]], /
    ) -> tracks_t:
        """"""
        unstructured = unstructured_tracks_t()

        with prgs.NewRichProgress() as progress:
            task_id = progress.add_task("Tracking Cells", total=n_time_points)
            for t_idx, next_cells in enumerate(cells_per_time_point):
                if next_cells.__len__() == 0:
                    L.warning(f"No cells at time point {t_idx}.")
                    continue

                self.DiscoverNextCells(next_cells)

                if t_idx > 0:
                    for next_c_idx, next_cell in enumerate(next_cells):
                        associated = self.PredecessorOfCell(next_cell, next_c_idx)
                        if associated is not None:
                            cell, tracking_affinity = associated
                            # float(): to convert from numpy type (and noop otherwise)
                            unstructured.AddTrackSegment(
                                cell, next_cell, t_idx - 1, float(tracking_affinity)
                            )

                self.Advance()

                progress.update(task_id, completed=t_idx + 1)

        return tracks_t.NewFromUnstructuredTracks(unstructured)
