import unittest
import pygame
from unittest.mock import patch
from io import StringIO

from spaceshooter_gy import Game  # Adjust this import path to match your file name

class TestSpaceShooter(unittest.TestCase):
    def setUp(self):
        """
        Setup the game instance for testing.
        """
        pygame.init()
        self.game = Game()

    def tearDown(self):
        """
        Quit pygame after tests.
        """
        pygame.quit()

    def test_initial_conditions(self):
        """
        Test initial conditions of the game.
        """
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.health, 3)
        self.assertEqual(len(self.game.enemies), 0)
        self.assertIsNone(self.game.boss)

    def test_spawn_enemy(self):
        """
        Test enemy spawning.
        """
        self.game.spawn_enemy()
        self.assertEqual(len(self.game.enemies), 1)
        self.assertEqual(self.game.enemies[0].width, 50)
        self.assertEqual(self.game.enemies[0].height, 50)

    def test_spawn_boss(self):
        """
        Test boss spawning.
        """
        self.game.spawn_boss()
        self.assertIsNotNone(self.game.boss)
        self.assertEqual(self.game.boss.width, 150)
        self.assertEqual(self.game.boss.height, 100)
        self.assertEqual(self.game.boss_health, 10)

    def test_player_bullet_collision_with_enemy(self):
        """
        Test collision between bullets and enemies.
        """
        self.game.spawn_enemy()
        enemy = self.game.enemies[0]
        bullet = pygame.Rect(enemy.centerx, enemy.top - 10, 10, 20)
        self.game.bullets.append(bullet)
        self.game.detect_collisions()
        self.assertEqual(len(self.game.enemies), 0)
        self.assertEqual(len(self.game.bullets), 0)
        self.assertEqual(self.game.score, 1)

    def test_player_bullet_collision_with_boss(self):
        """
        Test collision between bullets and the boss.
        """
        self.game.spawn_boss()
        boss = self.game.boss
        bullet = pygame.Rect(boss.centerx, boss.top - 10, 10, 20)
        self.game.bullets.append(bullet)
        self.game.detect_collisions()
        self.assertEqual(self.game.boss_health, 9)
        self.assertEqual(len(self.game.bullets), 0)

    def test_player_health_reduction(self):
        """
        Test health reduction when colliding with an enemy.
        """
        self.game.spawn_enemy()
        enemy = self.game.enemies[0]
        self.game.player_rect.topleft = enemy.topleft
        self.game.detect_collisions()
        self.assertEqual(self.game.health, 2)
        self.assertEqual(len(self.game.enemies), 0)

    def test_boss_health_zero_removes_boss(self):
        """
        Test boss removal when health reaches zero.
        """
        self.game.spawn_boss()
        self.game.boss_health = 1
        boss = self.game.boss
        bullet = pygame.Rect(boss.centerx, boss.top - 10, 10, 20)
        self.game.bullets.append(bullet)
        self.game.detect_collisions()
        self.assertIsNone(self.game.boss)
        self.assertEqual(self.game.score, 20)

    def test_increase_difficulty(self):
        """
        Test if the game increases speed multiplier with the score.
        """
        self.game.score = 10
        self.game.increase_difficulty()
        self.assertEqual(self.game.speed_multiplier, 1.1)
        self.game.score = 20
        self.game.increase_difficulty()
        self.assertEqual(self.game.speed_multiplier, 1.2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_message(self, mock_stdout):
        """
        Test display message functionality.
        """
        self.game.display_message("Test Message", "white")
        self.assertTrue(mock_stdout.getvalue(), "Test Message")

if __name__ == '__main__':
    unittest.main()
