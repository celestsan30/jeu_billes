import pygame, sys
from src.settings import *

RAYON_BILLE = 10

class Bille:
    def __init__(self,x,y,couleur,joueur) :
        self.x = x
        self.y = y
        self.couleur = couleur
        self.joueur = joueur
        self.dans_carre = True

    def dessiner(self):
        pygame.draw.circle(screen,self.couleur, (int(self.x),int(self.y)),RAYON_BILLE)
