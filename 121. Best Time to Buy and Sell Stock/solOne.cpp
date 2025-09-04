#include <iostream>
#include <vector>



int main(){
    std::vector<int> prices={7,1,5,3,6,4};
    int minprice = INT_MAX;
    int profit = 0;
    for(int i = 0;i<prices.size();i++)
    {
        minprice =std::min(minprice,prices[i]);
        profit = std::max(profit,prices[i]-minprice);
    }


    return profit;

}
