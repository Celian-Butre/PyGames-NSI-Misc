#include <iostream>
#include <vector>

std::vector<std::vector<int>> initiateMatrice(int width, int height){
    std::vector<std::vector<int>> matrice;
    //for (int i = 0; i < height; i++){
      //  std::vector<int> tempVect;
        //for (int j = 0; j < width; j++){
          //  tempVect.push_back(0);
        //}
        //matrice.push_back(tempVect);    
    //}
	for (int i = 0; i < height; i++)
	{
		// construct a vector of ints with given default value
		std::vector<int> v;
		for (int j = 0; j < width; j++)
			v.push_back(0);
	
		// push back above one-dimensional vector
		matrice.push_back(v);
	}

}

void printMatrice(std::vector<std::vector<int>> matrice, int width, int height){
    for (int i = 0; i < height; i++){
        for (int j = 0; j < width; j++){
            std::cout << matrice[i][j];
            //if (matrice[i][j] == 0){
            //    std::cout << "0";
            //}
            //if (matrice[i][j] == 1){
            //    std::cout << "1";
            //}
        }
        std::cout << "\n";
    }
}