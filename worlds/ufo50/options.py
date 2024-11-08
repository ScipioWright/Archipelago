from dataclasses import dataclass
from Options import StartInventoryPool, Range, OptionSet, PerGameCommonOptions, OptionGroup
from .constants import game_ids


class AlwaysOnGames(OptionSet):
    """
    Choose which games you would like to enable.
    """
    internal_name = "always_on_games"
    display_name = "Always On Games"
    valid_keys = {game_name for game_name in game_ids.keys()}


class RandomChoiceGames(OptionSet):
    """
    Choose which games have a chance of being enabled.
    The number of games that will be enabled is based on the Random Choice Game Count option.
    """
    internal_name = "random_choice_games"
    display_name = "Random Choice Games"
    valid_keys = {game_name for game_name in game_ids.keys()}


class RandomChoiceGameCount(Range):
    """
    Choose how many Random Choice Games will be included alongside your Always On Games.
    If you do not have enough Random Choice Games selected, it will enable all your selected games.
    """
    internal_name = "random_choice_game_count"
    display_name = "Random Choice Game Count"
    range_start = 0
    range_end = 50
    default = 0


class StartingGameAmount(Range):
    """
    Choose how many games to have unlocked at the start.
    At least on of the starting games will always be one of the implemented games.
    If this value is higher than the number of games you selected, you will start with all of them unlocked.
    If you put a game in your start inventory from pool, it will count towards the amount from this option.
    """
    internal_name = "starting_game_amount"
    display_name = "Starting Game Amount"
    range_start = 1
    range_end = 50
    default = 1


# todo: specific option for choosing the games you want on


@dataclass
class UFO50Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    always_on_games: AlwaysOnGames
    random_choice_games: RandomChoiceGames
    random_choice_game_count: RandomChoiceGameCount
    starting_game_amount: StartingGameAmount


ufo50_option_groups = [
    OptionGroup("General Options", [
        AlwaysOnGames,
        RandomChoiceGames,
        RandomChoiceGameCount,
        StartingGameAmount,
    ])
]
