import unittest
from player import Player
from npc import NPC
from platform import Platform

class TestGameComponents(unittest.TestCase):
    def setUp(self):
        # Initialize objects for testing
        self.player = Player("GameImage/tacocat.png", 100, 400)
        self.npc = NPC("GameImage/fashiondemon.png", 700, 400)
        self.platform = Platform(100, 500, 300, 20, "GameImage/platform_image.png")

    def test_player_initial_position(self):
        # Test the initial position of the player
        self.assertEqual(self.player.rect.x, 100)
        self.assertEqual(self.player.rect.y, 400)

    def test_npc_following(self):
        # Test if NPC follows the player when player moves to the right
        initial_npc_x = self.npc.rect.x
        self.player.rect.x += 50  # Simulate player moving to the right
        self.npc.update(self.player)
        self.assertTrue(self.npc.rect.x > initial_npc_x)

    def test_platform_collision(self):
        # Test player landing on a platform
        self.player.rect.y = self.platform.rect.top - 1  # Position player just above the platform
        self.player.velocity[1] = 1  # Simulate falling
        self.player.update([self.platform], [])
        self.assertEqual(self.player.rect.bottom, self.platform.rect.top)
        self.assertEqual(self.player.velocity[1], 0)  # Player should stop falling

if __name__ == "__main__":
    unittest.main()
