#include <iostream>
#include "jeu_de_la_vie_func.hpp"
#include <vector>
int main(){
    int width = 8;
    int height = 8;
    std::vector<std::vector<int>> matrice = initiateMatrice(width, height);
    matrice[3][4] = 1;
    printMatrice(matrice, width, height);
}
