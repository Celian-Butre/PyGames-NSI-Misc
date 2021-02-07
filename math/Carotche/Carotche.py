import random
import matplotlib.pyplot as plt

def simul_une_bille(h):
    droite = 0
    for i in range(h):
        droite += random.randint(0,1)
    return(droite)

def simul_N_billes(N,h):
    planche = [0 for i in range(h+1)]
    for i in range(N):
        planche[simul_une_bille(h)] += 1
    return(planche)

if __name__ == "__main__":
    plt.bar(range(7), simul_N_billes(500,6))
    plt.show()