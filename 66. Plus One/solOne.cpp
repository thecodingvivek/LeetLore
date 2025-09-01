#include <iostream>
#include <vector>
#include <cmath>

int main(){
    std::vector<int> digits={0};
    int sum=0;
    int carry=1;
    int tempsum=0;
    for(int i=digits.size()-1;i>=0;i--)
    {
        tempsum=digits[i]+carry;
        if(tempsum>=10)
        {
            digits[i] = (tempsum)%10;
            carry = (tempsum)/10;
        }
        else{
            digits[i]=tempsum;
            carry=0;
        }
    }

    if(carry!=0)
    {
        digits.insert(digits.begin(),carry);
    }


    for (int j=0;j<digits.size();j++)
    {
        std::cout<<digits[j];
    }



    
}