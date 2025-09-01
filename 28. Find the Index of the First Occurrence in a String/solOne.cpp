#include <iostream>
#include <vector>
#include <string>

int main(){
    std::string needle = "sad";
    std::string haystack = "sadbutsad";


    for(int i=0;i<haystack.size();i++)
    {
        if(haystack.substr(i,needle.size())==needle){
            std::cout<< i;
            break;
        }
    }
    return -1;
}