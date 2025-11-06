import pygame, sys
from pygame.locals import *
import random
import math
from src.entities.bille import Bille
from src.settings import *

pygame.init()

bille_j1 =[Bille(150,300 + i*25,BLEU,1) for i in range(10)]
bille_j2 =[Bille(650,300 + i*25,ROUGE,2) for i in range(10)]

clock = pygame.time.Clock()
running = True


while running:

    screen.fill(BLANC)
    pygame.draw.rect(screen, NOIR, CARRE, 3)
   
    for bille in bille_j1 + bille_j2:
        bille.dessiner()
    
    # Texte des scores
    font = pygame.font.SysFont(None, 30)
    txt1 = font.render(f"Joueur 1 : {len(bille_j1)} billes", True, BLEU)
    txt2 = font.render(f"Joueur 2 : {len(bille_j2)} billes", True, ROUGE)
    screen.blit(txt1, (20, 20))
    screen.blit(txt2, (WIDTH - 250, 20))

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    
 
