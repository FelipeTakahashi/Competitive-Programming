#include <iostream>

int main() {
    int number, higher;
        std::cin >> number;

    higher = number - 1;
    while (higher <= number) {
        std::cin >> higher;
    }

    int total = 0, counter = 0;
    while (total < higher) {
        total += number;
        number++;
        counter += 1;
    }
    
    std::cout << counter << std::endl;
}
