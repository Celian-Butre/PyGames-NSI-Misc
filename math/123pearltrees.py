def cahier():
    u = 16000
    n = 0
    while u > 2000:
        n += 1
        u -= u*15/100
        
    return(n+2018)
    
if __name__ == '__main__':
    print(cahier())