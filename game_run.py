######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose: This program is designed to test my final project
#
#
######################################################################
# Acknowledgements:
# https://www.pygame.org/docs/ref/display.html for updating display, as well as just general pygame tools
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect - More collision Information
#https://www.pygame.org/docs/ref/time.html#pygame.time.delay - delay/Timer
# str(self.player.hp) - converting a int into a string for display - Professor Hegan
#https://www.pygame.org/docs/ref/time.html - get ticks, clock
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
from random import randint

from player import *
from monster import *
from attack import *
import pygame

class Game(pygame.sprite.Sprite):
    def __init__(self):
        """
        Handles the basic logic needed to actually run the game
        """
        pygame.init()
        pygame.sprite.Sprite.__init__(self)  # Calls the sprite methods from pygame sprite
        self.size = (500,500) #Window size
        self.screen = pygame.display.set_mode(self.size)
        self.player = Player(self.size)
        self.monster = Monster(self.size)
        self.attack = Attack(self.size)
        self.chest = Item(self.size)
        self.damage = 5
        self.enemy_invincible = False
        self.chest_empty = False
        self.player_invincible = False

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()  # Group for all sprites
        self.monster_group = pygame.sprite.Group()  # Separate group for monsters
        self.attack_group = pygame.sprite.Group()  # Separate group for attacks
        self.chest_group = pygame.sprite.Group()  # Separate group for attacks
        self.player_group = pygame.sprite.Group()  # Separate group for attacks

        # Add sprites to groups
        self.all_sprites.add(self.monster)
        self.monster_group.add(self.monster)

        # Add sprites to groups
        self.all_sprites.add(self.attack)
        self.attack_group.add(self.attack)

        # Add sprites to groups
        self.all_sprites.add(self.chest)
        self.chest_group.add(self.chest)

        # Add sprites to groups
        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

        #Tick spawn time
        self.last_attack_time = pygame.time.get_ticks()
        self.attack_duration = 5000  # 5 seconds
        self.attack_cooldown = 5000  # 5 seconds cooldown time for spawning
        self.attack_move = 1000 # 1 second before attack moves


    def spawn_attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cooldown:
            # self.attack.add(self.new_attack)  # Add it to the group
            # pygame.attack.Attack.add(new_attack)
            self.attack.rect.x = self.monster.rect.x #moves attack to where monster just was
            self.attack.rect.y = self.monster.rect.y
            self.last_attack_time = current_time


    def handle_collisions(self, keys, damage):
        """
        Moved all collisions here, as a way to stop the lag
        :param keys:
        :param damage:
        :return:
        """
        # Collision - Player damages Monster
        if pygame.sprite.collide_rect(self.player, self.monster):
            if keys[pygame.K_f] and not self.enemy_invincible: #Checks if monster is able to be hurt
                Monster.take_damage(self.monster, damage)
                self.enemy_invincible = True #Checks if monster is able to be hurt
                pygame.time.delay(1000)
                self.enemy_invincible = False

        # Collision - Enemy attacks player
        if pygame.sprite.spritecollide(self.player, self.attack_group, dokill=True) and not self.player_invincible:
            Player.take_damage(self.player, damage)
            self.player_invincible = True
            pygame.time.delay(1000)
            self.player_invincible = False

    # Collision - Chest and Player
        if pygame.sprite.collide_rect(self.player, self.chest):
            if keys[pygame.K_a] and not self.chest_empty:
                self.chest.gold = self.chest.gold + randint(20, 100)
                self.chest_empty = True

    def game_loop(self, damage):
        """
        Handles running the game
        :return:
        """
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.screen.fill('gray')
            self.player.movement(pygame.key.get_pressed())
            keys = pygame.key.get_pressed()  #currently pressed keys
            self.player.movement(keys)  #Update players position based on keys
            self.all_sprites.draw(self.screen)
            self.monster.movement() #Monster moves
            self.attack.movement() #attack moves when spawned

            self.spawn_attack()

            #Handles collision
            self.handle_collisions(keys, damage)

            #Update sprites
            self.all_sprites.update()

            #Draws sprites
            self.all_sprites.draw(self.screen)

            #Check for game over
            self.game_over()

            # Display stats (e.g., health, gold) maybe move later?
            font = pygame.font.SysFont("ComicSans", 10)

            # Health text
            txt = font.render('Health', True, "darkblue")
            self.screen.blit(txt, (self.size[0] // 16, self.size[1] - 200))
            player_health = font.render(str(self.player.hp), True, "darkblue")
            self.screen.blit(player_health, (self.size[0] // 4, self.size[1] - 200))

            # Gold Text
            text = font.render('Gold', True, "darkblue")
            self.screen.blit(text, (self.size[0] // 3, self.size[1] - 200))
            t = font.render(str(self.chest.gold), True, "darkblue")
            self.screen.blit(t, (self.size[0] // 2, self.size[1] - 200))

            pygame.display.update()  # Update the display



    def game_over(self):
        """
        checks if game is over
        :return:
        """
        if self.player.hp <=0:
            # self.screen.fill('black')
            self.player.kill()
            self.monster.kill()
            self.attack.kill()
            self.chest.kill()
            # Display stats (e.g., health, gold) maybe move later?
            font = pygame.font.SysFont("ComicSans", 10)

            # Health text
            txt = font.render('Health', True, "white")
            self.screen.blit(txt, (self.size[0] // 16, self.size[1] - 200))
            player_health = font.render(str(self.player.hp), True, "white")
            self.screen.blit(player_health, (self.size[0] // 4, self.size[1] - 200))

            # Gold Text
            text = font.render('Gold', True, "white")
            self.screen.blit(text, (self.size[0] // 3, self.size[1] - 200))
            t = font.render(str(self.chest.gold), True, "white")
            self.screen.blit(t, (self.size[0] // 2, self.size[1] - 200))



    def display_stats(self):
        """
        displays information on screen such as gold, health, and item
        :return:
        """



        pygame.quit()

def main():
    """
    Starts the dungeon crawler

    :return: None
    """
    game = Game()
    game.game_loop(game.damage)  #Passed parameter into loop


if __name__ == "__main__":
    main()