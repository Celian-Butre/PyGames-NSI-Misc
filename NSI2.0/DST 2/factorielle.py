def facto_ite(n):
    res = 1
    for i in range(n):
        res = res*(i+1)
    return(res)

def facto_recu(n):
    if n == 0:
        return(1)
    return(n * facto_recu(n-1))

if __name__ == '__main__':
    for i in range(10):
        print(facto_ite(i), facto_recu(i))