import pygame
from pygame.locals import *
from coin import Coin

pygame.display.init()

screen = pygame.display.set_mode((800,600))
player = pygame.Rect(400, 300, 15, 15)
clock = pygame.time.Clock()

speed_x = 0
speed_y = 0

white = pygame.Color(255, 255, 255)
darkblue = pygame.Color(0, 150, 255)
black = pygame.Color(0, 0, 0)
yellow = pygame.Color(200, 255, 0)
blue = pygame.Color(0, 255, 230)

def move_up():
  global speed_y
  speed_y = 10

def move_down():
  global speed_y
  speed_y = -10

def move_right():
  global speed_x
  speed_x = 10

def move_left():
  global speed_x
  speed_x = -10

def movement_loop():
  global speed_x, speed_y, player
  player.centerx += speed_x
  player.centery -= speed_y
  speed_x = 0
  speed_y = 0

score = 0

list_of_coins = []

for i in range(100):
  list_of_coins.append(Coin())

def collision_loop():
  global list_of_coins, player, score

  for coin in list_of_coins:
    if player.colliderect(coin.rect) and coin.isHidden == False:
      coin.isHidden = True
      score += 1

def render_coin_loop(screen):
  global list_of_coins, yellow

  for coin in list_of_coins:
    if coin.isHidden == False:
      screen.fill(yellow, coin.rect)

pygame.font.init()
FONT = pygame.font.SysFont("freeserif", 36)

def main():
  global FONT, score
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit(0)
      
      pygame.event.pump()

      key = pygame.key.get_pressed()
      if key[K_UP]:
        move_up()
      if key[K_RIGHT]:
        move_right()
      if key[K_DOWN]:
        move_down()
      if key[K_LEFT]:
        move_left()
      
      movement_loop()
      collision_loop()
      
      clock.tick(60)
      screen.fill(blue)
      screen.fill(darkblue, player)

      render_coin_loop(screen)
      
      screen.blit(
        FONT.render('Score: ' + str(score), True, white), (20, 80)
      )

      seconds = int(pygame.time.get_ticks() / 1000)
      screen.blit(
        FONT.render('Time: ' + str(seconds), True, white), (640, 80)
      )

      pygame.display.flip()

main()