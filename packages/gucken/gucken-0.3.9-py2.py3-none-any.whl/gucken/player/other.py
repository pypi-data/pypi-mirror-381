from dataclasses import dataclass

from .common import Player
from ..settings import gucken_settings_manager

@dataclass
class OtherPlayer(Player):
    supports_headers: bool = False

    @classmethod
    def is_available(cls) -> bool:
        return True

    def play(
        self,
        url: str,
        title: str,
        full_screen: bool,
        headers: dict[str, str] = None,
        override_executable: str = None,
    ) -> list[str]:
        args = gucken_settings_manager.settings["settings"]["player"]["args"]
        return [override_executable, args.format(title=title, url=url)]
