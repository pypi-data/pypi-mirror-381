"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2022
SEE COPYRIGHT NOTICE BELOW
"""

import types as t

ellipsis_t = t.EllipsisType
function_t = t.FunctionType
function_builtin_t = t.BuiltinFunctionType
module_t = t.ModuleType
not_implemented_t = t.NotImplementedType

import typing as h

named_tuple_t = h.NamedTuple

from array import array as py_array_t
from datetime import date as date_t
from datetime import datetime as date_time_t
from datetime import time as time_t
from datetime import timedelta as time_delta_t
from datetime import timezone as time_zone_t
from decimal import Decimal as decimal_t
from enum import Enum as enum_t
from fractions import Fraction as fraction_t
from io import BytesIO as io_bytes_t
from io import StringIO as io_string_t
from pathlib import PurePath as path_pure_t
from uuid import UUID as uuid_t

PYTHON_BYTE_STRINGS = (bytes, bytearray)
PYTHON_CONTAINERS = (frozenset, list, set, tuple)

import builtins as bltn

PYTHON_TYPES = []
PYTHON_TYPES_W_QUALIFIED_NAME = []

for module in (bltn, h, t):
    for name in dir(module):
        if name[0] == "_":
            continue

        instance = getattr(module, name)
        # /!\ The test on instance module and module name seems useless. Unfortunately,
        # here is an example which makes this coherence check necessary to avoid JSONing
        # failures: types.NoneType.__module__ == "builtins" instead of "types".
        # Moreover, "builtins" does not define NoneType. This is a known issue.
        # See: https://github.com/python/cpython/issues/100129
        if (type(instance) is type) and (instance.__module__ == module.__name__):
            PYTHON_TYPES.append(instance)
            PYTHON_TYPES_W_QUALIFIED_NAME.append(
                (instance, f"{module.__name__}.{name}")
            )
PYTHON_TYPES = set(PYTHON_TYPES)  # For faster searches.


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
