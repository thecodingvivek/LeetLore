#include <vector>
#include <iostream>
#include "../printVector/printvector.cpp"

int main(){
    std::vector<std::vector<int>> matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    std::vector<int> result;
    int start=0;
    int end=0;
    int pointerh=0;
    int pointerv=0;


    ///some random shit
    //every day random 
    //another day same shit
    bool verticalrev = false;
    bool horizontalrev = false;

    while(start==end){
        if(!horizontalrev)
        {
            std::cout<<"joo";
            result.insert(result.end(), matrix[pointerv].begin()+start, matrix[pointerv].end()-end);
            pointerh=matrix[pointerv].size()-end;
            for(int i=pointerv+1;i<matrix.size()-end;i++)
            {
                result.push_back(matrix[i][matrix[pointerv].size()-1]);
            }
            std::cout<<"got this";
            pointerv=matrix.size()-end;
        }
        else{
            std::cout<<"koo";
            result.insert(result.end(), matrix[pointerv].rbegin()+start, matrix[pointerv].rend()-end);
            printVector(result);
            std::cout<<"lol";
            pointerh=start;
            start++;
            end++;
            for(int i=pointerv-1;i>=start;i--)
            {
                result.push_back(matrix[i][matrix[pointerv].size()-1]);
            }
            pointerv=start;
        }
        printVector(result);
        horizontalrev=!horizontalrev;
    }


}