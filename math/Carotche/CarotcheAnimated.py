import random, time, pygame
pygame.init
width, height = 700, 800
ballSize = 20
backgroundColor = 255, 255, 255
textColor = 0, 0, 0
screen = pygame.display.set_mode((width, height))

#BACKGROUND = pygame.image.load("BACKGROUND.png")
ball = pygame.image.load("ball.png")


class Bille:
    def __init__(self):
        self.path = self.generatePath()
        self.finalBucket = self.calculateBucket()
        self.coords = (0,0) # (x,y)
        
    def generatePath(self):
        path = [(random.randint(0,1)*2)-1 for i in range(6)]
        return path
    
    def calculateBucket(self):
        bucket = 0
        for i in range(6):
            if self.path[i] == 1:
                bucket += 1
        return(bucket)
    
    def move(self):
        self.coords = (self.coords[0] + self.path[0], self.coords[1] + 1)
        
    def show(self):
        ballRect = ball.get_rect()
        ballRect = ballRect.move(self.coords[0] + (width-ballSize)//2, self.coords[1])
        screen.blit(ball, ballRect)
    
if __name__ == "__main__":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    fallingBilles = []
    bucketNumbers = [0 for i in range(7)] #7 buckets for 6 levels
    while True: #infinite running loop
        fallingBilles.append(Bille())
        for pixel in range(100): #while the billes haven't fallen a full level
            screen.fill(backgroundColor)
            for bille in range(len(fallingBilles)):
                fallingBilles[bille].move()
                fallingBilles[bille].show()
            pygame.display.flip()
            time.sleep(1/200)
        if len(fallingBilles) == 7:
            bucketNumbers[fallingBilles[0].finalBucket] += 1
            fallingBilles.pop(0)