#include <iostream>

int main() {
    int reps, n, total; 
        std::cin >> reps;
    
    for(int i = 0; i < reps; i++) {
        std::cin >> n;

        total = 0;
        for (int j = 1; j < n; j++) {
            if (n % j == 0) {
                total += j;
            }
        }

        if (total == n) {
            std::cout << n << " eh perfeito" << std::endl;
        }
        else {
            std::cout << n << " nao eh perfeito" << std::endl;
        }
    }
}
