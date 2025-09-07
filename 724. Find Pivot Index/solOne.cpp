#include <vector>
#include <iostream>


int main(){
    std::vector<int> nums = {1,2,3};
    int sum =0;
    int prevSum = 0;
    for(int i=0;i<nums.size();i++)
    {
        sum+=nums[i];
    }
    for(int k=0;k<nums.size();k++)
    {
        if((sum-prevSum-nums[k]) == prevSum)
        {
            std::cout<<nums[k];
        }
        prevSum+=nums[k];
    }

    return 0;
}