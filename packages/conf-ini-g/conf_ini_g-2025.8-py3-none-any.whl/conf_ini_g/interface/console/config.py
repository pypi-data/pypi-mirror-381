"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2021
SEE COPYRIGHT NOTICE BELOW
"""

import re as rgex
import typing as h
from argparse import ArgumentParser as argument_parser_t
from pathlib import Path as path_t

from conf_ini_g.extension.string import Flattened
from conf_ini_g.type.config import config_t
from conf_ini_g.type.dict import config_typed_h
from value_factory.api.constant import UNSET
from value_factory.api.type import unset_t

parsed_arguments_h = dict[str, str | unset_t]


# Specified INI document file is stored in _INI_DOCUMENT_VARIABLE.
_INI_DOCUMENT_VARIABLE = "ini_path"

_ADVANCED_MODE_OPTION = "advanced-mode"
_ADVANCED_MODE_VARIABLE = "advanced_mode"

# Usage: {section_name}{_SECTION_PARAMETER_SEPARATOR}{parameter_name}.
_SECTION_PARAMETER_SEPARATOR = "-"


def CommandLineParser(
    description: str | None, specification: config_t, /
) -> argument_parser_t:
    """
    Currently, controlled parameters cannot be passed on the command line.
    """
    output = argument_parser_t(description=description, allow_abbrev=False)
    # This argument is optional because all parameters can be explicitly passed as
    # arguments (CLI mode), or nothing can be passed at all (GUI mode).
    output.add_argument(
        dest=_INI_DOCUMENT_VARIABLE,
        help="Path to INI configuration file",
        default=None,
        nargs="?",
        metavar="INI_config_file",
    )

    # Default is an unset_t instance to avoid overwriting if in INI but not passed.
    default = UNSET
    options = []
    for s_name, section in specification.items():
        if section.__class__.is_controlled:
            if None in section:
                parameters = section[None]
            else:
                # Controlled parameters are skipped.
                continue
        else:
            parameters = section

        for p_name, parameter in parameters.items():
            option = f"{s_name}{_SECTION_PARAMETER_SEPARATOR}{p_name}"
            if option == _ADVANCED_MODE_OPTION:
                # Raising an exception is adapted here since execution has been launched
                # from command line.
                raise ValueError(
                    f"{option}: Command-line option for parameter is identical to "
                    f"advanced mode option. "
                    f"Please change parameter specification (section name and/or "
                    f"parameter name)."
                )
            if option in options:
                # This can happen in controlled sections whose alternatives share
                # equally named parameters.
                continue

            attribute = f"{s_name}{_SECTION_PARAMETER_SEPARATOR}{p_name}"

            if parameter.ppt.optional:
                if isinstance(parameter.default, str):
                    delimiter = '"'
                else:
                    delimiter = ""
                type_and_value = (
                    f"Type: {parameter.hint}. "
                    f"Default: [green]{delimiter}{parameter.default}{delimiter}[/]"
                )
            else:
                type_and_value = str(default)
            flattened = Flattened(type_and_value)
            definition = f"{parameter.ppt.short}. {flattened}"

            # Type could be TypeOfAnnotatedHint(cmd_line_type). However, to allow
            # passing any of the allowed types, deferring type validation to functional
            # config instantiation, this parameter is not passed.
            output.add_argument(
                f"--{option}",
                dest=attribute,
                help=definition,
                default=default,
                metavar=attribute,
            )
            options.append(option)

    output.add_argument(
        f"--{_ADVANCED_MODE_OPTION}",
        dest=_ADVANCED_MODE_VARIABLE,
        help="Toggle display of advanced sections and parameters",
        action="store_true",
    )

    return output


def CommandLineConfig(
    parser: argument_parser_t, /, *, arguments: h.Sequence[str] = None
) -> tuple[config_typed_h, bool, path_t | None]:
    """"""
    parsed, unknowns = parser.parse_known_args(args=arguments)
    parsed = vars(parsed)

    advanced_mode = parsed[_ADVANCED_MODE_VARIABLE]
    del parsed[_ADVANCED_MODE_VARIABLE]

    ini_path = parsed[_INI_DOCUMENT_VARIABLE]
    del parsed[_INI_DOCUMENT_VARIABLE]
    if ini_path is not None:
        try:
            ini_path = path_t(ini_path).resolve(strict=True)
        except (FileNotFoundError, RuntimeError):
            raise FileNotFoundError(f"Nonexistent or invalid path: {ini_path}")

    pattern = rgex.compile(
        r"--(\w+)" + _SECTION_PARAMETER_SEPARATOR + r"(\w+\.\w+)=(.+)", flags=rgex.ASCII
    )
    for unknown in unknowns:
        match = pattern.fullmatch(unknown)
        if match is None:
            # Raising an exception is adapted here since execution has been launched
            # from command line.
            raise ValueError(
                f"{unknown}: Invalid option syntax; Expected=--SECTION-PARAMETER=VALUE"
            )

        section, parameter, value = match.groups()
        parsed[f"{section}{_SECTION_PARAMETER_SEPARATOR}{parameter}"] = value

    raw_config = {}
    for sct_name, prm_name, value in _SectionParameterValueIterator(parsed):
        if sct_name in raw_config:
            raw_config[sct_name][prm_name] = value
        else:
            raw_config[sct_name] = {prm_name: value}

    return raw_config, advanced_mode, ini_path


def _SectionParameterValueIterator(
    arguments: parsed_arguments_h,
) -> h.Iterator[tuple[str, str, h.Any]]:
    """"""
    for prm_uid, value in arguments.items():
        # See CommandLineParser for why this can happen.
        if value is UNSET:
            continue

        section, parameter = prm_uid.split(_SECTION_PARAMETER_SEPARATOR)
        yield section, parameter, value


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
