#include <iostream>
#include <iomanip>

int main() {
    int where;
        std::cin >> where;

    char operation;
        std::cin >> operation;
    
    float M[12][12], value, answer = 0;

        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 12; j++) {
                std::cin >> value;
                M[i][j] = value;

                    if (j == where) {
                            answer += value;
                    }
            }
        }
    if (operation == 'S') {
        std::cout << std::fixed << std::setprecision(1) << answer << std::endl;
    }
    else if (operation == 'M') {
        std::cout << std::fixed << std::setprecision(1) << answer/12.0 << std::endl;
    }
}
