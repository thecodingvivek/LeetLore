#include <iostream>
#include <vector>
#include <string>

// Function to print vector of ints
void printVector(const std::vector<int>& vec) {
    for (const int& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

// Function to print vector of strings
void printVector(const std::vector<std::string>& vec) {
    for (const std::string& elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}