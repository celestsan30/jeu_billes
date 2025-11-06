from src.scenes.play_scene import PlayScene
from src.settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jeu de Billes")

    play_scene = PlayScene(screen)  # créer la scène de jeu
    play_scene.run()  # lance la boucle de la partie

if __name__ == "__main__":
    main()
    
 
