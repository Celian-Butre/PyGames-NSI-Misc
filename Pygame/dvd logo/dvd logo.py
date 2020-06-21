import time
import pygame
pygame.init()
width, height = 800, 600
backgroundColor = 0, 0, 0
dvdLogoSpeed = [1,  1]  

screen = pygame. display.set_mode((width, height))

dvdLogo = pygame.image.load("dvd-logo.png")
dvdLogoRect = dvdLogo.get_rect()

while True:
  screen.fill (backgroundColor)
  
  screen.blit(dvdLogo, dvdLogoRect)
  dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

  if dvdLogoRect.left < 0  or dvdLogoRect.right > width:
    dvdLogoSpeed[0] = -dvdLogoSpeed[0]
  if dvdLogoRect.top < 0  or dvdLogoRect.bottom > height:
    dvdLogoSpeed[1] = -dvdLogoSpeed[1]

  pygame.display.flip()
  time.sleep(10 / 1000)

  