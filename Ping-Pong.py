from pygame import *

#Классы
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 40:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 40:
           self.rect.y += self.speed


#игровая сцена:
back = (200, 255, 255) #цвет фона 
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping-pong')
background = transform.scale(image.load('galaxy.jpg'), (600, 500))

game = True
finish = False
clock = time.Clock()
FPS = 120

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(background, (0, 0))


   display.update()
   clock.tick(FPS)
