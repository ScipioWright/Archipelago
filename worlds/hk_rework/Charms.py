from typing import List

vanilla_costs: List[int] = [1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 3, 1, 3, 1, 2, 2, 1, 2, 3, 2,
                            4, 2, 2, 2, 3, 1, 4, 2, 4, 1, 2, 3, 2, 4, 3, 5, 1, 3, 2, 2]

names: List[str] = [
    "Gathering Swarm",
    "Wayward Compass",
    "Grubsong",
    "Stalwart Shell",
    "Baldur Shell",
    "Fury of the Fallen",
    "Quick Focus",
    "Lifeblood Heart",
    "Lifeblood Core",
    "Defender's Crest",
    "Flukenest",
    "Thorns of Agony",
    "Mark of Pride",
    "Steady Body",
    "Heavy Blow",
    "Sharp Shadow",
    "Spore Shroom",
    "Longnail",
    "Shaman Stone",
    "Soul Catcher",
    "Soul Eater",
    "Glowing Womb",
    "Fragile Heart",
    "Fragile Greed",
    "Fragile Strength",
    "Nailmaster's Glory",
    "Joni's Blessing",
    "Shape of Unn",
    "Hiveblood",
    "Dream Wielder",
    "Dashmaster",
    "Quick Slash",
    "Spell Twister",
    "Deep Focus",
    "Grubberfly's Elegy",
    "Kingsoul",
    "Sprintmaster",
    "Dreamshield",
    "Weaversong",
    "Grimmchild"
]

charm_name_to_id = {"_".join(name.split(" ")): index for index, name in enumerate(names)}
                    # TODO >:(
