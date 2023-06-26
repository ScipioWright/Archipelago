# Locations are specific points that you would obtain an item at.
from enum import IntEnum
from typing import Dict, NamedTuple, Optional
from copy import deepcopy

from BaseClasses import Location


class NoitaLocation(Location):
    game: str = "Noita"


class LocationData(NamedTuple):
    id: int
    flag: int = 0
    ltype: Optional[str] = ""
    pw: bool = True


class LocationFlag(IntEnum):
    none = 0
    main_path = 1
    side_path = 2
    main_world = 3
    parallel_worlds = 4


# Mapping of items in each region.
# Only the first Hidden Chest and Pedestal are mapped here, the others are created in Regions.
# ltype key: "chest" = Hidden Chests, "pedestal" = Pedestals, "boss" = Boss, "orb" = Orb.
# pw is for locations that spawn in parallel worlds, for use in generating the parallel world location IDs
# 110000-110649
location_region_mapping: Dict[str, Dict[str, LocationData]] = {
    "Coal Pits Holy Mountain": {
        "Coal Pits Holy Mountain Shop Item 1":   LocationData(110000, LocationFlag.main_path, "shop"),
        "Coal Pits Holy Mountain Shop Item 2":   LocationData(110001, LocationFlag.main_path, "shop"),
        "Coal Pits Holy Mountain Shop Item 3":   LocationData(110002, LocationFlag.main_path, "shop"),
        "Coal Pits Holy Mountain Shop Item 4":   LocationData(110003, LocationFlag.main_path, "shop"),
        "Coal Pits Holy Mountain Shop Item 5":   LocationData(110004, LocationFlag.main_path, "shop"),
        "Coal Pits Holy Mountain Spell Refresh": LocationData(110005, LocationFlag.main_path, "shop"),
    },
    "Snowy Depths Holy Mountain": {
        "Snowy Depths Holy Mountain Shop Item 1":   LocationData(110006, LocationFlag.main_path, "shop"),
        "Snowy Depths Holy Mountain Shop Item 2":   LocationData(110007, LocationFlag.main_path, "shop"),
        "Snowy Depths Holy Mountain Shop Item 3":   LocationData(110008, LocationFlag.main_path, "shop"),
        "Snowy Depths Holy Mountain Shop Item 4":   LocationData(110009, LocationFlag.main_path, "shop"),
        "Snowy Depths Holy Mountain Shop Item 5":   LocationData(110010, LocationFlag.main_path, "shop"),
        "Snowy Depths Holy Mountain Spell Refresh": LocationData(110011, LocationFlag.main_path, "shop"),
    },
    "Hiisi Base Holy Mountain": {
        "Hiisi Base Holy Mountain Shop Item 1":   LocationData(110012, LocationFlag.main_path, "shop"),
        "Hiisi Base Holy Mountain Shop Item 2":   LocationData(110013, LocationFlag.main_path, "shop"),
        "Hiisi Base Holy Mountain Shop Item 3":   LocationData(110014, LocationFlag.main_path, "shop"),
        "Hiisi Base Holy Mountain Shop Item 4":   LocationData(110015, LocationFlag.main_path, "shop"),
        "Hiisi Base Holy Mountain Shop Item 5":   LocationData(110016, LocationFlag.main_path, "shop"),
        "Hiisi Base Holy Mountain Spell Refresh": LocationData(110017, LocationFlag.main_path, "shop"),
    },
    "Underground Jungle Holy Mountain": {
        "Underground Jungle Holy Mountain Shop Item 1":   LocationData(110018, LocationFlag.main_path, "shop"),
        "Underground Jungle Holy Mountain Shop Item 2":   LocationData(110019, LocationFlag.main_path, "shop"),
        "Underground Jungle Holy Mountain Shop Item 3":   LocationData(110020, LocationFlag.main_path, "shop"),
        "Underground Jungle Holy Mountain Shop Item 4":   LocationData(110021, LocationFlag.main_path, "shop"),
        "Underground Jungle Holy Mountain Shop Item 5":   LocationData(110022, LocationFlag.main_path, "shop"),
        "Underground Jungle Holy Mountain Spell Refresh": LocationData(110023, LocationFlag.main_path, "shop"),
    },
    "Vault Holy Mountain": {
        "Vault Holy Mountain Shop Item 1":   LocationData(110024, LocationFlag.main_path, "shop"),
        "Vault Holy Mountain Shop Item 2":   LocationData(110025, LocationFlag.main_path, "shop"),
        "Vault Holy Mountain Shop Item 3":   LocationData(110026, LocationFlag.main_path, "shop"),
        "Vault Holy Mountain Shop Item 4":   LocationData(110027, LocationFlag.main_path, "shop"),
        "Vault Holy Mountain Shop Item 5":   LocationData(110028, LocationFlag.main_path, "shop"),
        "Vault Holy Mountain Spell Refresh": LocationData(110029, LocationFlag.main_path, "shop"),
    },
    "Temple of the Art Holy Mountain": {
        "Temple of the Art Holy Mountain Shop Item 1":   LocationData(110030, LocationFlag.main_path, "shop"),
        "Temple of the Art Holy Mountain Shop Item 2":   LocationData(110031, LocationFlag.main_path, "shop"),
        "Temple of the Art Holy Mountain Shop Item 3":   LocationData(110032, LocationFlag.main_path, "shop"),
        "Temple of the Art Holy Mountain Shop Item 4":   LocationData(110033, LocationFlag.main_path, "shop"),
        "Temple of the Art Holy Mountain Shop Item 5":   LocationData(110034, LocationFlag.main_path, "shop"),
        "Temple of the Art Holy Mountain Spell Refresh": LocationData(110035, LocationFlag.main_path, "shop"),
    },
    "Laboratory Holy Mountain": {
        "Laboratory Holy Mountain Shop Item 1":   LocationData(110036, LocationFlag.main_path, "shop", pw=False),
        "Laboratory Holy Mountain Shop Item 2":   LocationData(110037, LocationFlag.main_path, "shop", pw=False),
        "Laboratory Holy Mountain Shop Item 3":   LocationData(110038, LocationFlag.main_path, "shop", pw=False),
        "Laboratory Holy Mountain Shop Item 4":   LocationData(110039, LocationFlag.main_path, "shop", pw=False),
        "Laboratory Holy Mountain Shop Item 5":   LocationData(110040, LocationFlag.main_path, "shop", pw=False),
        "Laboratory Holy Mountain Spell Refresh": LocationData(110041, LocationFlag.main_path, "shop", pw=False),
    },
    "Secret Shop": {
        "Secret Shop Item 1": LocationData(110042, LocationFlag.main_path, "shop", pw=False),
        "Secret Shop Item 2": LocationData(110043, LocationFlag.main_path, "shop", pw=False),
        "Secret Shop Item 3": LocationData(110044, LocationFlag.main_path, "shop", pw=False),
        "Secret Shop Item 4": LocationData(110045, LocationFlag.main_path, "shop", pw=False),
    },
    "Floating Island": {
        "Floating Island Orb": LocationData(110658, LocationFlag.main_path, "orb"),
    },
    "Pyramid": {
        "Kolmisilmän Koipi": LocationData(110649, LocationFlag.main_world, "boss", False),
        "Pyramid Orb":       LocationData(110659, LocationFlag.main_world, "orb"),
        "Sandcave Orb":      LocationData(110662, LocationFlag.main_world, "orb"),
    },
    "Overgrown Cavern": {
        "Overgrown Cavern Chest":    LocationData(110526, LocationFlag.main_world, "chest"),
        "Overgrown Cavern Pedestal": LocationData(110546, LocationFlag.main_world, "pedestal"),
    },
    "Lake": {
        "Syväolento": LocationData(110651, LocationFlag.main_world, "boss", False),
    },
    "Frozen Vault": {
        "Frozen Vault Orb":      LocationData(110660, LocationFlag.main_world, "orb"),
        "Frozen Vault Chest":    LocationData(110566, LocationFlag.main_world, "chest"),
        "Frozen Vault Pedestal": LocationData(110586, LocationFlag.main_world, "pedestal"),
    },
    "Mines": {
        "Mines Chest":    LocationData(110046, LocationFlag.main_path, "chest"),
        "Mines Pedestal": LocationData(110066, LocationFlag.main_path, "pedestal"),
    },
    # Collapsed Mines is a very small area, combining it with the Mines. Leaving this here in case we change our minds.
    # "Collapsed Mines": {
    #     "Collapsed Mines Chest":    LocationData(110086, LocationFlag.main_path, "chest"),
    #     "Collapsed Mines Pedestal": LocationData(110106, LocationFlag.main_path, "pedestal"),
    # },
    "Ancient Laboratory": {
        "Ylialkemisti": LocationData(110656, LocationFlag.side_path, "boss"),
    },
    "Abyss Orb Room": {
        "Sauvojen Tuntija": LocationData(110650, LocationFlag.side_path, "boss"),
        "Abyss Orb":        LocationData(110665, LocationFlag.main_path, "orb"),
    },
    "Below Lava Lake": {
        "Lava Lake Orb": LocationData(110661, LocationFlag.side_path, "orb", False),
    },
    "Coal Pits": {
        "Coal Pits Chest":    LocationData(110126, LocationFlag.main_path, "chest"),
        "Coal Pits Pedestal": LocationData(110146, LocationFlag.main_path, "pedestal"),
    },
    "Fungal Caverns": {
        "Fungal Caverns Chest":    LocationData(110166, LocationFlag.side_path, "chest"),
        "Fungal Caverns Pedestal": LocationData(110186, LocationFlag.side_path, "pedestal"),
    },
    "Snowy Depths": {
        "Snowy Depths Chest":    LocationData(110206, LocationFlag.main_path, "chest"),
        "Snowy Depths Pedestal": LocationData(110226, LocationFlag.main_path, "pedestal"),
    },
    "Magical Temple": {
        "Magical Temple Orb":  LocationData(110663, LocationFlag.side_path, "orb"),
    },
    "Hiisi Base": {
        "Hiisi Base Chest":    LocationData(110246, LocationFlag.main_path, "chest"),
        "Hiisi Base Pedestal": LocationData(110266, LocationFlag.main_path, "pedestal"),
    },
    "Underground Jungle": {
        "Suomuhauki":                  LocationData(110648, LocationFlag.main_path, "boss"),
        "Underground Jungle Chest":    LocationData(110286, LocationFlag.main_path, "chest"),
        "Underground Jungle Pedestal": LocationData(110306, LocationFlag.main_path, "pedestal"),
    },
    "Lukki Lair": {
        "Lukki Lair Orb":      LocationData(110664, LocationFlag.side_path, "orb"),
        "Lukki Lair Chest":    LocationData(110326, LocationFlag.side_path, "chest"),
        "Lukki Lair Pedestal": LocationData(110346, LocationFlag.side_path, "pedestal"),
    },
    "The Vault": {
        "The Vault Chest":    LocationData(110366, LocationFlag.main_path, "chest"),
        "The Vault Pedestal": LocationData(110386, LocationFlag.main_path, "pedestal"),
    },
    "Temple of the Art": {
        "Gate Guardian":              LocationData(110652, LocationFlag.main_path, "boss"),
        "Temple of the Art Chest":    LocationData(110406, LocationFlag.main_path, "chest"),
        "Temple of the Art Pedestal": LocationData(110426, LocationFlag.main_path, "pedestal"),
    },
    "The Tower": {
        "The Tower Chest":    LocationData(110606, LocationFlag.main_world, "chest"),
        "The Tower Pedestal": LocationData(110626, LocationFlag.main_world, "pedestal"),
    },
    "Wizards' Den": {
        "Mestarien Mestari":     LocationData(110655, LocationFlag.main_world, "boss"),
        "Wizards' Den Orb":      LocationData(110668, LocationFlag.main_world, "orb"),
        "Wizards' Den Chest":    LocationData(110446, LocationFlag.main_world, "chest"),
        "Wizards' Den Pedestal": LocationData(110466, LocationFlag.main_world, "pedestal"),
    },
    "Powerplant": {
        "Kolmisilmän silmä":    LocationData(110657, LocationFlag.main_world, "boss"),
        "Power Plant Chest":    LocationData(110486, LocationFlag.main_world, "chest"),
        "Power Plant Pedestal": LocationData(110506, LocationFlag.main_world, "pedestal"),
    },
    "Snow Chasm": {
        "Unohdettu":      LocationData(110653, LocationFlag.main_world, "boss"),
        "Snow Chasm Orb": LocationData(110667, LocationFlag.main_world, "orb"),
    },
    "Deep Underground": {
        "Limatoukka": LocationData(110647, LocationFlag.main_world, "boss", False),
    },
    "The Laboratory": {
        "Kolmisilmä": LocationData(110646, LocationFlag.main_path, "boss", False),
    },
    "Friend Cave": {
        "Toveri": LocationData(110654, LocationFlag.main_world, "boss"),
    },
    "The Work (Hell)": {
        "The Work (Hell) Orb": LocationData(110666, LocationFlag.main_world, "orb"),
    },
}


