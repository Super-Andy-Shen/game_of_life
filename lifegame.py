import pygame
import sys
from settings import Settings
from pawn import Pawn
class Lifegame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Game of Life---Kang's Version")
        self.mypawn = Pawn(self)

    
    def run_game(self):
         while True:
            self._check_events()
            self._update_screen()
    
    
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
    
    
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_ESCAPE:
              sys.exit()
    
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.mypawn.draw_pawn()
        pygame.display.flip()


# Main Progame 
if __name__ == "__main__":
  ai = Lifegame()
  ai.run_game()


    
                