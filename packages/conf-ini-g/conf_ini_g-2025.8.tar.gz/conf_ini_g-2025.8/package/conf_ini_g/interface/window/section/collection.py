"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2021
SEE COPYRIGHT NOTICE BELOW
"""

from babelwidget.api.backend import backend_t
from babelwidget.api.layout import scroll_container_p
from babelwidget.api.layout import tabs_h as tabs_wgt_h
from conf_ini_g.interface.window.section.main import (
    section_controlled_t,
    section_free_t,
)
from conf_ini_g.type.config import config_t


def SectionsAndCategories(
    config: config_t,
    category_selector: scroll_container_p | tabs_wgt_h | None,
    backend: backend_t,
    /,
) -> scroll_container_p | tabs_wgt_h:
    """"""
    categories = {}

    # --- Sections and categories
    controlled_pairs = []
    for name, functional in config.items():
        if functional.__class__.is_controlled:
            visual = section_controlled_t.New(name, functional, backend)
            if visual is not None:
                controlled_pairs.append((visual, functional.controller))
        else:
            visual = section_free_t.New(name, functional, backend)
        if visual is None:
            continue

        if (category := functional.ppt.category) not in categories:
            contents = backend.base_t()
            layout = backend.layout_v_t()
            contents.setLayout(layout)
            scroll_area = backend.scroll_container_t.NewForWidget(contents)
            categories[category] = (layout, scroll_area)

        layout = categories[category][0]
        layout.addWidget(visual.library_wgt)

    for visual, controller in controlled_pairs:
        value_wgt = controller[2].interface.value
        if hasattr(value_wgt, "SetFunction"):
            value_wgt.SetFunction(visual.subset_stack.setCurrentIndex)
        else:
            backend.ShowErrorMessage(
                f"{controller[0]}.{controller[1]}: "
                f'Controller has no "SetFunction" method; Disabling control.'
            )

    # --- Section dispatch into categories
    missing_category_selector = category_selector is None
    if categories.__len__() > 1:
        if missing_category_selector:
            category_selector = backend.tabs_t()
        for category, (_, scroll_area) in categories.items():
            category_selector.addTab(scroll_area, category)
    elif missing_category_selector:
        category = tuple(categories.keys())[0]
        category_selector = categories[category][1]

    return category_selector


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
