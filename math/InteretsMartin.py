import time, pygame, sys, random
black = 0,0,0

while True:
    debut = float(input   ("combien d'argent avez vous dans votre capitale:              "))
    fin = float(input     ("jusqu'à combien voulez vous allez:                           "))
    interets = float(input("quelle est le taux d'intérets:                               "))
    annees = 0
    pygame.init()
    screen = pygame. display.set_mode((800, 600))
    current = debut
    while current < fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        annees += 1
        
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)  
        textannees = font.render(("Années: " + str(annees)), True, black)
        textanneesRect = textannees.get_rect()
        textanneesRect = textanneesRect.move(100, 100)
        screen.blit(textannees, textanneesRect)
        
        textcapital = font.render(("Capital: "), True, black)
        textcapitalRect = textcapital.get_rect()
        textcapitalRect = textcapitalRect.move(50, 200)
        screen.blit(textcapital, textcapitalRect)
        
        textcurrent = font.render((str(current//1)), True, black)
        textcurrentRect = textcurrent.get_rect()
        textcurrentRect = textcurrentRect.move(200, 200)
        screen.blit(textcurrent, textcurrentRect)
        pygame.display.flip()
        
        time.sleep(0.5)
        nextYear = current*interets
        current = nextYear
        
        texttimes = font.render(("X"), True, black)
        texttimesRect = texttimes.get_rect()
        texttimesRect = texttimesRect.move(300, 200)
        screen.blit(texttimes, texttimesRect)
        
        textInterest = font.render(str(interets), True, black)
        textInterestRect = textInterest.get_rect()
        textInterestRect = textInterestRect.move(400, 200)
        screen.blit(textInterest, textInterestRect)
        pygame.display.flip()
        time.sleep(1)  
        
        textEgal = font.render("=", True, black)
        textEgalRect = textEgal.get_rect()
        textEgalRect = textEgalRect.move(500, 200)
        screen.blit(textEgal, textEgalRect)
        
        textNextYear = font.render(str(nextYear//1), True, black)
        textNextYearRect = textNextYear.get_rect()
        textNextYearRect = textNextYearRect.move(600, 200)
        screen.blit(textNextYear, textNextYearRect)
        pygame.display.flip()
        
        time.sleep(1)
        
        x = 600
        while x >= 200:
            screen.fill((255,255,255))
            font = pygame.font.Font('freesansbold.ttf', 30)  
            textannees = font.render(("Années: " + str(annees)), True, black)
            textanneesRect = textannees.get_rect()
            textanneesRect = textanneesRect.move(100, 100)
            screen.blit(textannees, textanneesRect)
            
            textcapital = font.render(("Capital: "), True, black)
            textcapitalRect = textcapital.get_rect()
            textcapitalRect = textcapitalRect.move(50, 200)
            screen.blit(textcapital, textcapitalRect)
            
            textcurrent = font.render((str(current//1)), True, black)
            textcurrentRect = textcurrent.get_rect()
            textcurrentRect = textcurrentRect.move(x, 200)
            screen.blit(textcurrent, textcurrentRect)
            
            pygame.display.flip()
            time.sleep(1/40)
            x -= 5
            
        
                                      
        
        time.sleep(1)
        
    print("Après ", annees, " années: ", debut, " dépasse ", fin, " et devient ", current, "!")