#include <iostream>
#include <vector>

int main(){
    std::vector<int> nums={3,2,2,3};
    int val = 2;
    int k=0;
    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]!=val)
        {
            nums[i] = nums[k];
            k++;
        }
    }
    return 0;
}