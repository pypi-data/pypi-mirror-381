# Copyright © 2025 GlacieTeam. All rights reserved.

from typing import Dict, Callable, Optional, List
from endstone import Player
from endstone.plugin import Plugin

class ChestForm:
    """
    Chest form API
    """

    def __init__(self, plugin: Plugin, title: str = "ChestUI", large_chest=True):
        """
        Create a chest form

        Args:
            plugin (Plugin): The plugin using chest form
            title (str): The title of the chest sent to client
            large_chest (bool): Whether to send a large chest
        """

    def set_title(self, title: str) -> None:
        """
        Set the title of the chest

        Args:
            title (str): The title of the chest sent to client
        """

    def set_slot(
        self,
        slot: int,
        item_type: str,
        callback: Optional[Callable[[Player, int], None]] = None,
        *,
        item_amount: int = 1,
        item_data: int = 0,
        display_name: Optional[str] = None,
        lore: Optional[List[str]] = None,
        enchants: Optional[Dict[str, int]] = None,
    ) -> None:
        """
        Set item in a specfic slot with click callback

        Args:
            slot (int): The index of the slot
            item_type (str): The full type name of the item
            callback (Optional[Callable[[Player, int], None]]): The click callback of the slot
            item_amount (int): The amount of the item
            item_data (int): The aux value of the item
            display_name (Optional[str]): The custom name (display name) of the item
            lore (Optional[List[str]]): The lore of the item
            enchants (Optional[Dict[str, int]]): The enchantments on the item (ingore vanilla limit)
        """

    def fill_slots(
        self,
        item_type: str,
        *,
        item_amount: int = 1,
        item_data: int = 0,
        display_name: Optional[str] = None,
        lore: Optional[List[str]] = None,
        enchants: Optional[Dict[str, int]] = None,
    ) -> None:
        """
        Fill all slots with a default item with no callback (default placeholder item)
        This method is recommend to call at first

        Args:
            item_type (str): The full type name of the item
            item_amount (int): The amount of the item
            item_data (int): The aux value of the item
            display_name (Optional[str]): The custom name (display name) of the item
            lore (Optional[List[str]]): The lore of the item
            enchants (Optional[Dict[str, int]]): The enchantments on the item (ingore vanilla limit)
        """

    def send_to(self, player: Player) -> None:
        """
        Send the form to a player

        Args:
            player (Player): The player who receive the form
        """
