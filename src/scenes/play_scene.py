import pygame, sys
import random
import math
from src.entities.bille import Bille
from src.settings import *

class PlayScene :
    def __init__(self, screen):
        self.screen = screen
        self.bille_j1 =[Bille(150,300 + i*25,BLEU,1) for i in range(10)]
        self.bille_j2 =[Bille(650,300 + i*25,ROUGE,2) for i in range(10)]
        self.tour_joueur = 1
        self.bille_en_cours = None
        self.clock = pygame.time.Clock()
        self.running = True
    

    def run(self):

        while self.running:

         self.screen.fill(BLANC)
         pygame.draw.rect(screen, NOIR, CARRE, 3)
   
         for bille in self.bille_j1 + self.bille_j2:
             bille.dessiner()

         # Texte des scores
         font = pygame.font.SysFont(None, 30)
         txt1 = font.render(f"Joueur 1 : {len(self.bille_j1)} billes", True, BLEU)
         txt2 = font.render(f"Joueur 2 : {len(self.bille_j2)} billes", True, ROUGE)
         self.screen.blit(txt1, (20, 20))
         self.screen.blit(txt2, (WIDTH - 250, 20))

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

         pygame.display.flip()
         self.clock.tick(FPS)

    




 
 
