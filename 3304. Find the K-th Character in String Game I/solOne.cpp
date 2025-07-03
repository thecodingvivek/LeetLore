#include <string> 
#include <cmath> 
#include <stdio.h>
#include <iostream>
using std::string;
using std::cout;
using std::endl;

class Solution {
public:
    char kthCharacter(int k) {
        string temp="";
        string str="a";
        while(str.length()<=k)
        {
            for(int j=0;j<str.length();j++)
            {
                temp+=nextChar(str[j]);
            }
            str+=temp;
            temp="";
        }

        return str[k-1];
    }

    char nextChar(char ch){
        return ch+1;
    }
};


int main() {
    Solution l;
    cout<<l.kthCharacter(5);
    return 0;
}


