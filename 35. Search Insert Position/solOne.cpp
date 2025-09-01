#include <iostream>
#include <vector>

int main(){
    std::vector<int> nums={1,3,5,6};
    int target = 7;
    int min=0;
    int max= nums.size()-1;
    int index;

    while(min<=max){
        index=min+(max-min)/2;
        if(nums[index]==target)
        {
            break;
        }

        if(nums[index]>target){
            max=index-1;
        }
        else if(nums[index]<target){
            min=index+1;
        }
    }
    
    return 0;
}