import pygame

class SpriteSheet:
  def __init__(self, img_path):
    # load sprite sheet input
    self.sprite_sheet = pygame.image.load(img_path)
  
  def get_image(self, x, y, width, height):
    # create a blank image
    image = pygame.Surface([width, height])
    image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(image.get_at((0, 0)))
    return image