#include <iostream>
#include <iomanip>

int main() {
    double num, numbers[100];

    for (int i = 0; i < 100; i++) {
        std::cin >> num;

        if (num <= 10) {
            std::cout << "A[" << i << "] = " << std::fixed << std::setprecision(1) << num << std::endl;
        }
    }
