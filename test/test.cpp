#include <iostream>
#include <vector>
#include "../printVector/printvector.cpp"


int main(){
    std::vector<int> nums1={1,2,3};
    nums1.insert(nums1.begin()+1,9);
    printVector(nums1);
    
}