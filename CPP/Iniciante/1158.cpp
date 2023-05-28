#include <iostream>

int main() {
    int n, start, finish, total = 0;
        std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> start >> finish;

        total = 0;

        if (start % 2 == 0) {
            start += 1;
        }

        for (int k = 0; k < finish; k++) {
            total += start;
            start += 2;
        }
        
          std::cout << total << std::endl;
    }
    
}
