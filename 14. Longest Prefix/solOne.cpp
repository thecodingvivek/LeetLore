#include <iostream>
#include <vector>
#include <algorithm>


int main(){
    std::vector<std::string> strs = {"flower","flower","flower"};
    std::sort(strs.begin(),strs.end());
    int counter = 0;
    int endCounter=strs.size()-1;
    int substrLength = 1;
    std::string preFix = "";

    if(strs[counter].substr(0,substrLength) != strs[endCounter].substr(0,substrLength))
    {
        std::cout<<"no common prefix";
        return 0;
    }

    while ((strs[counter].substr(0,substrLength) == strs[endCounter].substr(0,substrLength))&&(substrLength<=strs[0].size()))
    {
        std::cout<<substrLength;
        substrLength+=1;
    }
    
    std::cout<<strs[0].substr(0,substrLength-1);
    return 0;
}