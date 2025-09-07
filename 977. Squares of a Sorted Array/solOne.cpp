#include <iostream>
#include <vector>


#include "../printVector/printvector.cpp"


int main(){
    std::vector<int> nums = {-4,-1,0,3,10};
    std::vector<int> negArr;
    std::vector<int>postArr;
    for(int i=0;i<nums.size();i++)
    {
        if(nums[i]<0)
        {
            nums[i]*=(nums[i]);
            negArr.push_back(nums[i]);
        }
        else{
            nums[i]*=(nums[i]);
            postArr.push_back(nums[i]);
        }
    }
    printVector(negArr);
    printVector(postArr);

    int i =0;
    int j = negArr.size()-1;
    int k=0;

    while (i<postArr.size() && j>=0)
    {
        if(postArr[i]<negArr[j])
        {


            nums[k]=postArr[i];
            i++;
        }
        else{
            nums[k]=negArr[j];
            j--;
        }
        k++;
    }


    while(i<postArr.size())
    {
        nums[k]=postArr[i];
        i++;
        k++;
    }

    while(j>=0)
    {
        nums[k]=negArr[j];
        j--;
        k++;
    }

    printVector(nums);
    

    

    return 0;
}