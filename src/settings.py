import pygame, sys


WIDTH, HEIGHT = 800, 600
CARRE = pygame.Rect(250, 150, 300, 300)
FPS = 60

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 100, 255)
VERT = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Billes - Célestin")
