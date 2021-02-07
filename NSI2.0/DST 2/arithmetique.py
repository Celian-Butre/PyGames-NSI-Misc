def arithmetique(k):
    for i in range(k - 1):
        print(k*(i+1) + (i+1), end = ' ; ')
    print('')

if __name__ == '__main__':
    for i in range(10):
        arithmetique(i)