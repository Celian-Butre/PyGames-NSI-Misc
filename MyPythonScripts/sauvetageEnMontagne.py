def quelleLigne(distance):
    if distance >= 0 and distance <= 170:
        return (1)
    if distance >= 170 and distance <= 470:
        distance -= 170
        return (2)
    if distance >= 470 and distance <= 970:
        distance -= 470
        return (3)
    if distance >= 970 and distance <= 1270:
        distance -= 970
        return (4)
    if distance >= 1270 and distance <= 1770:
        distance -= 1270
        return (5)
    if distance >= 1770 and distance <= 1940:
        distance -= 1770
        return (6)

def quellecoordonnée(distance, stretch):
    #lat = previous corner + ((distance/distance in stretch)*(next corner-previous corner))
    if stretch == 1:
        lat = 48.852204 + ((distance/170)*(48.851213-48.852204))
        lon = 2.299272 + ((distance/170)*(2.300967-2.299272))
        return([lat,lon])
    if stretch == 2:
        lat = 48.851213 + ((distance/300)*(48.849477-48.851213))
        lon = 2.300967 + ((distance/300)*(2.303855-2.300967))
        return([lat,lon])
    if stretch == 3:
        lat = 48.849477 + ((distance/500)*(48.852710-48.849477))
        lon = 2.303855 + ((distance/500)*(2.308517-2.303855))
        return([lat,lon])
    if stretch == 4:
        lat = 48.852710 + ((distance/300)*(48.854270-48.852710))
        lon = 2.308517 + ((distance/300)*(2.305488-2.308517))
        return([lat,lon])
    if stretch == 5:
        lat = 48.854270 + ((distance/500)*(48.851213-48.854270))
        lon = 2.305488 + ((distance/500)*(2.300967-2.305488))
        return([lat,lon])
    if stretch == 6:
        lat = 48.851213 + ((distance/170)*(48.852204-48.851213))
        lon = 2.300967 + ((distance/170)*(2.299272-2.300967))
        return([lat,lon])
    
    
while True:
    distance = int(input("distance"))
    stretch = quelleLigne(distance)
    coord = quellecoordonnée(distance, stretch)
    print (coord)