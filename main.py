import pygame, sys
from pygame.locals import *
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
CARRE = pygame.Rect(250, 150, 300, 300)
FPS = 60
RAYON_BILLE = 10

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 100, 255)
VERT = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Billes - Célestin")

class Bille:
    def __init__(self,x,y,couleur,joueur) :
        self.x = x
        self.y = y
        self.couleur = couleur
        self.joueur = joueur
        self.dans_carre = True

    def dessiner(self):
        pygame.draw.circle(screen,self.couleur, (int(self.x),int(self.y)),RAYON_BILLE)


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
    
 
