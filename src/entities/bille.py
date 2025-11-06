import pygame, sys
from src.settings import *

RAYON_BILLE = 10

class Bille:
    def __init__(self,x,y,couleur,joueur) :
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.couleur = couleur
        self.joueur = joueur
        self.dans_carre = True
        self.active = False

    def dessiner(self):
        pygame.draw.circle(screen,self.couleur, (int(self.x),int(self.y)),RAYON_BILLE)

    def deplacer(self):
        if self.active :
            self.x += self.vx
            self.y += self.vy

        if self.x - 10 < 0 or self.x + 10 > 800 :
            self.vx *= -1
        
        if self.y - 10 < 0 or self.y + 10 > 600 :
            self.vy *= -1

