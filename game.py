import pygame
import random

WIDTH = 360
width_player = 50
height_player = 50
HEIGHT = 480
FPS = 30
y = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
x = 0
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
colorApple = (255,150,100)
x_APPLE = 100
y_Apple = 200
running = True
red = 0
green = 0
blue = 0
isRedMax = False
while running:
    clock.tick(FPS)
    screen.fill((red,green,blue))
    green = green + 1
  
    if green == 255:
        green = 0
   
    
   
    pygame.draw.rect(screen,(100,50,200),[x,y,width_player,height_player])

    pygame.draw.circle(screen,colorApple,[x_APPLE,y_Apple],15)

    
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         y = y - 100
        #         print("нажали на w")
        #     if event.key == pygame.K_s:
        #         y = y + 100
        #         print("нажали на S")
        #     if event.key == pygame.K_d:
        #         x = x + 100
        #         print("нажали на D")
        #     if event.key == pygame.K_a:
        #         x = x - 100
        #         print("нажали на A")
    
    if ((x<x_APPLE+15 and x_APPLE<x-15 + width_player)and(y<y_Apple+15 and y_Apple<y-15 + height_player)):
        width_player += 10
        x_APPLE = random.randint(0,WIDTH)
        y_Apple = random.randint(0,WIDTH)
        pygame.draw.circle(screen,colorApple,[x_APPLE,y_Apple],15)





    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 10
    if keys[pygame.K_s]:
        y += 10
    if keys[pygame.K_a]:
        x -= 10
    if keys[pygame.K_d]:
        x += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if (x<0 or x>WIDTH-50):
        running = False
        pass
        
    pygame.display.flip()
pygame.quit()
