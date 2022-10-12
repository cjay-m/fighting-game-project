import pygame 

from abc import ABC, abstractmethod

class Fighter(ABC):
    

    @abstractmethod 
    def _init__(self, x, y): 
        self.rect = pygame.Rect((x, y, 80, 180))

    @abstractmethod
    def move(self, speed):
        pass

    @abstractmethod
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0, 0), self.rect)

        


