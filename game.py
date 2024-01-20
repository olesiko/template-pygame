import pygame

WIDTH = 360
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
   
    
   
    pygame.draw.rect(screen,(100,50,200),[x,y,100,200])

    pygame.draw.circle(screen,colorApple,[x_APPLE,y_Apple],15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y - 100
                print("нажали на w")
            if event.key == pygame.K_s:
                y = y + 100
                print("нажали на S")
            if event.key == pygame.K_d:
                x = x + 100
                print("нажали на D")
            if event.key == pygame.K_a:
                x = x - 100
                print("нажали на A")



    pygame.display.flip()
pygame.quit()
