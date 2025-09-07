#include <vector>
#include <iostream>


int main(){
    std::vector<std::vector<int>> result = {{1},{1,1}};
    int numRows =5;
    if(numRows==2)
    {

    }
    else if(numRows==1){
        
    }
    std::vector<int> temp;
    for(int i=2;i<numRows;i++)
    {
        temp.push_back(1);
        for(int j=1;j<i;j++)
        {
            temp.push_back(result[i-1][j-1]+result[i-1][j]);
        }
        temp.push_back(1);
        result.push_back(temp);
        temp.clear();
    }


    for(int t=0;t<result.size();t++)
    {
        for(int k=0;k<result[t].size();k++)
        {
            std::cout<<result[t][k]<<" ";
        }
        std::cout<<"\n";

    }


    return 0;
}