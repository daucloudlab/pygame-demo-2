import pygame

pygame.init()


win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My PyGame demo")


x = 50
y = 50 
width = 40
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 600 - (width+speed):
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < 600 - (height+speed):
        y += speed
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    
    pygame.display.update()


pygame.quit()