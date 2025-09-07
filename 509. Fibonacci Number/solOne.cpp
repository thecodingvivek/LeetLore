#include <iostream>

int main(){
    int n =0;
    int fprev = 0;
    int sprev = 1;
    int tem=0;
    if(n==0) return 0;
    for(int i=2;i<n;i++)
    {
        tem = sprev;
        sprev+=fprev;
        fprev=tem;
    }
    return 0;
}