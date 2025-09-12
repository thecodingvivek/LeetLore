#include <vector>
#include <iostream>
#include "../printVector/printvector.cpp"

int main(){
    std::vector<int> arr={2,1,3};
    int pivot=0;
    for(int i=1;i<arr.size();i++)
    {
        if(arr[i-1]<=arr[i])
        {
            pivot=i;
            break;
        }
    }

    if(!pivot)
    {

    }
    else{

    }

    std::cout<<pivot<<"\n";

    std::sort(arr.begin()+pivot,arr.end(),std::greater<int>());


    printVector(arr);

}