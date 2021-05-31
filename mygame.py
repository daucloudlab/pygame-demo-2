import pygame

pygame.init()


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My PyGame demo")

clock = pygame.time.Clock()

walkRight = [
    pygame.image.load('game/right_1.png'), 
    pygame.image.load('game/right_2.png'), 
    pygame.image.load('game/right_3.png'), 
    pygame.image.load('game/right_4.png'), 
    pygame.image.load('game/right_5.png'), 
    pygame.image.load('game/right_6.png')
    ] 

walkLeft = [
    pygame.image.load('game/left_1.png'), 
    pygame.image.load('game/left_2.png'), 
    pygame.image.load('game/left_3.png'), 
    pygame.image.load('game/left_4.png'), 
    pygame.image.load('game/left_5.png'), 
    pygame.image.load('game/left_6.png') 
    ]

playerStand = pygame.image.load('game/idle.png')
bg = pygame.image.load('game/bg.jpg')

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False 
jumpCount = 10

left = False 
right = False 
animCount = 0 

def drawWindow():
    global animCount

    win.blit(bg, (0,0))
    
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    
    
    
    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - (width+speed):
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:    
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1 
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()