# Iterating the hidden chest and pedestal locations here to avoid clutter above
def generate_location_entries(locname: str, locinfo: LocationData) -> Dict[str, int]:
    if locinfo.ltype in ["chest", "pedestal"]:
        return {f"{locname} {i + 1}": locinfo.id + i for i in range(20)}
    return {locname: locinfo.id}


# TODO: PW locations get placed in their main-world regions
# Creates parallel world locations for locations not marked as non-existing
# def generate_pw_locations(locname: str, locinfo: LocationData) -> Dict[str, int]:
#     pw_locations = {}
#     if locinfo.pw:
#         if locinfo.ltype in ["chest", "pedestal"]:
#             for i in range(10):
#                 pw_locations[f"West {locname} {i + 1}"] = locinfo.id + i + 669
#                 pw_locations[f"East {locname} {i + 1}"] = locinfo.id + i + 669 * 2
#         else:
#             pw_locations[f"West {locname}"] = locinfo.id + 669
#             pw_locations[f"East {locname}"] = locinfo.id + 669 * 2
#
#     return pw_locations


full_location_region_mapping = deepcopy(location_region_mapping)
for region_name, location_group in location_region_mapping.items():
    wregion_name = f"West {region_name}"
    eregion_name = f"East {region_name}"
    wlocation_group = {}
    elocation_group = {}
    for location_name, location_data in location_group.items():
        if location_data.pw:
            wlocation_data = location_data._replace(id=location_data.id + 669, flag=LocationFlag.parallel_worlds)
            elocation_data = location_data._replace(id=location_data.id + 669 * 2, flag=LocationFlag.parallel_worlds)
            wlocation_group[f"West {location_name}"] = wlocation_data
            elocation_group[f"East {location_name}"] = elocation_data
    full_location_region_mapping[wregion_name] = wlocation_group
    full_location_region_mapping[eregion_name] = elocation_group


location_name_to_id: Dict[str, int] = {}
for location_group in full_location_region_mapping.values():
    for locname, locinfo in location_group.items():
        location_name_to_id.update(generate_location_entries(locname, locinfo))
        # location_name_to_id.update(generate_pw_locations(locname, locinfo))
