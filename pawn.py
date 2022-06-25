from email.mime import image
from tkinter.tix import Tree
import pygame

class Pawn:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width,self.height = 50,50
        self.pawn_color = (0,0,0)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
    
    def draw_pawn(self):
        self.screen.fill(self.pawn_color,self.rect)
      