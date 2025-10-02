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

import sys as sstm

from rich.progress import BarColumn as progress_bar_t
from rich.progress import Progress as progress_t
from rich.progress import TimeElapsedColumn as time_elapsed_t
from rich.progress import TimeRemainingColumn as time_remaining_t


class silent_progress_t:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


def NewRichProgress(
    *, should_be_silent: bool = False
) -> progress_t | silent_progress_t:
    """"""
    if should_be_silent:
        return silent_progress_t()

    sstm.stdout.flush()
    sstm.stderr.flush()

    return progress_t(
        "[progress.description]{task.description}",
        progress_bar_t(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "[progress.elapsed]+",
        time_elapsed_t(),
        "/ [progress.remaining]-",
        time_remaining_t(),
        refresh_per_second=0.5,
    )


# from typing import Iterable
# from rich.progress import ProgressType as element_t
# from rich.progress import TaskID as progress_id_t
# tracked_elements_t = Iterable[element_t]
# def NewProgressTask(
#     progress: progress_t | silent_progress_t,
#     iterable: Iterable,
#     /,
#     *,
#     description: str = "Progress",
#     total: int | None = None,
#     update_period: float = 1.0,
# ) -> tuple[progress_id_t, tracked_elements_t] | tuple[int, None]:
#     """"""
#     if isinstance(progress, silent_progress_t):
#         return 0, None
#
#     if total is None:
#         kwargs = {}
#     else:
#         kwargs = {"total": total}
#     uid = progress.add_task(description)
#     elements = progress.track(
#         iterable, task_id=uid, update_period=update_period, **kwargs
#     )
#
#     sstm.stdout.flush()
#
#     return uid, elements


# @dtcl.dataclass(repr=False, eq=False)
# class progress_context_t:
#     progress: progress_t | silent_progress_t
#     #
#     last: dtcl.InitVar[int | Iterable]
#     first: dtcl.InitVar[int] = 0
#     total: dtcl.InitVar[int] = 0  # Used only if not isinstance(last, int)
#     description: dtcl.InitVar[str] = "Progress"
#     update_period: dtcl.InitVar[float] = 1.0
#     #
#     is_silent: bool = dtcl.field(init=False)
#     uid: progress_id_t = dtcl.field(init=False)
#     elements: tracked_elements_t = dtcl.field(init=False)
#
#     def __post_init__(self, last, first, total, description, update_period) -> None:
#         """"""
#         if isinstance(last, int):
#             iterable = range(first, last + 1)
#             kwargs = {}
#         else:
#             iterable = last
#             kwargs = {"total": total}
#
#         self.is_silent = isinstance(self.progress, silent_progress_t)
#         if self.is_silent:
#             self.elements = iterable
#         else:
#             self.uid = self.progress.add_task(description)
#             self.elements = self.progress.track(
#                 iterable, task_id=self.uid, update_period=update_period, **kwargs
#             )
#             sstm.stdout.flush()
#
#     def UpdateDescription(self, description: str, /) -> None:
#         """"""
#         if self.is_silent:
#             return
#
#         self.progress.update(self.uid, description=description)
