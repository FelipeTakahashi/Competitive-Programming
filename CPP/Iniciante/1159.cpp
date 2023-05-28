#include <iostream>

int main() {
    int n, total; 
    while (true) {
        std::cin >> n;

        if (n == 0) {
            return 0;
        }

        if (n % 2 != 0) {
            n += 1;
        }

        total = 0;
        for (int i = 0; i < 5;i++) {
            total += n;
            n += 2;
        }

        std::cout << total << std::endl;
    }
}
