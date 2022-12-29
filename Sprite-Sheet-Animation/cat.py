import pygame, random

class Cat(pygame.sprite.Sprite):
  def __init__(self, pos, images):
    super().__init__()
    self.images = images
    self.image = images[0]
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = [12, 0]

  def update(self):
    frame = pygame.time.get_ticks() // 60 % 8
    self.image = self.images[frame]
    self.rect.move_ip(self.speed)
    if self.rect.left > pygame.display.Info().current_w:
      self.rect.right = 0
      self.rect.centery = random.randint(50, pygame.display.Info().current_h-50)

  def draw(self, screen):
    screen.blit(self.image, self.rect)