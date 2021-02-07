def populationOver(dico, n = 10000000):
    listToReturn = []
    for x in dico:
        if int(dico[x]["Population"]) > n:
            listToReturn.append((x, dico[x]["Population"]))
    return(listToReturn)

def nLargestCountries(dico, n = 50):
    listToReturn = populationOver(dico, -1)
    listToReturn = [(int(listToReturn[i][1]), listToReturn[i][0]) for i in range(len(listToReturn))]
    for i in range(len(listToReturn)-1):
        for j in range(len(listToReturn)-i-1):
            if listToReturn[j][0] > listToReturn[j+1][0]:
                listToReturn[j], listToReturn[j+1] = listToReturn[j+1], listToReturn[j]
    listToReturn.reverse()
    return(listToReturn)
    
if __name__ == "__main__":
    headingsList = ["ISO",	"ISO3", "ISO-Numeric",	"fips",	"Country",	"Capital",	"Area(in sq km)",	"Population",	"Continent",	"tld",	"CurrencyCode",	"CurrencyName",	"Phone", "Postal Code Format",	"Postal Code Regex",	"Languages",	"geonameid",	"neighbours",	"EquivalentFipsCode"]
    countries = ("countries.txt")
    with open(countries) as f:
        countriesText = f.read()
    countriesLine = countriesText.split("\n")
    CSVCountries = {}
    for i in range(len(countriesLine)):
        if len(countriesLine[i]) != 0:
            if countriesLine[i][0] != "#":
                externalDico = {}
                line = countriesLine[i].split("\t")
                for j in range(len(headingsList)):
                    externalDico[headingsList[j]] = line[j]
                CSVCountries[line[4]] = externalDico
    """            
    CSVCountries = []
    for i in range(len(countriesLine)):
        if len(countriesLine[i]) != 0:
            if countriesLine[i][0] != "#":
                CSVCountries.append(countriesLine[i].split("\t"))
    """
    #print(CSVCountries)
    #print(populationOver(CSVCountries))
    print(nLargestCountries(CSVCountries))