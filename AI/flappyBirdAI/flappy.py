import pygame, neat, time, os, random #imports

WIN_WIDTH, WIN_HEIGHT = 600, 800 #size of screen

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))] #list of the three bird images

PIP_EIMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png"))) #image of the pipe
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png"))) #image of the base
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png"))) # image of the background

TERM_VEL = 16

class Bird: #setup of the bird class
    IMGS = BIRD_IMGS #abreviating BIRD_IMGS in class
    MAX_ROTATION = 25 #maximum rotation angle
    ROTATION_VEL = 20 #speed of the rotation
    ANIMATION_TIME = 5 #time of the rotation
    
    def __init__(self, x, y): #function to represent the starting position of the bird
        self.x = x #the birds x position
        self.y = y #the birds y position
        self.tilt = 0 #the birds tilt
        self.tickCount = 0 #sets the last jump to right before the initiation
        self.vel = 0 #the birds velocity
        self.height = self.y #used for the tilt of the bird
        self.imgCount = 0 #to know what image of the bird to use
        self.img = self.IMGS[0] #setting the image of the bird to the first image in IMGS
        
    def jump(self): #function to simulate the jumping of the bird
        self.vel = -10.5 #velocity that goes upward in pygame
        self.tickCount = 0 #keeps in mind when the last jump was executed: right now
        self.height = self.y #keeps in mind the starting position of the jump
        
    def move(self): #function to evolve the bird from one frame to the other
        self.tickCount += 1 #adds one to the number of states since the last action
        displacement = self.vel * self.tickCount + 1.5 * self.tickCount ** 2 #calculates the displacement in between 2 states
        
        if displacement >= TERM_VEL: #checks if terminal velocity is reached
            displacement = TERM_VEL * displacement/abs(displacement) #sets it to terminal velocity in whichever direction it is going
            
        if displacement < 0: #checks if going up after a jump
            d -= 2 #makes it go up faster than it would go down, so the jump is more powerfull
            
        self.y = self.y + displacement #changes the y position by the displacement
        
        if displacement < 0 or self.y < self.height + 50: #checking if the movement is upward, or if the position is higher than the jumping point + 50
            if self.tilt < self.MAX_ROTATION: #if the tilt isn't fully tilted
                self.tilt = self.MAX_ROTATION # tilt it fully
        else: #if it is falling and 50 below the jump point
            if self.tilt > -90: #as long as it isn't vertical
                self.tilt -= ROTATION_VEL #rotate it downwards by the rotation velocity
                
    def draw(self, win): #takes care of the display
        self.imgCount += 1 #counts how many ticks have gone by
        
        if self.imgCount <= self.ANIMATION_TIME: #if the first animation has not completed
            self.img = self.IMGS[0] #image is the first image
        elif self.imgCount <= self.ANIMATION_TIME * 2: #if the first animation is completed but the second one isn't
            self.img = self.IMGS[1] #image is the second image
        elif self.imgCount <= self.ANIMATION_TIME * 3: #if the second animation is completed but the third one isn't
            self.img = self.IMGS[2] #image is the third image  
        elif self.imgCount <= self.ANIMATION_TIME * 4: #if the third animation is finished but the fourth one isn't
            self.img = self.IMGS[1] #image is the second image
        elif self.imgCount == self.ANIMATION_TIME * 4 + 1: #if the fourth animation just finished
            self.img = self.IMGS[0] #image is the first one
            self.imgCount = 0 #resets the imgCount
            
        if self.tilt <= -80: #if the bird is nosediving
            self.img = self.IMGS[1] #wings are level (second image)
            self.img_count = self.ANIMATION_TIME * 2 #resets the count to halway so that the third animation will begin when it stops nosediving
        
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt) #calls the function to rotate around center from stack overflow
        
    def get_mask(self): #in case of collision
        return (pygame.mask.from_surface(self.img)) #does something

def drawWindow(win, bird):  #draws the window              
    win.blit(BG_IMG, (0,0)) #puts the background in the background
    bird.draw(win) #calls the draw function for the bird
    pygame.display.update() #refreshes the screen
        
def blitRotateCenter(surf, image, topleft, angle): #STACK OVERFLOW CODE TO ROTATE AROUND CENTER
    """
    Rotate a surface and blit it to the window
    :param surf: the surface to blit to
    :param image: the image surface to rotate
    :param topLeft: the top left position of the image
    :param angle: a float value for angle
    :return: None
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
        
        
def main(): #main loop
    bird = Bird(200, 200) #puts a bird at 200, 200
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #initiates the window
    
    run = True #sets run to True so the while loop starts until the game is told to stop
    while run: #while's until the game is told to stop
        for event in pygame.event.get(): #checks all pygame events
            if event.type == pygame.QUIT: #if pygame is told to quit (x top corner)
                run = False #run is false so loop ends
        
        drawWindow(win, bird)
    
    pygame.quit() #pygame quits because while loop has ended
    quit() #quit the program

main()