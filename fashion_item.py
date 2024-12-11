from item import Item


class FashionItem(Item):
    """
    Represents a fashion-related item in the game, extending the base Item class.
    """

    def __init__(self, position, item_type, style_points, rarity="common"):
        """
        Initializes the fashion item with its position, type, style points, and rarity.

        :param position: Tuple (x, y) representing the item's position.
        :param item_type: String representing the type of the fashion item (e.g., "hat", "shoes").
        :param style_points: Integer representing the points the item adds to the player's fashion score.
        :param rarity: String representing the rarity of the item (default: "common").
        """
        super().__init__(position, item_type)
        self.style_points = style_points
        self.rarity = rarity

    def activate_effect(self, player, sound_manager):
        """
        Activates the effect of the fashion item, adding style points to the player's score.

        :param player: The Player object collecting the item.
        :param sound_manager: The SoundManager object to play sound effects.
        """
        player.add_fashion_points(self.style_points)
        sound_manager.play_sound_effect("fashion_points")
        print(f"{player.name} collected a {self.rarity} {self.type} worth {self.style_points} points!")

    def describe(self):
        """
        Provides a description of the fashion item.

        :return: A string describing the item.
        """
        return f"A {self.rarity} {self.type} worth {self.style_points} style points."
