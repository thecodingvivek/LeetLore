#include <iostream>
#include <vector>
#include "../printVector/printvector.cpp"

int main(){
    std::vector<int> nums={0,0,1,1,1,2,2,3,3,4};
    int k=1;
    for(int j=1;j<nums.size();j++)
    {
        if(nums[j-1]!=nums[j])
        {
            nums[k]=nums[j];
            k++;
        }
    }
}
