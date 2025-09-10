#include <iostream>
#include <vector>
#include "../printVector/printvector.cpp"
//beats 100


int main(){
    std::vector<int> nums = {-1,1,0,-3,3};
    int p1=1;
    int p2=1;
    int n=nums.size();
    std::vector<int> output(n,1);


    for(int i=0;i<n;i++)
    {
        output[i]*=p1;
        p1*=nums[i];
        int j=n-i-1;
        output[j]*=p2;
        p2*=nums[j];
    }
}
