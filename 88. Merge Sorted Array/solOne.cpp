#include <iostream>
#include <vector>
#include "../printVector/printvector.cpp"


int main(){
    std::vector<int> nums1={1,2,3,0,0,0};
    std::vector<int> nums2={2,5,6};
    int m = 3;
    int n=3;
    int firstPointer=0;
    int secondPointer = 0;


    while((secondPointer<n) && (firstPointer<nums1.size())){
        if(nums1[firstPointer]>=nums2[secondPointer] || firstPointer>=m)
        {
            nums1.erase(nums1.end()-1,nums1.end());
            nums1.insert(nums1.begin() + firstPointer, nums2[secondPointer]);
            secondPointer++;
            m++;
        }
        else{
            firstPointer++;
        }
    }
    printVector(nums1);



    return 0;
}