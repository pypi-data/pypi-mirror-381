"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2021
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h
from pathlib import Path as path_t

from babelwidget.api.backend import backend_t
from babelwidget.api.layout import layout_v_h
from babelwidget.api.widget import button_p as button_wgt_h
from babelwidget.api.widget import menu_p as menu_wgt_h
from conf_ini_g.catalog.path import path_wgt_t
from conf_ini_g.type.config import config_t
from value_factory.api.catalog import path_kind_e, path_purpose_e
from value_factory.api.catalog import path_t as path_annotation_t
from value_factory.api.type import hint_t


def TitleLayout(
    title: str | None,
    config: config_t,
    history: h.Sequence[str] | None,
    backend: backend_t,
    ini_path: path_t | None,
    UpdateWithNewINI: h.Callable,
    Close: h.Callable,
    /,
) -> tuple[layout_v_h, path_wgt_t, button_wgt_h, menu_wgt_h, button_wgt_h]:
    """"""
    if title is None:
        title = "Conf-INI-g"

    layout = backend.layout_h_t()
    inner_layout = backend.layout_v_t()

    title = (
        f'<h1 style="color: blue">{title}</h1>'
        f"<b><font face=monospace>SPEC:</font></b> {config.path}"
    )
    title_wgt = backend.label_t(title)
    title_wgt.setAlignment(backend.ALIGNED_LEFT)

    label_wgt = backend.label_t("<b><font face=monospace>INI: </font></b>")
    hint = hint_t.New(
        path_annotation_t(kind=path_kind_e.document, purpose=path_purpose_e.input)
    )
    ini_path_wgt = path_wgt_t.New(
        hint, backend, editable=False, PostAssignmentFunction=UpdateWithNewINI
    )
    ini_path_wgt.Assign(ini_path, None)
    history_button = backend.button_t("🕑")
    history_menu = backend.menu_t.NewWithFunction(UpdateWithNewINI)
    if history is None:
        history_button.setEnabled(False)
    else:
        for choice in history:
            history_menu.addAction(choice)
    history_button.setMenu(history_menu)
    #
    label_wgt.setSizePolicy(backend.SIZE_FIXED, backend.SIZE_FIXED)
    history_button.setSizePolicy(backend.SIZE_FIXED, backend.SIZE_MINIMUM)
    #
    path_layout = backend.layout_h_t()
    path_layout.addWidget(label_wgt)
    path_layout.addWidget(ini_path_wgt.library_wgt)
    path_layout.addWidget(history_button)

    inner_layout.addWidget(title_wgt)
    inner_layout.addLayout(path_layout)

    close_button = backend.button_t("CLOSE")
    close_button.SetFunction(Close)
    close_button.setSizePolicy(backend.SIZE_FIXED, backend.SIZE_MINIMUM)

    layout.addLayout(inner_layout)
    layout.addWidget(close_button)

    return layout, ini_path_wgt, history_button, history_menu, close_button


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
