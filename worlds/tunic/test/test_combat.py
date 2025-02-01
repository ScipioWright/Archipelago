from BaseClasses import ItemClassification
from collections import Counter

from . import TunicTestBase
from .. import options
from ..combat_logic import has_combat_reqs, check_combat_reqs, area_data
from ..items import item_table


class TestCombat(TunicTestBase):
    options = {options.CombatLogic.internal_name: options.CombatLogic.option_on}

    combat_items = Counter()
    # just load all progression in, Vi said it was fine lol
    for item, data in item_table.items():
        ic = data.combat_ic or data.classification
        if ItemClassification.progression in ic:
            combat_items[item] = data.quantity_in_item_pool




