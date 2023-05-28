#include <iostream>
#include <iomanip>

int main() {
    char operation;
        std::cin >> operation;

    double M[12][12], value, answer = 0;
        for (int row = 0; row < 12; row++) {
            for (int column = 0; column < 12; column++) {
                std::cin >> value;
                M[row][column] = value;
                    if (row > column) {
                        answer += value;
                    }
            }
        }
    
    if (operation == 'S') {
        std::cout << std::fixed << std::setprecision(1) << answer << std::endl;
    }

    else if (operation == 'M') {
        std::cout << std::fixed << std::setprecision(1) << answer/66.0 << std::endl;
    }
    
}
