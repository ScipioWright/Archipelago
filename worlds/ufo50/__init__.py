from typing import ClassVar, Dict, Any, Type, Union

import Utils
from BaseClasses import Tutorial
from Options import PerGameCommonOptions, OptionError
from settings import Group, UserFilePath, LocalFolderPath, Bool
from worlds.AutoWorld import World, WebWorld
from .constants import *
from . import options
from .games.game_manager import get_items, get_locations, get_options, GameManager


class UFO50Settings(Group):
    class GamePath(UserFilePath):
        """Path to the game executable from which files are extracted"""
        description = "the UFO 50 game executable"
        is_exe = True
        md5s = [GAME_HASH]

    class InstallFolder(LocalFolderPath):
        """Path to the mod installation folder"""
        description = "the folder to install UFO 50 Archipelago to"

    class LaunchGame(Bool):
        """Set this to false to never autostart the game"""

    class LaunchCommand(str):
        """
        The console command that will be used to launch the game
        The command will be executed with the installation folder as the current directory
        """

    exe_path: GamePath = GamePath("ufo50.exe")
    install_folder: InstallFolder = InstallFolder("UFO 50")
    launch_game: Union[LaunchGame, bool] = True
    launch_command: LaunchCommand = LaunchCommand("ufo50.exe" if Utils.is_windows
                                                  else "wine ufo50.exe")


class UFO50Web(WebWorld):
    theme = "partyTime"
    bug_report_page = "https://github.com/UFO-50-Archipelago/ufo-50-archipelago/issues"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up UFO 50 for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["LeonarthCG"]
    )
    tutorials = [setup_en]


class UFO50World(World):
    """ 
    UFO 50 is a collection of 50 single and multiplayer games from the creators of Spelunky, Downwell, Air Land & Sea,
    Skorpulac, Catacomb Kids, and Madhouse.
    Jump in and explore a variety of genres, from platformers and shoot 'em ups to puzzle games and RPGs.
    Our goal is to combine a familiar 8-bit aesthetic with new ideas and modern game design sensibilities.
    """  # Excerpt from https://50games.fun/
    game = GAME_NAME
    web = UFO50Web()
    required_client_version = (0, 5, 0)

    topology_present = False

    item_name_to_id = {k: v for k, v in get_items().items()}
    location_name_to_id = {k: v for k, v in get_locations().items()}

    options_dataclass: ClassVar[Type[PerGameCommonOptions]] = options.UFO50Options
    options: options.UFO50Options
    settings_key = "ufo_50_settings"
    settings: ClassVar[UFO50Settings]

    manager: GameManager

    def generate_early(self) -> None:
        self.manager = GameManager(self)
        if not self.player_name.isascii():
            raise OptionError(f"{self.player_name}'s name must be only ASCII.")

    def create_regions(self) -> None:
        self.manager.create_regions()

    def create_items(self) -> None:
        self.manager.create_items()

    def get_filler_item_name(self) -> str:
        return self.manager.get_filler_item_name()

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict()
        return slot_data
