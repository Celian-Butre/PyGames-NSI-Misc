def approxRacine(a, n):
    closest = a
    save = 0
    for i in range(a + 1):
        if closest > abs(a-i**2):
            closest = abs(a-i**2)
            save = i
    
    save2 = save
    if save2 **2 > a:
        save2 -= 1
    save3 = save2
    closest = abs(a-save2**2)
    for i in range((10**n) +1):
        if closest > abs(a-(save2+(i/10**n))**2):
            closest = abs(a-(save2+(i/10**n))**2)
            save3 = save2 + i/10**n
    return(save3)
    
if __name__ == '__main__':
    print(approxRacine(1003, 5))