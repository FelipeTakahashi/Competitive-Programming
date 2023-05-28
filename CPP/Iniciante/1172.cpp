#include <iostream>

int main() {

    int num, numbers[10];

        for(int i = 0; i<10; i++) {
            std::cin >> num;
            if(num <= 0) {
                numbers[i] = 1;
            } else {
                numbers[i] = num;
            }
        }
    
        for(int i = 0; i<10; i++) {
            std::cout << "X[" << i << "] = " << numbers[i] << std::endl;
        }
}
