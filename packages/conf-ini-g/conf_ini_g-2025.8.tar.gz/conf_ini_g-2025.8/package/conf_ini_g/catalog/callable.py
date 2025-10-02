"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2021
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import inspect as nspt
import typing as h
from importlib import util as mprt
from pathlib import Path as pl_path_t

from babelwidget.api.backend import backend_t
from babelwidget.api.widget import base_h as library_wgt_h
from conf_ini_g.catalog.choices import choices_wgt_t
from conf_ini_g.catalog.path import path_wgt_t
from conf_ini_g.interface.window.parameter.value import value_wgt_a
from value_factory.api.catalog import callable_t, path_kind_e, path_purpose_e, path_t
from value_factory.api.type import hint_t


@d.dataclass(repr=False, eq=False)
class callable_wgt_t(value_wgt_a):
    library_wgt: library_wgt_h
    kind: h.Literal["class", "function"]
    default_choices: choices_wgt_t | None = d.field(init=False, default=None)
    path: path_wgt_t | None = d.field(init=False, default=None)
    choices: choices_wgt_t | None = d.field(init=False, default=None)

    @classmethod
    def New(cls, stripe: hint_t, backend: backend_t, /) -> h.Self:
        """"""
        if (annotation := stripe.FirstAnnotationWithType(callable_t)) is None:
            kind = "function"
            default_choices = None
            allow_external = True
        else:
            kind = annotation.kind
            default_choices = annotation.choices
            allow_external = annotation.allow_external

        assert (default_choices is not None) or allow_external

        if default_choices is None:
            default_choices_wgt = None
        else:
            default_choices_wgt = choices_wgt_t.New(default_choices, backend)

        # TODO: Check emitter and signal.
        output = cls(
            default_choices_wgt,
            "currentIndexChanged",
            backend,
            library_wgt=backend.base_t(),
            kind=kind,
        )
        output.default_choices = default_choices_wgt

        kind_wgt = backend.label_t(kind)

        layout = backend.layout_h_t()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(kind_wgt)
        if allow_external:
            hint = hint_t.New(
                path_t(kind=path_kind_e.document, purpose=path_purpose_e.input)
            )
            path_wgt = path_wgt_t.New(
                hint, backend, PostAssignmentFunction=output._UpdateChoices
            )
            choices_wgt = choices_wgt_t.New(None, backend)
            output.path = path_wgt
            output.choices = choices_wgt

            if default_choices_wgt is not None:
                layout.addWidget(default_choices_wgt.library_wgt)
            layout.addWidget(path_wgt.library_wgt)
            layout.addWidget(choices_wgt.library_wgt)
        else:
            layout.addWidget(default_choices_wgt.library_wgt)
        output.library_wgt.setLayout(layout)

        return output

    def _UpdateChoices(self, path: pl_path_t, /) -> None:
        """"""
        self.choices.library_wgt.clear()

        spec = mprt.spec_from_file_location(path.stem, path)
        module = spec.loader.load_module(spec.name)
        if self.kind == "class":
            condition = nspt.isclass
        else:
            condition = nspt.isfunction

        for name, _ in nspt.getmembers(module, condition):
            if not name.startswith("_"):
                self.choices.library_wgt.addItem(name)

    def SetFunction(self, function: h.Callable, /) -> None:
        """
        self.activated.connect(function): Responds only to GUI interaction, not
        programmatic change.
        """
        if self.default_choices is not None:
            self.default_choices.currentIndexChanged.connect(function)
        if self.choices is not None:
            self.choices.currentIndexChanged.connect(function)

    def Assign(self, value: str, _: h.Any, /) -> None:
        """"""
        if callable_t.SEPARATOR in value:
            path, choice = value.split(callable_t.SEPARATOR)
            self.path.Assign(pl_path_t(path), None)
            self.choices.Assign(choice, None)
        else:
            self.default_choices.Assign(value, None)

    def Text(self) -> str:
        """"""
        if self.path is None:
            return self.default_choices.Text()

        path = self.path.Text()
        if path.__len__() > 0:
            return f"{path}{callable_t.SEPARATOR}{self.choices.Text()}"

        if self.default_choices is None:
            return ""

        return self.default_choices.Text()


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
