import time, pygame, sys, random
pygame.init
width, height = 800, 600
backgroundColor = 255, 255, 255
snakeSpeed = [0, 0]
pygame.display.set_caption("Snake")

score = 0

clone = []
cloneRect = []

noRight = False
noLeft = False
noUp = False
noDown = False

turnRight = False
turnLeft = False
turnUp = False
turnDown = False

apple = pygame.image.load("Apple.png")
appleRect = apple.get_rect()

snakeHead = pygame.image.load("black_square.png")
snakeHeadRect = snakeHead.get_rect()

screen = pygame. display.set_mode((width, height))
dead = False

hit = False

screen.blit(snakeHead, snakeHeadRect)
snakeHeadRect = snakeHeadRect.move(random.randint(4,(width//20)-5)*20,random.randint(4,(height//20)-5)*20)

screen.blit(apple, appleRect)
appleRect = appleRect.move(random.randint(4,(width//20)-5)*20,random.randint(4,(height//20)-5)*20)

pygame.display.flip()

def setupclone ():
    global score
    for i in range (5):
        clone[score-1][2].append(1)
    if score-1 > 0:   
        for i in range((score-1)*5):
            clone[score-1][2].append(clone[score-2][2][i])
            clone[score-1].append([])
        clone[score-1][3].append(clone[score-2][1].x)
        clone[score-1][3].append(clone[score-2][1].y)
    if score-1 == 0:
        clone[score-1].append([])
        clone[score-1][3].append(snakeHeadRect.x)
        clone[score-1][3].append(snakeHeadRect.y)
    clone[score-1][1] = clone[score-1][1].move(0, 0)


def cloneslide(i):
    global snakeSpeed, score
    if clone[i][2][0] != 1:
        clone[i][1] = clone[i][1].move(clone[i][2][0])
    for j in range (((i+1)*5)-1):
        clone[i][2][j] = clone[i][2][j+1] 
        
def teleportTo():
    
    clone[score-1][1] = clone[score-1][1].move(clone[score-1][3][0], clone[score-1][3][1])

def move(): 
    global noRight, noLeft, noUp, noDown, turnRight, turnLeft, turnUp, turnDown, snakeSpeed
    # control the player
    
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_LEFT] or AiLeft == True) and noLeft == False:
        turnLeft = True
        
    if (keys[pygame.K_RIGHT] or AiRight == True) and noRight == False:
        turnRight = True
         
    if (keys[pygame.K_UP] or AiUp == True) and noUp == False:
        turnUp = True
        
    if (keys[pygame.K_DOWN] or AiDown == True) and noDown == False:
        turnDown = True       
            
    if turnLeft == True and snakeHeadRect.x%20 == 0 and snakeHeadRect.y%20 == 0:
        turnLeft = False
        noLeft = False
        noRight = True
        noUp = False
        noDown = False
        snakeSpeed = [-4, 0]   
        
    if turnRight == True and snakeHeadRect.x%20 == 0 and snakeHeadRect.y%20 == 0:
        noLeft = True
        noRight = False
        noUp = False
        noDown = False
        turnRight = False
        snakeSpeed = [4, 0]
    
    if turnUp == True and snakeHeadRect.x%20 == 0 and snakeHeadRect.y%20 == 0:
        noLeft = False
        noRight = False
        noUp = False
        noDown = True
        turnUp = False
        snakeSpeed = [0, -4]
    
    if turnDown == True and snakeHeadRect.x%20 == 0 and snakeHeadRect.y%20 == 0:
        noLeft = False
        noRight = False
        noUp = True
        noDown = False
        turnDown = False
        snakeSpeed = [0, 4]
 
    return (snakeSpeed)




while dead == False:
    AiLeft = True
    AiRight = False
    AiDown = False
    AiUp = False
    screen.fill (backgroundColor)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.blit(snakeHead, snakeHeadRect)
    screen.blit(apple, appleRect)
    
    # kill the player        
    if snakeHeadRect.left < 0  or snakeHeadRect.right > width or snakeHeadRect.top < 0  or snakeHeadRect.bottom > height:
        hit = True
        
    for i in range (1, score):
        if ((snakeHeadRect.x == clone[i][1].x) and (snakeHeadRect.y == clone[i][1].y)):
            hit = True
            
    
    snakeSpeed = move()
    
    if hit == False:
        snakeHeadRect = snakeHeadRect.move(snakeSpeed)

    for i in range (score):
        if hit == False:
            cloneslide(i)
        clone[i][2][((i+1)*5)-1] = snakeSpeed
        
    # apple collision
    if appleRect.x == snakeHeadRect.x and appleRect.y == snakeHeadRect.y:
        score += 1
        appleRect = appleRect.move(random.randint(0,(width//20)-1)*20 - appleRect.x ,random.randint(0,(height//20)-1)*20 - appleRect.y)
        clone.append([])
        clone[score-1].append(pygame.image.load("black_square.png"))
        clone[score-1].append(clone[score-1][0].get_rect())
        clone[score-1].append([])
        setupclone()
        teleportTo()
        

        
    #tail
    for i in range (score):
        screen.blit(clone[i][0], clone[i][1])
    
    time.sleep(10 / 1000)
    pygame.display.flip()

# inputs up down left right
# parameters tailpos and applepos and headpos