#include <iostream>

int main() {
    int number, numbers[10];
        std::cin >> number;
    
    for(int i = 0; i < 10; i++) {
        numbers[i] = number;
        number *= 2;
    }

    for(int j = 0; j < 10; j++) {
        std::cout << "N[" << j << "] = " << numbers[j] << std::endl;
    }
}
