// pièces dans le désordre
let coins = [1, 0.01, 0.5, 0.02, 0.1, 0.2, 2, 0.05];

//tri par séléction décroissant des pièces
for (let i = 0; i < coins.length; i++) {
    let maxValue = coins[i];
    let maxValuePlace = i;
    for (let j = 0; j < coins.length - i; j++) {
        if (coins[i+j] > maxValue) {
            maxValue = coins[i+j];
            maxValuePlace = [i+j];
        };
    };
    coins[maxValuePlace] = coins[i];
    coins[i] = maxValue;
};

// valeur à changé directement dans le code
let moneyToReturn = 2.76;

// modification si la somme n'est pas purement en centimes
if (moneyToReturn  - (Math.round(moneyToReturn*100) / 100) !== 0) {
    moneyToReturn = (Math.ceil(moneyToReturn*100) / 100);
    console.log('Il est impossible de payer une valeur si précise, vous allez donc payer '+ moneyToReturn + '€');
};
let moneyToReturnCopy = moneyToReturn;

//algo gourmand
let coinsToPay = [];
let biggestCurrencyIndex = 0;
let lastIndex = (coins.length-1)

while (moneyToReturn >= coins[lastIndex]) {
    if (moneyToReturn >= coins[biggestCurrencyIndex]) {
        moneyToReturn = (Math.round(100 * (moneyToReturn - coins[biggestCurrencyIndex])) / 100);
        coinsToPay.push(coins[biggestCurrencyIndex]);
    };
    if (moneyToReturn < coins[biggestCurrencyIndex]) {
        biggestCurrencyIndex++;
    };
};    

//retourn les pièces à payer
console.log('Les pièces a utiliser pour payer ' + moneyToReturnCopy + '€ sont:');
for (i = 0; i < coinsToPay.length; i++) {
    console.log(coinsToPay[i]);
};