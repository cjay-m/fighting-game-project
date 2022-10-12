import pygame

from characters.fighter import Fighter

class Sword(Fighter): 

    def _init__(self, x, y): 
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self, speed):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0, 0), self.rect)