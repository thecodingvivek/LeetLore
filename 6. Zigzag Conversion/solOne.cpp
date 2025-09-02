#include <iostream>
#include <vector>


int main(){
    std::string s="A";
    int k=1;
    std::vector<std::string> newString(k);
    bool reverse = false;
    int subCounter = 0;
    if(s.size()<=k){}
    for(int i=0;i<s.size();i++)
    {
        newString[subCounter]+=std::string(1,s[i]);
        if (subCounter == 0) reverse = true;
        else if (subCounter == k - 1) reverse = false;
        subCounter += reverse ? 1 : -1;
    }

    for(int l=0;l<k;l++)
    {
        std::cout<<newString[l];
    }

}