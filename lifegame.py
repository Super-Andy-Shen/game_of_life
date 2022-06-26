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
        self.pawns = pygame.sprite.Group()
        self.mypawn_1 = Pawn(self)
        self.mypawn_2 = Pawn(self)
        self.mypawn_3 = Pawn(self)
        self.mypawn_4 = Pawn(self)
        self.mypawn_2.rect.x= self.mypawn_1.rect.x 
        self.mypawn_2.rect.y= self.mypawn_1.rect.y - 10
        self.mypawn_3.rect.x= self.mypawn_1.rect.x - 10
        self.mypawn_3.rect.y= self.mypawn_1.rect.y 
        self.mypawn_4.rect.x= self.mypawn_1.rect.x + 10
        self.mypawn_4.rect.y= self.mypawn_1.rect.y + 10
        self.mypawn_1.life = True
        self.mypawn_2.life = True
        self.mypawn_3.life = True
        self.mypawn_4.life = True
        self.pawns.add(self.mypawn_1)
        self.pawns.add(self.mypawn_2)
        self.pawns.add(self.mypawn_3)
        self.pawns.add(self.mypawn_4)
        self.m = 0
    
    
    def run_game(self):
         while True:
            self._check_events()
            self._update_screen()
            print(self.m)
    
    
    
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
        for pawn in self.pawns:
            self.m += 1
            self.rules(pawn)
        
        pygame.display.flip()
    
    
    def rules(self,p):
        num = 0
        EE = Pawn(self)
        EE.rect.x = p.rect.x + 10
        EE.rect.y = p.rect.y
        WW = Pawn(self)
        WW.rect.x = p.rect.x - 10
        WW.rect.y = p.rect.y
        NW = Pawn(self)
        NW.rect.x = p.rect.x - 10
        NW.rect.y = p.rect.y - 10
        NE = Pawn(self)
        NE.rect.x = p.rect.x + 10
        NE.rect.y = p.rect.y - 10
        SE = Pawn(self)
        SE.rect.x = p.rect.x + 10
        SE.rect.y = p.rect.y + 10
        SW = Pawn(self)
        SW.rect.x = p.rect.x - 10
        SW.rect.y = p.rect.y + 10
        SS = Pawn(self)
        SS.rect.x = p.rect.x 
        SS.rect.y = p.rect.y + 10
        NN = Pawn(self)
        NN.rect.x = p.rect.x 
        NN.rect.y = p.rect.y - 10

        for pp in self.pawns:
            if pp.rect.colliderect(EE) and pp.life:
                num += 1
                EE.life = True
            if pp.rect.colliderect(WW) and pp.life:
                num += 1
                WW.life = True
            if pp.rect.colliderect(NW) and pp.life:
                num += 1
                NW.life = True
            if pp.rect.colliderect(NE) and pp.life:
                num += 1
                NE.life = True
            if pp.rect.colliderect(SE) and pp.life:
                num += 1
                SE.life = True
            if pp.rect.colliderect(SW) and pp.life:
                num += 1
                SW.life = True
            if pp.rect.colliderect(SS) and pp.life:
                num += 1
                SS.life = True
            if pp.rect.colliderect(NN) and pp.life:
                num += 1
                NN.life = True
        
        if num < 2 :
            p.life = False
        elif num <= 3 :
            p.life = True
        else:
            p.life = False
        
        p.draw_pawn()

        if EE.life == False:
            self.pawns.add(EE)
        if WW.life == False:
            self.pawns.add(WW)
        if NW.life == False:
            self.pawns.add(NW)
        if NE.life == False:
            self.pawns.add(NE)
        if SE.life == False:
            self.pawns.add(SE)
        if SW.life == False:
            self.pawns.add(SW)
        if SS.life == False:
            self.pawns.add(SS)
        if NN.life == False:
            self.pawns.add(NN)





        


       

    
        
# Main Progame 
if __name__ == "__main__":
  ai = Lifegame()
  ai.run_game()


    
                