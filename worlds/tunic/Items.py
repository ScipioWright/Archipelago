from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class TunicItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


item_table: Dict[str, TunicItemData] = {
    "Firecracker x2": TunicItemData(ItemClassification.filler, 3, 0, "bombs"),
    "Firecracker x3": TunicItemData(ItemClassification.filler, 3, 1, "bombs"),
    "Firecracker x4": TunicItemData(ItemClassification.filler, 3, 2, "bombs"),
    "Firecracker x5": TunicItemData(ItemClassification.filler, 1, 3, "bombs"),
    "Firecracker x6": TunicItemData(ItemClassification.filler, 2, 4, "bombs"),
    "Fire Bomb x2": TunicItemData(ItemClassification.filler, 2, 5, "bombs"),
    "Fire Bomb x3": TunicItemData(ItemClassification.filler, 1, 6, "bombs"),
    "Ice Bomb x2": TunicItemData(ItemClassification.filler, 2, 7, "bombs"),
    "Ice Bomb x3": TunicItemData(ItemClassification.filler, 2, 8, "bombs"),
    "Ice Bomb x5": TunicItemData(ItemClassification.filler, 1, 9, "bombs"),
    "Lure": TunicItemData(ItemClassification.filler, 4, 10, "consumables"),
    "Lure x2": TunicItemData(ItemClassification.filler, 1, 11, "consumables"),
    "Pepper x2": TunicItemData(ItemClassification.filler, 4, 12, "consumables"),
    "Ivy x3": TunicItemData(ItemClassification.filler, 2, 13, "consumables"),
    "Effigy": TunicItemData(ItemClassification.useful, 12, 14, "money"),
    "HP Berry": TunicItemData(ItemClassification.filler, 2, 15, "consumables"),
    "HP Berry x2": TunicItemData(ItemClassification.filler, 4, 16, "consumables"),
    "HP Berry x3": TunicItemData(ItemClassification.filler, 2, 17, "consumables"),
    "MP Berry": TunicItemData(ItemClassification.filler, 4, 18, "consumables"),
    "MP Berry x2": TunicItemData(ItemClassification.filler, 2, 19, "consumables"),
    "MP Berry x3": TunicItemData(ItemClassification.filler, 7, 20, "consumables"),
    "Fairy": TunicItemData(ItemClassification.progression, 20, 21),
    "Stick": TunicItemData(ItemClassification.progression, 1, 22, "weapons"),
    "Sword": TunicItemData(ItemClassification.progression, 3, 23, "weapons"),
    "Sword Upgrade": TunicItemData(ItemClassification.progression, 4, 24, "weapons"),
    "Magic Wand": TunicItemData(ItemClassification.progression, 1, 25, "weapons"),
    "Magic Dagger": TunicItemData(ItemClassification.progression, 1, 26),
    "Magic Orb": TunicItemData(ItemClassification.progression, 1, 27),
    "Hero's Laurels": TunicItemData(ItemClassification.progression, 1, 28),
    "Lantern": TunicItemData(ItemClassification.progression, 1, 29),
    "Shotgun": TunicItemData(ItemClassification.useful, 1, 30, "weapons"),
    "Shield": TunicItemData(ItemClassification.useful, 1, 31),
    "Dath Stone": TunicItemData(ItemClassification.useful, 1, 32),
    "Hourglass": TunicItemData(ItemClassification.useful, 1, 33),
    "Old House Key": TunicItemData(ItemClassification.progression, 1, 34, "keys"),
    "Key": TunicItemData(ItemClassification.progression, 2, 35, "keys"),
    "Fortress Vault Key": TunicItemData(ItemClassification.progression, 1, 36, "keys"),
    "Flask Shard": TunicItemData(ItemClassification.useful, 12, 37, "potions"),
    "Potion Flask": TunicItemData(ItemClassification.useful, 5, 38, "potions"),
    "Golden Coin": TunicItemData(ItemClassification.progression, 17, 39),
    "Card Slot": TunicItemData(ItemClassification.useful, 4, 40),
    "Red Hexagon": TunicItemData(ItemClassification.progression_skip_balancing, 1, 41, "hexagons"),
    "Green Hexagon": TunicItemData(ItemClassification.progression_skip_balancing, 1, 42, "hexagons"),
    "Blue Hexagon": TunicItemData(ItemClassification.progression_skip_balancing, 1, 43, "hexagons"),
    "Gold Hexagon": TunicItemData(ItemClassification.progression_skip_balancing, 30, 44, "hexagons"),
    "ATT Offering": TunicItemData(ItemClassification.useful, 4, 45, "offerings"),
    "DEF Offering": TunicItemData(ItemClassification.useful, 4, 46, "offerings"),
    "Potion Offering": TunicItemData(ItemClassification.useful, 3, 47, "offerings"),
    "HP Offering": TunicItemData(ItemClassification.useful, 6, 48, "offerings"),
    "MP Offering": TunicItemData(ItemClassification.useful, 3, 49, "offerings"),
    "SP Offering": TunicItemData(ItemClassification.useful, 2, 50, "offerings"),
    "Hero Relic - ATT": TunicItemData(ItemClassification.useful, 1, 51, "hero relics"),
    "Hero Relic - DEF": TunicItemData(ItemClassification.useful, 1, 52, "hero relics"),
    "Hero Relic - HP": TunicItemData(ItemClassification.useful, 1, 53, "hero relics"),
    "Hero Relic - MP": TunicItemData(ItemClassification.useful, 1, 54, "hero relics"),
    "Hero Relic - POTION": TunicItemData(ItemClassification.useful, 1, 55, "hero relics"),
    "Hero Relic - SP": TunicItemData(ItemClassification.useful, 1, 56, "hero relics"),
    "Orange Peril Ring": TunicItemData(ItemClassification.useful, 1, 57, "cards"),
    "Tincture": TunicItemData(ItemClassification.useful, 1, 58, "cards"),
    "Scavenger Mask": TunicItemData(ItemClassification.progression, 1, 59, "cards"),
    "Cyan Peril Ring": TunicItemData(ItemClassification.useful, 1, 60, "cards"),
    "Bracer": TunicItemData(ItemClassification.useful, 1, 61, "cards"),
    "Dagger Strap": TunicItemData(ItemClassification.useful, 1, 62, "cards"),
    "Inverted Ash": TunicItemData(ItemClassification.useful, 1, 63, "cards"),
    "Lucky Cup": TunicItemData(ItemClassification.useful, 1, 64, "cards"),
    "Magic Echo": TunicItemData(ItemClassification.useful, 1, 65, "cards"),
    "Anklet": TunicItemData(ItemClassification.useful, 1, 66, "cards"),
    "Muffling Bell": TunicItemData(ItemClassification.useful, 1, 67, "cards"),
    "Glass Cannon": TunicItemData(ItemClassification.useful, 1, 68, "cards"),
    "Perfume": TunicItemData(ItemClassification.useful, 1, 69, "cards"),
    "Louder Echo": TunicItemData(ItemClassification.useful, 1, 70, "cards"),
    "Aura's Gem": TunicItemData(ItemClassification.useful, 1, 71, "cards"),
    "Bone Card": TunicItemData(ItemClassification.useful, 1, 72, "cards"),
    "Mr Mayor": TunicItemData(ItemClassification.useful, 1, 73, "golden treasures"),
    "Secret Legend": TunicItemData(ItemClassification.useful, 1, 74, "golden treasures"),
    "Sacred Geometry": TunicItemData(ItemClassification.useful, 1, 75, "golden treasures"),
    "Vintage": TunicItemData(ItemClassification.useful, 1, 76, "golden treasures"),
    "Just Some Pals": TunicItemData(ItemClassification.useful, 1, 77, "golden treasures"),
    "Regal Weasel": TunicItemData(ItemClassification.useful, 1, 78, "golden treasures"),
    "Spring Falls": TunicItemData(ItemClassification.useful, 1, 79, "golden treasures"),
    "Power Up": TunicItemData(ItemClassification.useful, 1, 80, "golden treasures"),
    "Back To Work": TunicItemData(ItemClassification.useful, 1, 81, "golden treasures"),
    "Phonomath": TunicItemData(ItemClassification.useful, 1, 82, "golden treasures"),
    "Dusty": TunicItemData(ItemClassification.useful, 1, 83, "golden treasures"),
    "Forever Friend": TunicItemData(ItemClassification.useful, 1, 84, "golden treasures"),
    "Money x1": TunicItemData(ItemClassification.filler, 3, 85, "money"),
    "Money x10": TunicItemData(ItemClassification.filler, 1, 86, "money"),
    "Money x15": TunicItemData(ItemClassification.filler, 10, 87, "money"),
    "Money x16": TunicItemData(ItemClassification.filler, 1, 88, "money"),
    "Money x20": TunicItemData(ItemClassification.filler, 17, 89, "money"),
    "Money x25": TunicItemData(ItemClassification.filler, 14, 90, "money"),
    "Money x30": TunicItemData(ItemClassification.filler, 4, 91, "money"),
    "Money x32": TunicItemData(ItemClassification.filler, 4, 92, "money"),
    "Money x40": TunicItemData(ItemClassification.filler, 3, 93, "money"),
    "Money x48": TunicItemData(ItemClassification.filler, 1, 94, "money"),
    "Money x50": TunicItemData(ItemClassification.filler, 7, 95, "money"),
    "Money x64": TunicItemData(ItemClassification.filler, 1, 96, "money"),
    "Money x100": TunicItemData(ItemClassification.useful, 5, 97, "money"),
    "Money x128": TunicItemData(ItemClassification.useful, 3, 98, "money"),
    "Money x200": TunicItemData(ItemClassification.useful, 1, 99, "money"),
    "Money x255": TunicItemData(ItemClassification.useful, 1, 100, "money"),
    "Pages 0-1": TunicItemData(ItemClassification.progression_skip_balancing, 1, 101, "pages"),
    "Pages 2-3": TunicItemData(ItemClassification.progression_skip_balancing, 1, 102, "pages"),
    "Pages 4-5": TunicItemData(ItemClassification.progression_skip_balancing, 1, 103, "pages"),
    "Pages 6-7": TunicItemData(ItemClassification.progression_skip_balancing, 1, 104, "pages"),
    "Pages 8-9": TunicItemData(ItemClassification.progression_skip_balancing, 1, 105, "pages"),
    "Pages 10-11": TunicItemData(ItemClassification.progression_skip_balancing, 1, 106, "pages"),
    "Pages 12-13": TunicItemData(ItemClassification.progression_skip_balancing, 1, 107, "pages"),
    "Pages 14-15": TunicItemData(ItemClassification.progression_skip_balancing, 1, 108, "pages"),
    "Pages 16-17": TunicItemData(ItemClassification.progression_skip_balancing, 1, 109, "pages"),
    "Pages 18-19": TunicItemData(ItemClassification.progression_skip_balancing, 1, 110, "pages"),
    "Pages 20-21": TunicItemData(ItemClassification.progression_skip_balancing, 1, 111, "pages"),
    "Pages 22-23": TunicItemData(ItemClassification.progression_skip_balancing, 1, 112, "pages"),
    "Pages 24-25 (Prayer)": TunicItemData(ItemClassification.progression, 1, 113, "pages"),
    "Pages 26-27": TunicItemData(ItemClassification.progression_skip_balancing, 1, 114, "pages"),
    "Pages 28-29": TunicItemData(ItemClassification.progression_skip_balancing, 1, 115, "pages"),
    "Pages 30-31": TunicItemData(ItemClassification.progression_skip_balancing, 1, 116, "pages"),
    "Pages 32-33": TunicItemData(ItemClassification.progression_skip_balancing, 1, 117, "pages"),
    "Pages 34-35": TunicItemData(ItemClassification.progression_skip_balancing, 1, 118, "pages"),
    "Pages 36-37": TunicItemData(ItemClassification.progression_skip_balancing, 1, 119, "pages"),
    "Pages 38-39": TunicItemData(ItemClassification.progression_skip_balancing, 1, 120, "pages"),
    "Pages 40-41": TunicItemData(ItemClassification.progression_skip_balancing, 1, 121, "pages"),
    "Pages 42-43 (Holy Cross)": TunicItemData(ItemClassification.progression, 1, 122, "pages"),
    "Pages 44-45": TunicItemData(ItemClassification.progression_skip_balancing, 1, 123, "pages"),
    "Pages 46-47": TunicItemData(ItemClassification.progression_skip_balancing, 1, 124, "pages"),
    "Pages 48-49": TunicItemData(ItemClassification.progression_skip_balancing, 1, 125, "pages"),
    "Pages 50-51": TunicItemData(ItemClassification.progression_skip_balancing, 1, 126, "pages"),
    "Pages 52-53 (Ice Rod)": TunicItemData(ItemClassification.progression, 1, 127, "pages"),
    "Pages 54-55": TunicItemData(ItemClassification.progression_skip_balancing, 1, 128, "pages"),
}


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
}

# extra groups for the purpose of aliasing items
extra_groups: Dict[str, Set[str]] = {
    "laurels": {"Hero's Laurels"},
    "holy cross": {"Pages 42-43 (Holy Cross)"},
    "prayer": {"Pages 24-25 (Prayer)"},
    "ice rod": {"Pages 52-53 (Ice Rod)"},
    "melee weapons": {"Stick", "Sword", "Sword Upgrade"}
}

item_name_groups.update(extra_groups)
