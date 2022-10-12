import pygame 

from abc import ABC, abstractmethod

class Fighter(ABC):
    

    @abstractmethod 
    def _init__(self, x, y):
        pass
      

    @abstractmethod
    def move(self, speed):
        pass

    @abstractmethod
    def draw(self, surface):
        pass
       

        


