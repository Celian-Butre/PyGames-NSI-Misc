# DST2 : exo bonus arithmétique

k = int(input("Saisir un entier naturel k : "))

print("Les entiers non nuls dont le quotient et le reste dans la division euclidienne par k sont égaux sont :")
for n in range(1, k**2  ) :
    if ( n//k == n % k ) :
        print(n)

print("On constate, en incluant le cas trivial n=0*k+0, que ce sont les entiers de la forme n = q(k+1), où 0 < q < k-1 (ce qui se montre facilement à partir de n=qk+r avec q=r)")
