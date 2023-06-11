from BaseClasses import MultiWorld
from .Options import BossesAsChecks, OrbsAsChecks, VictoryCondition
from random import shuffle

# heavily inspired by and stolen from Vi's implementation for The Witness


def get_always_hint_locations(multiworld: MultiWorld, player: int):
    always_locations = []
    # if Kolmi is a check andd you're going for orbs, make them a priority hint
    if multiworld.bosses_as_checks[player].value >= BossesAsChecks.option_main_path and \
            multiworld.victory_condition[player].value >= VictoryCondition.option_pure_ending:
        always_locations.append("Kolmisilmä")
    # bosses that are more difficult to access
    if multiworld.bosses_as_checks[player].value >= BossesAsChecks.option_all_bosses:
        always_locations.extend(["Syväolento", "Limatoukka"])

    return always_locations


def get_always_hint_items(multiworld: MultiWorld, player: int):
    always_items = [
        "Fire Immunity Perk",
        "Explosion Immunity Perk",
        "Tinker with Wands Everywhere Perk",
        "All-Seeing Eye Perk",
    ]

    # if Toveri is a check, make the Map perk a priority hint
    if multiworld.bosses_as_checks[player].value >= BossesAsChecks.option_all_bosses:
        always_items.append("Spatial Awareness Perk")

    return always_items


# todo: check if we actually need these if statements, or if the prog_items and loc_in things just take care of it
def get_useful_hint_locations(multiworld: MultiWorld, player: int):
    # useful locations are ones that would be nice to have
    useful_locations = []

    if multiworld.orbs_as_checks[player].value >= OrbsAsChecks.option_main_world:
        useful_locations.extend([
            "Snow Chasm Orb",
            "The Work (Hell) Orb",
            "Frozen Vault Orb",
            "Sandcave Orb",
            "Wizards' Den Orb"
        ])

    if multiworld.orbs_as_checks[player].value >= OrbsAsChecks.option_side_path:
        useful_locations.extend([
            "Lukki Lair Orb",
            "Magical Temple Orb"
        ])

    if multiworld.bosses_as_checks[player].value >= BossesAsChecks.option_all_bosses:
        useful_locations.extend([
            "Unohdettu",
            "Mestarien Mestari",
            "Kolmisilmän silmä",
            "Toveri",
            "Kolmisilmän Koipi"
        ])

    if multiworld.bosses_as_checks[player].value >= BossesAsChecks.option_side_path:
        useful_locations.extend([
            "Ylialkemisti",
            "Sauvojen Tuntija"
        ])

    return useful_locations


def get_useful_hint_items():
    # useful items are ones that would be nice to have
    return [
        "Toxic Immunity Perk",
        "Melee Immunity Perk",
        "Electricity Immunity Perk",
    ]


joke_hints = [
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke 5",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
    "joke hint sample",
    "joke hint sample 2",
    "joke 3",
    "jok3 4",
]


def make_hint_from_item(multiworld: MultiWorld, player: int, item: str):
    location_obj = multiworld.find_item(item, player).item.location
    location_name = location_obj.name
    if location_obj.player != player:
        location_name += " in " + multiworld.get_player_name(location_obj.player) + "'s world"
    else:
        location_name += " of your world"

    return location_name, item


def make_hint_from_location(multiworld: MultiWorld, player: int, location: str):
    # location_obj = multiworld.get_location(location, player)
    item_obj = multiworld.get_location(location, player).item
    item_name = item_obj.name
    if item_obj.player != player:
        item_name = multiworld.get_player_name(item_obj.player) + "'s " + item_name
    else:
        item_name = "your " + item_name

    return location, item_name


def get_loc_in_this_world(multiworld: MultiWorld, player: int):
    loc_in_this_world = {
        location.name for location in multiworld.get_locations()
        if location.player == player and location.address
    }
    return loc_in_this_world


def get_prog_items_in_this_world(multiworld: MultiWorld, player: int):
    prog_items_in_this_world = {
        item.name for item in multiworld.get_items()
        if item.player == player and item.code and item.advancement
    }
    return prog_items_in_this_world


def make_hint_pairs(multiworld: MultiWorld, player: int, hint_locations: list, hint_items: list):
    location_hints = [
        location for location in hint_locations
        if location in get_loc_in_this_world(multiworld, player)
    ]
    item_hints = [
        item for item in hint_items
        if item in get_prog_items_in_this_world(multiworld, player)
    ]

    hint_pairs = dict()

    for location in location_hints:
        hint_pair = make_hint_from_location(multiworld, player, location)
        hint_pairs[hint_pair[0]] = (hint_pair[1], False)

    for item in item_hints:
        hint_pair = make_hint_from_item(multiworld, player, item)
        hint_pairs[hint_pair[0]] = (hint_pair[1], True)

    return hint_pairs


def make_hint_text(item: tuple, location: str):
    if item[1]:
        return f"Your {item[0]} is being held by the {location}."
    else:
        return f"The {location} of your world holds {item[0]}."


def make_hints(multiworld: MultiWorld, player: int, hint_amount: int):
    hints = list()

    loc_in_this_world = get_loc_in_this_world(multiworld, player)

    always_pairs = make_hint_pairs(multiworld, player, get_always_hint_locations(multiworld, player),
                                   get_always_hint_items(multiworld, player))
    useful_pairs = make_hint_pairs(multiworld, player, get_useful_hint_locations(multiworld, player),
                                   get_useful_hint_items())

    for loc, item in always_pairs.items():
        hints.append(make_hint_text(item, loc))

    multiworld.per_slot_randoms[player].shuffle(hints)

    locations_in_this_world = sorted(list(loc_in_this_world))

    multiworld.per_slot_randoms[player].shuffle(locations_in_this_world)

    if hint_amount < 13:
        # if you have less than 13 hints set, add some joke hints and then up the hint_amount so the while works
        hints.extend(generate_joke_hints(multiworld, player, 13 - hint_amount))
        hint_amount = 13

    while len(hints) < hint_amount:
        if len(hints) == 13:
            # we want the unforged tablets to have the good hints, but not necessarily starting with our items
            shuffle(hints)
        if useful_pairs:
            loc = multiworld.per_slot_randoms[player].choice(list(useful_pairs.keys()))
            item = useful_pairs[loc]
            del useful_pairs[loc]

            hints.append(make_hint_text(item, loc))
            continue

        if len(locations_in_this_world) == 0:
            hints.extend(generate_joke_hints(multiworld, player, hint_amount - len(hints)))
            continue

        location = locations_in_this_world.pop()
        item = multiworld.get_location(location, player).item
        if item.advancement and item.player != player:
            hint = make_hint_from_location(multiworld, player, location)
            hints.append(f"Your {hint[0]} holds {hint[1]}.")

    if hint_amount == 13:
        shuffle(hints)

    hints.extend(generate_joke_hints(multiworld, player, 26 - hint_amount))
    for item in hints:
        print(item)
    numbered_hints = dict(zip(range(len(hints)), hints))

    return numbered_hints


def generate_joke_hints(multiworld: MultiWorld, player: int, amount: int):
    return [x for x in multiworld.per_slot_randoms[player].sample(joke_hints, amount)]


def create_all_hints(multiworld: MultiWorld, player: int):
    hint_amount = multiworld.hint_amount[player].value

    if hint_amount != 0:
        generated_hints = make_hints(multiworld, player, hint_amount)
        return generated_hints
