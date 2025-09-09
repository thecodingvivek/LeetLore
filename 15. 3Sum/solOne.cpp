#include <vector>
#include <iostream>
#include "../printVector/printvector.cpp"

int getNextIndex(std::vector<int> arr,int k){
    for(int i=k+1;i<arr.size()-1;i++)
    {
        if(arr[k]!=arr[i])
        {
            std::cout<<i<<"next \n";
            return i;
        }
    }
    return -1;
}


int getBackIndex(std::vector<int> arr,int k){
    for(int i=k-1;i>=1;i--)
    {
        if(arr[k]!=arr[i])
        {
            std::cout<<i<<"back \n";
            return i;
        }
    }
    return -1;
}



int main(){
    std::vector<int> nums = {0,1,1};
    std::vector<std::vector<int>> result;
    std::sort(nums.begin(),nums.end());
    int onePointer =0;
    int twoPointer =0;
    for(int i=0;i<nums.size();i++)
    {   
        if(i!=0 && nums[i]==nums[i-1])
        {
            continue;

        }

        int t=-(nums[i]);//doubt
        onePointer=i+1;
        twoPointer=nums.size()-1;
        while (onePointer<twoPointer && (onePointer != -1 && twoPointer !=-1))
        {
            if(nums[onePointer]+nums[twoPointer]==t)
            {
                result.push_back({nums[i],nums[onePointer],nums[twoPointer]});
                onePointer=getNextIndex(nums,onePointer);
                twoPointer=getBackIndex(nums,twoPointer);
            }
            else if(nums[onePointer]+nums[twoPointer]>t){
                twoPointer--;
            }
            else{
                onePointer++;
            }
        }
    }


    for(int l=0;l<result.size();l++)
    {
        std::cout<<result[l][0]<<result[l][1]<<result[l][2]<<"\n";
    }
    return 0;
}