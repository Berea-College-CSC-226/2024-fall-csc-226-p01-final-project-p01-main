class Item:
    """
    Represents the items in my game, such as a speed boost or fashion points.
    """

    def __init__(self, position, item_type, effect_value=0):
        """
        Initializes the item with its position, type, and effect value.

        :param position: Tuple (x, y) representing the item's position on the map.
        :param item_type: String representing the type of the item (e.g., "speed_boost", "fashion_points").
        :param effect_value: The magnitude of the effect (e.g., points to add, speed multiplier).
        """
        self.position = position
        self.type = item_type
        self.effect_value = effect_value

    def activate_effect(self, player, sound_manager):
        """
        Activates the item's effect on the player and triggers a sound effect.

        :param player: The Player object interacting with the item.
        :param sound_manager: The SoundManager object to play sound effects.
        """
        if self.type == "speed_boost":
            player.increase_speed(self.effect_value)
            sound_manager.play_sound("speed_boost_collected")
            print(f"Speed boost activated! Multiplier: {self.effect_value}")
        elif self.type == "fashion_points":
            player.add_fashion_points(self.effect_value)
            sound_manager.play_sound("fashion_points_collected")
            print(f"Fashion points gained: {self.effect_value}")
        elif self.type == "health":
            player.heal(self.effect_value)
            sound_manager.play_sound("health_collected")
            print(f"Health restored: {self.effect_value}")
        else:
            print(f"Unknown item type: {self.type}")