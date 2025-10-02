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

import cell_tracking_BC.in_out.graphics.dbe.matplotlib.d_2 as twod
import cell_tracking_BC.in_out.graphics.dbe.matplotlib.d_3 as thrd
import cell_tracking_BC.in_out.graphics.dbe.matplotlib.d_any as anyd
import cell_tracking_BC.in_out.graphics.dbe.matplotlib.style as styl
from cell_tracking_BC.in_out.graphics.type.context import context_t
from matplotlib.artist import Artist as artist_t

DRAWING_CONTEXT = context_t(
    figure_2d_t=twod.figure_t,
    axes_2d_t=twod.axes_t,
    s_drawer_2d_t=twod.s_drawer_2d_t,
    s_viewer_2d_t=twod.s_viewer_2d_t,
    t_explorer_2d_t=twod.t_explorer_2d_t,
    #
    figure_3d_t=thrd.figure_t,
    axes_3d_t=thrd.axes_t,
    #
    CellAnnotationStyle=styl.CellAnnotationStyle,
    #
    NewSlider=anyd.NewSlider,
    SliderValue=anyd.SliderValue,
    UpdateSlider=anyd.UpdateSlider,
    SliderBounds=lambda _sld: (_sld.valmin, _sld.valmax),
    SliderAxes=lambda _sld: _sld.ax,
    #
    IsVisible=artist_t.get_visible,
    SetVisibility=artist_t.set_visible,
    #
    # _evt: matplotlib.backend_bases.LocationEvent
    IsTargetOfEvent=lambda _axs, _evt: _evt.inaxes is _axs,
    KeyEventKey=lambda _evt: _evt.key,
    ScrollEventStep=lambda _evt: _evt.step,
)
