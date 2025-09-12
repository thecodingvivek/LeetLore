#include <vector>
#include <iostream>
#include <unordered_map>
#include "../printVector/printvector.cpp"


int main(){
    std::vector<int> nums={1,-1,1,1,1,1};
    int k=3;
    std::unordered_map<int,int> prefixCount = {{0,1}};
    int sum=0;
    int req=0;
    int result=0;


    for(int i=0;i<nums.size();i++){
        sum+=nums[i];
        req=sum-k;
        if(prefixCount[req])
        {
            result+=prefixCount[req];
        }

        if(prefixCount[sum])
        {
            prefixCount[sum]+=1;
        }
        else{
            prefixCount[sum]=1;
        }

    }

    
}