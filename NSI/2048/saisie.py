#/celian
import time, sys, os, tty, termios
# pour la saisie en ligne

def saisieCaractereEnLigne():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        
def checkKeyPress():
    global turnLeft, turnRight, turnUp, turnDown
    keys = saisieCaractereEnLigne()
    
    if keys == "a":
        exit()
        
    if keys == "r":
        return (5)
        
    if keys == "q":
        return(0)
        
    if keys == "d":
        return(2)
         
    if keys == "z":
        return(1)
        
    if keys == "s":
        return(3)
    
    return(4)
#\celian
