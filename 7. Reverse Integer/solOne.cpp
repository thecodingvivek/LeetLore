#include <iostream>
#include <vector>


int main(){
    int32_t x=123;
    int32_t rem;
    int32_t rev = 0;
    bool isNegative = x<0?true:false;
    if (isNegative) {
        if (x <= INT32_MIN) {
            return 0;
        }
    }

    x=abs(x);

    std::cout<<"hello";
    while(x!=0)
    {
        rem=x%10;
        x=x/10;
        if((INT32_MAX- rem)/10 < (rev)) return 0;
        rev=(rev*10)+rem;
    }
    return isNegative?-x:x;
}