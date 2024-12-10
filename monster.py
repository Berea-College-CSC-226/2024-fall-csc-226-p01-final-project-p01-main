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
# https://www.pygame.org/docs/ref/sprite.html - Killing Sprites using .kill
# https://www.youtube.com/watch?v=4TfZjhw0J-8 - sprite groups explained
#https://www.pygame.org/docs/ref/image.html#pygame.image.load
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import pygame
import random
from player import *
from dungeon import *


class Monster(pygame.sprite.Sprite): #Monster is child of sprite class
    def __init__(self,screen_size, width=50, height=50):
        """
        Handles the basic logic needed to create monsters
        """
        super().__init__()
        pygame.sprite.Sprite.__init__(self)  # Calls the sprite methods from pygame sprite
        self.screen_size = screen_size
        print("Spawning monster")
        self.image = pygame.image.load('image/enemy.png').convert_alpha()
        self.surf = pygame.transform.scale(self.image, (width, height))  # changes height and width of monster


        # self.surf = pygame.image.load('image/enemy.png').convert_alpha()
        # self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()

        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)

        # self.surf = pygame.transform.scale(self.image, (width, height)) #changes height and width of monster

        self.rect.x = 10 #screen_size[0] - width  # Right of screen, changes spawn point
        self.rect.y = 4  # Top of screen, changes spawn point
        self.health = 2
        #Code from tuna teamwork
        self.move_distance = 2
        self.directions = ["north", "south", "east", "west"]
        self.path = random.choice(self.directions)
        self.position = [0, 0]




    def direction(self):
        """
        Choose a direction for movement purposes TO DO: Create a back and forth motion for monsters, use legend of Tuna as base
        :return:
        """

        def get_directions(self):
            """
            Keeps the NPC on the screen.
            :return: None
            """
            pass

    def movement(self):
        """
        Moves the characters in a pattern
        :return:
        """
        #Eventual momvement of monster
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top <= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"
        elif random.random() > .95:
            self.path = random.choice(self.directions)

        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance




    def take_damage(self, damage):
        """
        calculates the damage the monster takes after its been hit
        :param:
        :return:
        """
        #Trying to make monster take damage
        self.health -= damage
        if self.health <= 0:
            self.kill() #removes sprite from group, removes sprite form screen


