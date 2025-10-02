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
import datetime as dttm
import re as regx
from pathlib import Path as path_t
from typing import Callable, Dict, Sequence

import numpy as nmpy
import tifffile as tiff
from cell_tracking_BC.in_out.graphics.type.axes import axes_2d_t as axes_t
from cell_tracking_BC.in_out.graphics.type.context import context_t
from cell_tracking_BC.in_out.graphics.type.event import (
    event_h,
    event_key_h,
    event_scroll_h,
)
from cell_tracking_BC.in_out.graphics.type.s_drawer_2d import s_drawer_2d_t
from cell_tracking_BC.type.analysis import analysis_t

# from cell_tracking_BC.type.acquisition.sequence import AllChannels, sequence_t
from cell_tracking_BC.type.compartment.cell import cell_t

array_t = nmpy.ndarray

all_versions_h = Dict[str, tuple[tuple[int, int], Sequence[array_t]]]
conversion_fct_h = Callable[..., array_t]


@dtcl.dataclass(repr=False, eq=False)
class s_viewer_2d_t(s_drawer_2d_t):
    _AsAnnotatedVolume: conversion_fct_h = None

    @classmethod
    def _NewForSequence(
        cls,
        analysis: analysis_t,
        frames,  #: frames_t,
        dbe: context_t,
        /,
        *,
        version: str = None,
        with_segmentation: bool = False,
        with_cell_labels: bool = True,
        main_frames: Sequence[array_t] = None,
        all_cells: Sequence[Sequence[cell_t]] = None,
        with_track_labels: bool = True,
        in_axes: axes_t = None,
        with_ticks: bool = True,
    ) -> s_viewer_2d_t:
        """"""
        drawer = s_drawer_2d_t._NewForSequence(
            analysis,
            # AllVersionsOfSequence,
            dbe,
            with_segmentation=with_segmentation,
            with_cell_labels=with_cell_labels,
            main_frames=main_frames,
            all_cells=all_cells,
            with_track_labels=with_track_labels,
            in_axes=in_axes,
            with_ticks=with_ticks,
        )
        if in_axes is None:
            current_time_point = None
            slider = dbe.NewSlider(drawer.figure, analysis.sequence.length)
        else:
            current_time_point = 0
            slider = None

        arguments = {
            "figure": drawer.figure,
            "axes": drawer.axes,
            "current_time_point": current_time_point,
            "slider": slider,
        }
        instance = cls(**arguments)
        already_set = tuple(arguments.keys())
        for field in dtcl.fields(drawer):
            if (name := field.name) not in already_set:
                setattr(instance, name, getattr(drawer, name))

        instance._ActivateEventProcessing(False)

        return instance

    def _ActivateEventProcessing(self, more_than_one_version: bool, /) -> None:
        """"""
        self.figure.ActivateEvent("key_press_event", self._OnKeyPress)
        if more_than_one_version:
            self.figure.ActivateEvent("button_press_event", self._OnButtonPress)
        if self.slider is not None:
            self.figure.ActivateEvent("scroll_event", self._OnScrollEvent)

    def _OnKeyPress(self, event: event_key_h, /) -> None:
        """"""
        if self.dbe.KeyEventKey(event).lower() == "s":
            if self._AsAnnotatedVolume is None:
                print(
                    f'"{self.__class__.SetConversionToAnnotatedVolume.__name__}" has not been called; '
                    f"Saving the sequence is therefore disabled"
                )
                return

            print("Sequence saving in progress...")
            volume = self.AsAnnotatedVolume()

            illegal = "[^-_a-zA-Z0-9]"
            version = ""  # regx.sub(illegal, "", self.current_version)
            now = regx.sub(illegal, "-", dttm.datetime.now().isoformat())
            path = path_t.home() / f"sequence-{version}-{now}.tif"
            if path.exists():
                print(f"{path}: Existing path; Cannot override")
                return

            tiff.imwrite(
                str(path),
                volume,
                photometric="rgb",
                compression="deflate",
                planarconfig="separate",
                metadata={"axes": "XYZCT"},
            )
            print(f"Annotated sequence saved at: {path}")

    def _OnButtonPress(self, event: event_h, /) -> None:
        """"""
        if self.dbe.IsTargetOfEvent(self.axes, event):
            pass
            # self.SelectNextVersion()
        elif (self.slider is not None) and self.dbe.IsTargetOfEvent(
            self.dbe.SliderAxes(self.slider), event
        ):
            pass
            # self.SelectVersionAndTimePoint(
            #     time_point=self.dbe.SliderValue(self.slider), force_new_time_point=True
            # )

    def _OnScrollEvent(self, event: event_scroll_h) -> None:
        """"""
        value = self.dbe.SliderValue(self.slider)
        bounds = self.dbe.SliderBounds(self.slider)
        new_value = round(value + nmpy.sign(self.dbe.ScrollEventStep(event)))
        new_value = min(max(new_value, bounds[0]), bounds[1])
        if new_value != value:
            pass
            # self.SelectVersionAndTimePoint(time_point=new_value)

    def SetConversionToAnnotatedVolume(
        self, ConversionFct: conversion_fct_h, /
    ) -> None:
        """
        The goal of this method is to provide a "solution" to circular imports
        """
        self._AsAnnotatedVolume = ConversionFct

    def AsAnnotatedVolume(self) -> array_t:
        """"""
        return nmpy.zeros((10, 10))
        # frames = self.all_versions[self.current_version][1]
        # drawer = self.__class__._NewForSequence(
        #     frames,
        #     AllChannels,
        #     self.dbe,
        #     with_segmentation=self.cell_contours is not None,
        #     with_cell_labels=self.with_cell_labels,
        #     main_frames=self.main_frames,
        #     all_cells=self.cells,
        #     with_track_labels=self.tracks is not None,
        #     with_ticks=False,
        # )
        # drawer.cell_contours = self.cell_contours
        # drawer.tracks = self.tracks
        #
        # return self._AsAnnotatedVolume(
        #     frames,
        #     "",
        #     False,
        #     False,
        #     False,
        #     drawer=drawer,
        # )
