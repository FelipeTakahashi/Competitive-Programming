#include <iostream>
#include <iomanip>

int main() {
    char operation;
        std::cin >> operation;

    double M[12][12], sum = 0;
        for (int row = 0; row < 12; row++) {
            for (int col = 0; col < 12; col++) {
                std::cin >> M[row][col];
                if (col < row and col + row < 11) {
                    sum += M[row][col];
                }
            }
        }

    if (operation == 'S') {
        std::cout << std::fixed << std::setprecision(1) << sum << std::endl;
    }
    else if (operation == 'M') {
        std::cout << std::fixed << std::setprecision(1) << sum/30.0 << std::endl;
    }
}
