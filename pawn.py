import pygame
from pygame.sprite import Sprite

class Pawn(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width,self.height = 10,10
        self.pawn_color = (0,0,0)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.life = False
    
    
    def update(self,alive):
        self.life = alive
    
    
    def draw_pawn(self):
        if self.life:
           self.screen.fill(self.pawn_color,self.rect)

      