#include <iostream>
#include <cstring>
#include <unordered_map>
#include <string>

int main(){
    std::cout<<"enter something : \n";

    std::string s = "VII";
    std::unordered_map<std::string,int> romanMap;
    romanMap = {{"I", 1},{"IV",4},{"V",5},{"IX",9},{"X",10},{"XL",40},{"L",50},{"C",100},{"D",500},{"M",1000},{"XC",90},{"CD",400},{"CM",900}};

    int counter=0;
    int sum=0;
    while(counter < s.length())
    {
        if(counter < s.length()-1 && romanMap.find(s.substr(counter,2)) != romanMap.end()){
            sum+=romanMap[s.substr(counter,2)];
            counter+=2;
        }
        else{
            sum+=romanMap[s.substr(counter,1)];
            counter+=1;
        }
    }
    std::cout<<"sum : "<<sum;

    return 0;
}