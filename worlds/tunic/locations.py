from typing import Dict, NamedTuple, Set
from itertools import groupby


class TunicLocationData(NamedTuple):
    region: str
    location_group: str = "region"


location_base_id = 509342400

location_table: Dict[str, TunicLocationData] = {
    "Bottom of the Well - [Powered Secret Room] Chest": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Entryway] Chest": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Third Room] Beneath Platform Chest": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Third Room] Tentacle Chest": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Entryway] Obscured Behind Waterfall": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Save Room] Upper Floor Chest 1": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Save Room] Upper Floor Chest 2": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Second Room] Underwater Chest": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Back Corridor] Right Secret": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Back Corridor] Left Secret": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Second Room] Obscured Behind Waterfall": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Side Room] Chest By Pots": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Side Room] Chest By Phrends": TunicLocationData("Bottom of the Well"),
    "Bottom of the Well - [Second Room] Page": TunicLocationData("Bottom of the Well"),
    "Dark Tomb Checkpoint - [Passage To Dark Tomb] Page Pickup": TunicLocationData("Bottom of the Well"),
    "Cathedral - [1F] Guarded By Lasers": TunicLocationData("Cathedral"),
    "Cathedral - [1F] Near Spikes": TunicLocationData("Cathedral"),
    "Cathedral - [2F] Bird Room": TunicLocationData("Cathedral"),
    "Cathedral - [2F] Entryway Upper Walkway": TunicLocationData("Cathedral"),
    "Cathedral - [1F] Library": TunicLocationData("Cathedral"),
    "Cathedral - [2F] Library": TunicLocationData("Cathedral"),
    "Cathedral - [2F] Guarded By Lasers": TunicLocationData("Cathedral"),
    "Cathedral - [2F] Bird Room Secret": TunicLocationData("Cathedral"),
    "Cathedral - [1F] Library Secret": TunicLocationData("Cathedral"),
    "Dark Tomb - Spike Maze Near Exit": TunicLocationData("Dark Tomb"),
    "Dark Tomb - 2nd Laser Room": TunicLocationData("Dark Tomb"),
    "Dark Tomb - 1st Laser Room": TunicLocationData("Dark Tomb"),
    "Dark Tomb - Spike Maze Upper Walkway": TunicLocationData("Dark Tomb"),
    "Dark Tomb - Skulls Chest": TunicLocationData("Dark Tomb"),
    "Dark Tomb - Spike Maze Near Stairs": TunicLocationData("Dark Tomb"),
    "Dark Tomb - 1st Laser Room Obscured": TunicLocationData("Dark Tomb"),
    "Guardhouse 2 - Upper Floor": TunicLocationData("East Forest"),
    "Guardhouse 2 - Bottom Floor Secret": TunicLocationData("East Forest"),
    "Guardhouse 1 - Upper Floor Obscured": TunicLocationData("East Forest"),
    "Guardhouse 1 - Upper Floor": TunicLocationData("East Forest"),
    "East Forest - Dancing Fox Spirit Holy Cross": TunicLocationData("East Forest", "holy cross"),
    "East Forest - Golden Obelisk Holy Cross": TunicLocationData("East Forest", "holy cross"),
    "East Forest - Ice Rod Grapple Chest": TunicLocationData("East Forest"),
    "East Forest - Above Save Point": TunicLocationData("East Forest"),
    "East Forest - Above Save Point Obscured": TunicLocationData("East Forest"),
    "East Forest - From Guardhouse 1 Chest": TunicLocationData("East Forest"),
    "East Forest - Near Save Point": TunicLocationData("East Forest"),
    "East Forest - Beneath Spider Chest": TunicLocationData("East Forest"),
    "East Forest - Near Telescope": TunicLocationData("East Forest"),
    "East Forest - Spider Chest": TunicLocationData("East Forest"),
    "East Forest - Lower Dash Chest": TunicLocationData("East Forest"),
    "East Forest - Lower Grapple Chest": TunicLocationData("East Forest"),
    "East Forest - Bombable Wall": TunicLocationData("East Forest"),
    "East Forest - Page On Teleporter": TunicLocationData("East Forest"),
    "Forest Belltower - Near Save Point": TunicLocationData("East Forest"),
    "Forest Belltower - After Guard Captain": TunicLocationData("East Forest"),
    "Forest Belltower - Obscured Near Bell Top Floor": TunicLocationData("East Forest"),
    "Forest Belltower - Obscured Beneath Bell Bottom Floor": TunicLocationData("East Forest"),
    "Forest Belltower - Page Pickup": TunicLocationData("East Forest"),
    "Forest Grave Path - Holy Cross Code by Grave": TunicLocationData("East Forest", "holy cross"),
    "Forest Grave Path - Above Gate": TunicLocationData("East Forest"),
    "Forest Grave Path - Obscured Chest": TunicLocationData("East Forest"),
    "Forest Grave Path - Upper Walkway": TunicLocationData("East Forest"),
    "Forest Grave Path - Sword Pickup": TunicLocationData("East Forest"),
    "Hero's Grave - Tooth Relic": TunicLocationData("East Forest"),
    "Fortress Courtyard - From East Belltower": TunicLocationData("East Forest"),
    "Fortress Leaf Piles - Secret Chest": TunicLocationData("Eastern Vault Fortress"),
    "Fortress Arena - Hexagon Red": TunicLocationData("Eastern Vault Fortress"),
    "Fortress Arena - Siege Engine/Vault Key Pickup": TunicLocationData("Eastern Vault Fortress"),
    "Fortress East Shortcut - Chest Near Slimes": TunicLocationData("Eastern Vault Fortress"),
    "Eastern Vault Fortress - [West Wing] Candles Holy Cross": TunicLocationData("Eastern Vault Fortress", "holy cross"),
    "Eastern Vault Fortress - [West Wing] Dark Room Chest 1": TunicLocationData("Eastern Vault Fortress"),
    "Eastern Vault Fortress - [West Wing] Dark Room Chest 2": TunicLocationData("Eastern Vault Fortress"),
    "Eastern Vault Fortress - [East Wing] Bombable Wall": TunicLocationData("Eastern Vault Fortress"),
    "Eastern Vault Fortress - [West Wing] Page Pickup": TunicLocationData("Eastern Vault Fortress"),
    "Fortress Grave Path - Upper Walkway": TunicLocationData("Eastern Vault Fortress"),
    "Fortress Grave Path - Chest Right of Grave": TunicLocationData("Eastern Vault Fortress"),
    "Fortress Grave Path - Obscured Chest Left of Grave": TunicLocationData("Eastern Vault Fortress"),
    "Hero's Grave - Flowers Relic": TunicLocationData("Eastern Vault Fortress"),
    "Beneath the Fortress - Bridge": TunicLocationData("Beneath the Vault"),
    "Beneath the Fortress - Cell Chest 1": TunicLocationData("Beneath the Vault"),
    "Beneath the Fortress - Obscured Behind Waterfall": TunicLocationData("Beneath the Vault"),
    "Beneath the Fortress - Back Room Chest": TunicLocationData("Beneath the Vault"),
    "Beneath the Fortress - Cell Chest 2": TunicLocationData("Beneath the Vault"),
    "Frog's Domain - Near Vault": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Slorm Room": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Escape Chest": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Grapple Above Hot Tub": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Above Vault": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Main Room Top Floor": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Main Room Bottom Floor": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Side Room Secret Passage": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Side Room Chest": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Side Room Grapple Secret": TunicLocationData("Frog's Domain"),
    "Frog's Domain - Magic Orb Pickup": TunicLocationData("Frog's Domain"),
    "Librarian - Hexagon Green": TunicLocationData("Library"),
    "Library Hall - Holy Cross Chest": TunicLocationData("Library", "holy cross"),
    "Library Lab - Chest By Shrine 2": TunicLocationData("Library"),
    "Library Lab - Chest By Shrine 1": TunicLocationData("Library"),
    "Library Lab - Chest By Shrine 3": TunicLocationData("Library"),
    "Library Lab - Behind Chalkboard by Fuse": TunicLocationData("Library"),
    "Library Lab - Page 3": TunicLocationData("Library"),
    "Library Lab - Page 1": TunicLocationData("Library"),
    "Library Lab - Page 2": TunicLocationData("Library"),
    "Hero's Grave - Mushroom Relic": TunicLocationData("Library"),
    "Lower Mountain - Page Before Door": TunicLocationData("Overworld"),
    "Changing Room - Normal Chest": TunicLocationData("Overworld"),
    "Fortress Courtyard - Chest Near Cave": TunicLocationData("Overworld"),
    "Fortress Courtyard - Near Fuse": TunicLocationData("Overworld"),
    "Fortress Courtyard - Below Walkway": TunicLocationData("Overworld"),
    "Fortress Courtyard - Page Near Cave": TunicLocationData("Overworld"),
    "West Furnace - Lantern Pickup": TunicLocationData("Overworld"),
    "Maze Cave - Maze Room Chest": TunicLocationData("Overworld"),
    "Old House - Normal Chest": TunicLocationData("Overworld"),
    "Old House - Shield Pickup": TunicLocationData("Overworld"),
    "Overworld - [West] Obscured Behind Windmill": TunicLocationData("Overworld"),
    "Overworld - [South] Beach Chest": TunicLocationData("Overworld"),
    "Overworld - [West] Obscured Near Well": TunicLocationData("Overworld"),
    "Overworld - [Central] Bombable Wall": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Chest Near Turret": TunicLocationData("Overworld"),
    "Overworld - [East] Chest Near Pots": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Chest Near Golden Obelisk": TunicLocationData("Overworld"),
    "Overworld - [Southwest] South Chest Near Guard": TunicLocationData("Overworld"),
    "Overworld - [Southwest] West Beach Guarded By Turret": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Chest Guarded By Turret": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Shadowy Corner Chest": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Obscured In Tunnel To Beach": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Grapple Chest Over Walkway": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Chest Beneath Quarry Gate": TunicLocationData("Overworld"),
    "Overworld - [Southeast] Chest Near Swamp": TunicLocationData("Overworld"),
    "Overworld - [Southwest] From West Garden": TunicLocationData("Overworld"),
    "Overworld - [East] Grapple Chest": TunicLocationData("Overworld"),
    "Overworld - [Southwest] West Beach Guarded By Turret 2": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Beach Chest Near Flowers": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Bombable Wall Near Fountain": TunicLocationData("Overworld"),
    "Overworld - [West] Chest After Bell": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Tunnel Guarded By Turret": TunicLocationData("Overworld"),
    "Overworld - [East] Between Ladders Near Ruined Passage": TunicLocationData("Overworld"),
    "Overworld - [Northeast] Chest Above Patrol Cave": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Beach Chest Beneath Guard": TunicLocationData("Overworld"),
    "Overworld - [Central] Chest Across From Well": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Chest Near Quarry Gate": TunicLocationData("Overworld"),
    "Overworld - [East] Chest In Trees": TunicLocationData("Overworld"),
    "Overworld - [West] Chest Behind Moss Wall": TunicLocationData("Overworld"),
    "Overworld - [South] Beach Page": TunicLocationData("Overworld"),
    "Overworld - [Southeast] Page on Pillar by Swamp": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Key Pickup": TunicLocationData("Overworld"),
    "Overworld - [West] Key Pickup": TunicLocationData("Overworld"),
    "Overworld - [East] Page Near Secret Shop": TunicLocationData("Overworld"),
    "Overworld - [Southwest] Fountain Page": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Page on Pillar by Dark Tomb": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Fire Wand Pickup": TunicLocationData("Overworld"),
    "Overworld - [West] Page On Teleporter": TunicLocationData("Overworld"),
    "Overworld - [Northwest] Page By Well": TunicLocationData("Overworld"),
    "Patrol Cave - Normal Chest": TunicLocationData("Overworld"),
    "Ruined Shop - Chest 1": TunicLocationData("Overworld"),
    "Ruined Shop - Chest 2": TunicLocationData("Overworld"),
    "Ruined Shop - Chest 3": TunicLocationData("Overworld"),
    "Ruined Passage - Page Pickup": TunicLocationData("Overworld"),
    "Shop - Potion 1": TunicLocationData("Overworld", "shop"),
    "Shop - Potion 2": TunicLocationData("Overworld", "shop"),
    "Shop - Coin 1": TunicLocationData("Overworld", "shop"),
    "Shop - Coin 2": TunicLocationData("Overworld", "shop"),
    "Special Shop - Secret Page Pickup": TunicLocationData("Overworld"),
    "Stick House - Stick Chest": TunicLocationData("Overworld"),
    "Sealed Temple - Page Pickup": TunicLocationData("Overworld"),
    "Hourglass Cave - Hourglass Chest": TunicLocationData("Overworld"),
    "Far Shore - Secret Chest": TunicLocationData("Overworld"),
    "Far Shore - Page Pickup": TunicLocationData("Overworld"),
    "Coins in the Well - 10 Coins": TunicLocationData("Overworld", "well"),
    "Coins in the Well - 15 Coins": TunicLocationData("Overworld", "well"),
    "Coins in the Well - 3 Coins": TunicLocationData("Overworld", "well"),
    "Coins in the Well - 6 Coins": TunicLocationData("Overworld", "well"),
    "Secret Gathering Place - 20 Fairy Reward": TunicLocationData("Overworld", "fairies"),
    "Secret Gathering Place - 10 Fairy Reward": TunicLocationData("Overworld", "fairies"),
    "Overworld - [West] Moss Wall Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [Southwest] Flowers Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [Southwest] Fountain Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [Northeast] Flowers Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [East] Weathervane Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [West] Windmill Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [Southwest] Haiku Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [West] Windchimes Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [South] Starting Platform Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Overworld - [Northwest] Golden Obelisk Page": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Old House - Holy Cross Door Page": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Cube Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Southeast Cross Door - Chest 3": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Southeast Cross Door - Chest 2": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Southeast Cross Door - Chest 1": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Maze Cave - Maze Room Holy Cross": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Caustic Light Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Old House - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Patrol Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Ruined Passage - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Hourglass Cave - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Sealed Temple - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Fountain Cross Door - Page Pickup": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Secret Gathering Place - Holy Cross Chest": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Top of the Mountain - Page At The Peak": TunicLocationData("Overworld Holy Cross", "holy cross"),
    "Monastery - Monastery Chest": TunicLocationData("Quarry"),
    "Quarry - [Back Entrance] Bushes Holy Cross": TunicLocationData("Quarry", "holy cross"),
    "Quarry - [Back Entrance] Chest": TunicLocationData("Quarry"),
    "Quarry - [Central] Near Shortcut Ladder": TunicLocationData("Quarry"),
    "Quarry - [East] Near Telescope": TunicLocationData("Quarry"),
    "Quarry - [East] Upper Floor": TunicLocationData("Quarry"),
    "Quarry - [Central] Below Entry Walkway": TunicLocationData("Quarry"),
    "Quarry - [East] Obscured Near Winding Staircase": TunicLocationData("Quarry"),
    "Quarry - [East] Obscured Beneath Scaffolding": TunicLocationData("Quarry"),
    "Quarry - [East] Obscured Near Telescope": TunicLocationData("Quarry"),
    "Quarry - [Back Entrance] Obscured Behind Wall": TunicLocationData("Quarry"),
    "Quarry - [Central] Obscured Below Entry Walkway": TunicLocationData("Quarry"),
    "Quarry - [Central] Top Floor Overhang": TunicLocationData("Quarry"),
    "Quarry - [East] Near Bridge": TunicLocationData("Quarry"),
    "Quarry - [Central] Above Ladder": TunicLocationData("Quarry"),
    "Quarry - [Central] Obscured Behind Staircase": TunicLocationData("Quarry"),
    "Quarry - [Central] Above Ladder Dash Chest": TunicLocationData("Quarry"),
    "Quarry - [West] Upper Area Bombable Wall": TunicLocationData("Quarry"),
    "Quarry - [East] Bombable Wall": TunicLocationData("Quarry"),
    "Hero's Grave - Ash Relic": TunicLocationData("Quarry"),
    "Quarry - [West] Shooting Range Secret Path": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Near Shooting Range": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Below Shooting Range": TunicLocationData("Lower Quarry"),
    "Quarry - [Lowlands] Below Broken Ladder": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Upper Area Near Waterfall": TunicLocationData("Lower Quarry"),
    "Quarry - [Lowlands] Upper Walkway": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Lower Area Below Bridge": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Lower Area Isolated Chest": TunicLocationData("Lower Quarry"),
    "Quarry - [Lowlands] Near Elevator": TunicLocationData("Lower Quarry"),
    "Quarry - [West] Lower Area After Bridge": TunicLocationData("Lower Quarry"),
    "Rooted Ziggurat Upper - Near Bridge Switch": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Upper - Beneath Bridge To Administrator": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Tower - Inside Tower": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Near Corpses": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Spider Ambush": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Left Of Checkpoint Before Fuse": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - After Guarded Fuse": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Guarded By Double Turrets": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - After 2nd Double Turret Chest": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Guarded By Double Turrets 2": TunicLocationData("Rooted Ziggurat"),
    "Rooted Ziggurat Lower - Hexagon Blue": TunicLocationData("Rooted Ziggurat"),
    "Ruined Atoll - [West] Near Kevin Block": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [South] Upper Floor On Power Line": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [South] Chest Near Big Crabs": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [North] Guarded By Bird": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Northeast] Chest Beneath Brick Walkway": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Northwest] Bombable Wall": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [North] Obscured Beneath Bridge": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [South] Upper Floor On Bricks": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [South] Near Birds": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Northwest] Behind Envoy": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Southwest] Obscured Behind Fuse": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [East] Locked Room Upper Chest": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [North] From Lower Overworld Entrance": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [East] Locked Room Lower Chest": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Northeast] Chest On Brick Walkway": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Southeast] Chest Near Fuse": TunicLocationData("Ruined Atoll"),
    "Ruined Atoll - [Northeast] Key Pickup": TunicLocationData("Ruined Atoll"),
    "Cathedral Gauntlet - Gauntlet Reward": TunicLocationData("Swamp"),
    "Cathedral - Secret Legend Trophy Chest": TunicLocationData("Swamp"),
    "Swamp - [Upper Graveyard] Obscured Behind Hill": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] 4 Orange Skulls": TunicLocationData("Swamp"),
    "Swamp - [Central] Near Ramps Up": TunicLocationData("Swamp"),
    "Swamp - [Upper Graveyard] Near Shield Fleemers": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Obscured Behind Ridge": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Obscured Beneath Telescope": TunicLocationData("Swamp"),
    "Swamp - [Entrance] Above Entryway": TunicLocationData("Swamp"),
    "Swamp - [Central] South Secret Passage": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Upper Walkway On Pedestal": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Guarded By Tentacles": TunicLocationData("Swamp"),
    "Swamp - [Upper Graveyard] Near Telescope": TunicLocationData("Swamp"),
    "Swamp - [Outside Cathedral] Near Moonlight Bridge Door": TunicLocationData("Swamp"),
    "Swamp - [Entrance] Obscured Inside Watchtower": TunicLocationData("Swamp"),
    "Swamp - [Entrance] South Near Fence": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Guarded By Big Skeleton": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Chest Near Graves": TunicLocationData("Swamp"),
    "Swamp - [Entrance] North Small Island": TunicLocationData("Swamp"),
    "Swamp - [Outside Cathedral] Obscured Behind Memorial": TunicLocationData("Swamp"),
    "Swamp - [Central] Obscured Behind Northern Mountain": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Upper Walkway Dash Chest": TunicLocationData("Swamp"),
    "Swamp - [South Graveyard] Above Big Skeleton": TunicLocationData("Swamp"),
    "Swamp - [Central] Beneath Memorial": TunicLocationData("Swamp"),
    "Hero's Grave - Feathers Relic": TunicLocationData("Swamp"),
    "West Furnace - Chest": TunicLocationData("West Garden"),
    "Overworld - [West] Near West Garden Entrance": TunicLocationData("West Garden"),
    "West Garden - [Central Highlands] Holy Cross (Blue Lines)": TunicLocationData("West Garden", "holy cross"),
    "West Garden - [West Lowlands] Tree Holy Cross Chest": TunicLocationData("West Garden", "holy cross"),
    "West Garden - [Southeast Lowlands] Outside Cave": TunicLocationData("West Garden"),
    "West Garden - [Central Lowlands] Chest Beneath Faeries": TunicLocationData("West Garden"),
    "West Garden - [North] Behind Holy Cross Door": TunicLocationData("West Garden", "holy cross"),
    "West Garden - [Central Highlands] Top of Ladder Before Boss": TunicLocationData("West Garden"),
    "West Garden - [Central Lowlands] Passage Beneath Bridge": TunicLocationData("West Garden"),
    "West Garden - [North] Across From Page Pickup": TunicLocationData("West Garden"),
    "West Garden - [Central Lowlands] Below Left Walkway": TunicLocationData("West Garden"),
    "West Garden - [West] In Flooded Walkway": TunicLocationData("West Garden"),
    "West Garden - [West] Past Flooded Walkway": TunicLocationData("West Garden"),
    "West Garden - [North] Obscured Beneath Hero's Memorial": TunicLocationData("West Garden"),
    "West Garden - [Central Lowlands] Chest Near Shortcut Bridge": TunicLocationData("West Garden"),
    "West Garden - [West Highlands] Upper Left Walkway": TunicLocationData("West Garden"),
    "West Garden - [Central Lowlands] Chest Beneath Save Point": TunicLocationData("West Garden"),
    "West Garden - [Central Highlands] Behind Guard Captain": TunicLocationData("West Garden"),
    "West Garden - [Central Highlands] After Garden Knight": TunicLocationData("West Garden"),
    "West Garden - [South Highlands] Secret Chest Beneath Fuse": TunicLocationData("West Garden"),
    "West Garden - [East Lowlands] Page Behind Ice Dagger House": TunicLocationData("West Garden"),
    "West Garden - [North] Page Pickup": TunicLocationData("West Garden"),
    "West Garden House - [Southeast Lowlands] Ice Dagger Pickup": TunicLocationData("West Garden"),
    "Hero's Grave - Effigy Relic": TunicLocationData("West Garden"),
}

hexagon_locations: Dict[str, str] = {
    "Red Questagon": "Fortress Arena - Siege Engine/Vault Key Pickup",
    "Green Questagon": "Librarian - Hexagon Green",
    "Blue Questagon": "Rooted Ziggurat Lower - Hexagon Blue",
}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

def get_loc_group(location_name: str) -> str:
    loc_group = location_table[location_name].location_group
    if loc_group == "region":
        # set loc_group as the region name. Typically, location groups are lowercase
        loc_group = location_table[location_name].region.lower()
    return loc_group


location_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(location_table, key=get_loc_group), get_loc_group)
}
