import pygame
import sys

class Grille:
    def __init__(self):
        self.lignes =



class jeu :
    def __init__(self):
        self.ecran= pygame.display.set_mode((600,500))
        pygame.display.set_caption('Tic Tac Teo')
        self.jeu_encours= True

    def fonction_principale(self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            self.ecran.fill((240,240,240))
            pygame.display.flip()
if __name__== '__main__':
    pygame.init()
    jeu().fonction_principale()
    pygame.quit()