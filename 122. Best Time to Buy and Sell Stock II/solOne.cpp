#include <iostream>
#include <vector>


int main(){
    std::vector<int> prices = {7,1,5,3,6,4};
    int profit =0;

    for(int i=0;i<prices.size()-1;i++)
    {
        if(prices[i+1]>prices[i])
        {
            profit+=(prices[i+1]-prices[i]);
        }
    }

    std::cout<<profit;
    return 0;
}