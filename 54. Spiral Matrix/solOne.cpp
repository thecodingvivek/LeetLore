#include <vector>
#include <iostream>
#include "../printVector/printvector.cpp"

int main(){
    std::vector<std::vector<int>> matrix = {{1,2,3,4},{5,6,7,8}};
    std::vector<int> result;
    int start=0;
    int end=0;
    int pointerh=0;
    int pointerv=0;

    bool verticalrev = false;
    bool horizontalrev = false;

    while(start==end){
        if(!horizontalrev)
        {
            result.insert(result.end(), matrix[pointerv].begin()+start, matrix[pointerv].end()-end);
            pointerh=matrix[pointerv].size()-end;
            for(int i=pointerv;i<matrix.size()-end;i++)
            {
                result.push_back(matrix[pointerv][matrix[pointerv].size()-1]);
            }
            pointerv=matrix.size()-end;
        }
        else{
            result.insert(result.end(), matrix[pointerv].rbegin()+start, matrix[pointerv].rend()-end);
            pointerh=start;
            start++;
            end++;
            for(int i=pointerv;i>=start;i--)
            {
                result.push_back(matrix[pointerv][matrix[pointerv].size()-1]);
            }
            pointerv=start;
        }
        printVector(result);
        horizontalrev=!horizontalrev;
    }


    printVector(result);
}