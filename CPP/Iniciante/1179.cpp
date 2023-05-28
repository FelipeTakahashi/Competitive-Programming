#include <iostream>

int main() {
    int even[5], odd[5], number, even_counter = 0, odd_counter = 0;
    
    for (int i = 0; i < 15; i++) {
        std::cin >> number;
            if (number % 2 == 0) {
                even[even_counter] = number;
                even_counter += 1;
            }
            else {
                odd[odd_counter] = number;
                odd_counter += 1;
            }
        
            if (even_counter == 5) {
                for (int j = 0; j < 5; j++) {
                    std::cout << "par[" << j << "] = " << even[j] << std::endl;
                    even_counter = 0;
                }
            }
            if (odd_counter == 5) {
                for (int j = 0; j < 5; j++) {
                    std::cout << "impar[" << j << "] = " << odd[j] << std::endl;
                    odd_counter = 0;
                }
            }
    }

    for (int j = 0; j < odd_counter; j++) {
        std::cout << "impar[" << j << "] = " << odd[j] << std::endl;
    }

    for (int j = 0; j < even_counter; j++) {
        std::cout << "par[" << j << "] = " << even[j] << std::endl;
    }
}
