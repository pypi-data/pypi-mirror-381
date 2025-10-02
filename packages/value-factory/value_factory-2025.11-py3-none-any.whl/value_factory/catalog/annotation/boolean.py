"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h
from enum import Enum as enum_t

from logger_36.api.message import MessageWithActualExpected
from value_factory.extension.hint import hint_h
from value_factory.type.annotation import annotation_a


class mode_e(enum_t):
    # True value must be listed first.
    true_false = ("True", "False")
    yes_no = ("Yes", "No")
    on_off = ("On", "Off")


_MODES = tuple(mode_e.__members__.keys())
_MODE_INITIALS = "".join(_[0] for _ in _MODES)


class boolean_t(annotation_a):
    ACCEPTED_TYPES: h.ClassVar[hint_h] = bool

    labels: tuple[str, str]

    def __init__(self, mode: str | mode_e, /) -> None:
        """
        If str, can be t[...], y[...], or o[...].
        """
        if isinstance(mode, str):
            index = _MODE_INITIALS.index(mode[0].lower())
            self.labels = mode_e[_MODES[index]].value
        elif isinstance(mode, mode_e):
            self.labels = mode.value
        else:
            raise ValueError(
                MessageWithActualExpected(
                    "Invalid boolean mode", actual=mode, expected=" or ".join(_MODES)
                )
            )

    def __call__(self, value: h.Any, /) -> bool:
        """"""
        return isinstance(value, bool)


"""
COPYRIGHT NOTICE

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

SEE LICENCE NOTICE: file README-LICENCE-utf8.txt at project source root.

This software is being developed by Eric Debreuve, a CNRS employee and
member of team Morpheme.
Team Morpheme is a joint team between Inria, CNRS, and UniCA.
It is hosted by the Centre Inria d'Université Côte d'Azur, Laboratory
I3S, and Laboratory iBV.

CNRS: https://www.cnrs.fr/index.php/en
Inria: https://www.inria.fr/en/
UniCA: https://univ-cotedazur.eu/
Centre Inria d'Université Côte d'Azur: https://www.inria.fr/en/centre/sophia/
I3S: https://www.i3s.unice.fr/en/
iBV: http://ibv.unice.fr/
Team Morpheme: https://team.inria.fr/morpheme/
"""
