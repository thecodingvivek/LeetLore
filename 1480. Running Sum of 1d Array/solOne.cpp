#include <iostream>
#include <vector>
#include "../printVector/printvector.cpp"


int main(){
    std::vector<int> nums = {1,2,3,4};
    std::vector<int> runningSum(nums.size());
    int prevSum = 0;

    for(int i=0;i<nums.size();i++)
    {
        prevSum+=nums[i];
        runningSum[i]=prevSum;
    }


    return 0;
}