import pygame
import random

class Coin:
  def __init__(self):
    x = random.randint(0, 790)
    y = random.randint(0, 599)
    self.rect = pygame.Rect(x, y, 8, 8)
    self.isHidden = False