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

from typing import Any, Dict

try:
    # noinspection PyPackageRequirements
    import vedo.colors as clrs
except ModuleNotFoundError:
    clrs = None

import cell_tracking_BC.in_out.graphics.dbe.vedo.missing as vmsg
from cell_tracking_BC.in_out.graphics.type.color import ColorAndAlpha

FONT_SIZE_DEFAULT = 14
FONT_SIZE_CONVERSION = {
    "xx-small": 8,
    "x-small": 10,
    "small": 12,
    "medium": 14,
    "large": 16,
    "x-large": 18,
    "xx-large": 20,
}

CELL_ANNOTATION_COLOR_DEFAULT = "red"
CELL_ANNOTATION_COLOR_HIGHLIGHT = "magenta"
CELL_ANNOTATION_STYLE_DEFAULT = {
    "c": CELL_ANNOTATION_COLOR_DEFAULT,
    "s": 8,
    "depth": 1,
    "justify": "centered",
    "alpha": 0.95,
}


def CellAnnotationStyle(highlighted: bool, _: bool, /) -> Dict[str, Any]:
    """"""
    output = CELL_ANNOTATION_STYLE_DEFAULT.copy()

    if highlighted:
        output["c"] = CELL_ANNOTATION_COLOR_HIGHLIGHT
    else:
        output["c"] = CELL_ANNOTATION_COLOR_DEFAULT

    return output


if clrs is None:
    ConvertedTextStyle = vmsg.RaiseMissingVedoException
else:

    def ConvertedTextStyle(style: Dict[str, Any], /) -> Dict[str, Any]:
        """"""
        output = style.copy()

        if "color" in output:
            color, _ = ColorAndAlpha(output["color"], clrs.getColor)
            output["c"] = color
            del output["color"]

        if "fontsize" in output:
            key_or_size = output["fontsize"]
            size = FONT_SIZE_CONVERSION.get(key_or_size, key_or_size)
            output["s"] = size
            del output["fontsize"]

        if "bbox" in output:
            del output["bbox"]

        return output
