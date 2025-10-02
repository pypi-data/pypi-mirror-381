"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2022
SEE COPYRIGHT NOTICE BELOW
"""

from json_any.catalog.module import grph, nmpy, pnds, pypl, sprs, xrry
from json_any.catalog.type.networkx import NETWORKX_CLASSES
from json_any.catalog.type.numpy import NUMPY_ARRAY_CLASSES, NUMPY_SCALAR_CLASSES
from json_any.catalog.type.pandas import PANDAS_CLASSES
from json_any.catalog.type.python import (
    date_t,
    date_time_t,
    decimal_t,
    ellipsis_t,
    enum_t,
    fraction_t,
    function_builtin_t,
    function_t,
    io_bytes_t,
    io_string_t,
    module_t,
    named_tuple_t,
    not_implemented_t,
    # path_pure_t: Not needed.
    py_array_t,
    time_delta_t,
    time_t,
    time_zone_t,
    uuid_t,
)
from json_any.catalog.type.scipy import SCIPY_ARRAY_CLASSES
from json_any.catalog.type.xarray import XARRAY_CLASSES
from json_any.constant.json import MODULE_TYPE_SEPARATOR
from json_any.task.registration import RegisterTypes

# Matches non-builtin types with module-name_type-name.
REGISTERED_QUALIFIED_TYPES: dict[type, str] = {}

RegisterTypes(
    REGISTERED_QUALIFIED_TYPES,
    (
        date_t,
        date_time_t,
        decimal_t,
        ellipsis_t,
        enum_t,
        fraction_t,
        function_t,
        function_builtin_t,
        io_bytes_t,
        io_string_t,
        module_t,
        named_tuple_t,
        not_implemented_t,
        # path_pure_t: Not needed.
        py_array_t,
        time_delta_t,
        time_t,
        time_zone_t,
        uuid_t,
    ),
)

if pypl is not None:
    figure_t = pypl.Figure
    # Unfortunately, figure_t.__module__ is reported as "matplotlib.figure" instead of
    # the expected "matplotlib.pyplot".
    REGISTERED_QUALIFIED_TYPES[figure_t] = (
        f"{pypl.__name__}{MODULE_TYPE_SEPARATOR}{figure_t.__name__}"
    )
if grph is not None:
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, NETWORKX_CLASSES)
if nmpy is not None:
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, NUMPY_SCALAR_CLASSES)
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, NUMPY_ARRAY_CLASSES)
if pnds is not None:
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, PANDAS_CLASSES)
if sprs is not None:
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, SCIPY_ARRAY_CLASSES)
if xrry is not None:
    RegisterTypes(REGISTERED_QUALIFIED_TYPES, XARRAY_CLASSES)

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
