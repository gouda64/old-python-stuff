import random
import pygame
import math
import sys
from pygame.locals import *

from sprite_loader import *
#from player import *
from cat import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#color = (0, 128, 128)

background_image = pygame.image.load("forest.png").convert()
cat_images = []
#man_images = {}

def get_images():
  cat_sheet = SpriteSheet('runningcat.png')
  #man_sheet = SpriteSheet('man.png)
  directions = ['n', 'w', 's', 'e']
  
  for i in range(4):

    for j in range(2):
      cat_images.append(cat_sheet.get_image(j*512, i*256, 512, 256))
      cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (180, 90))
  
  #for i in range(len(directions)):
    #for j in range(9):
      #man_images[directions[i] + str(j)] = #man_sheet.get_image(j*64, i*64, 64, 64)

def main():
  get_images()
  cat = Cat((-90, random.randint(50, height - 50)), cat_images)
  #player = Player((width // 2, height // 2), man_images)

  while True:
    clock.tick(60)

    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    
    #keys = pygame.key.get_pressed()
    #if keys[K_UP]:
      #player.up()
    #if keys[K_DOWN]:
      #player.down()
    #if keys[K_LEFT]:
      #player.left()
    #if keys[K_RIGHT]:
      #player.right()
    
    #player.update()
    cat.update()
    

    #screen.fill(color)
    screen.blit(background_image, [0, 0])
    cat.draw(screen)

    #player.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
  main()