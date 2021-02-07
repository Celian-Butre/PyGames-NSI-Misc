import pygame
backgroundColor = 255,255,255
width, height = 600, 800
pygame.init

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill(backgroundColor)
    pygame.display.flip()