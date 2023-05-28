#include <iostream>

int main() {
    int num, numbers[20];
    
    for (int i = 19; i >= 0; i--) {
        std::cin >> num;
        numbers[i] = num;
    }
    for (int i = 0; i < 20; i++) {
        std::cout << "N[" << i << "] = " << numbers[i] << std::endl;
    }
}
