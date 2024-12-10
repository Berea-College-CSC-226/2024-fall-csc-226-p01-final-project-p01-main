######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose:
#
#
######################################################################
# Acknowledgements:
# Collision Examples- https://github.com/search?q=pygame.sprite.collide_rect+language%3APython&type=Code&l=Python
# Collision examples found on - https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.kill
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import pygame
from monster import *
import time
# from dungeon import *
# from item import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size, width=50, height=50):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning player")
        self.surf = pygame.image.load('image/player.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        #self.surf = pygame.transform.scale(self.surf, (width, height))  # changes height
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)
        self.move_distance = 0
        self.position = [0,0]


    def boundaries(self):
        """
        Keep player from leaving boundaries
        :return:
        """
        #Attempting to create better boundaries
        if self.rect.bottom >self.screen_size[1]:
            self.rect.bottom = self.screen_size[1]
            self.direction = "north"
        elif self.rect.top <0:
            self.rect.top = 0
            self.direction = "south"
        elif self.rect.left <0:
            self.rect.left = 0
            self.direction = "east"
        elif self.rect.right >self.screen_size[0]:
            self.rect.right = self.screen_size[0]
            self.direction = "west"
        else:
            self.direction = "none"

    def movement(self, keys):
        """
        Handles movement events from the player

        :param keys: key presses from pygame event listener

        :return: None
        """
        #Attempting better movement
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -1)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)
        self.boundaries()



    def take_damage(self):
        """
        calculates the damage the player takes after its been hit, and reduces health
        :param:
        :return:
        """
        pass


