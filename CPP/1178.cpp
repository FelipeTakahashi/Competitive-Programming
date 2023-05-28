#include <iostream>
#include <iomanip>

int main() {
    double array[100], n;
        std::cin >> n;
    
    for (int i = 0; i < 100; i++) {
        array[i] = n;
        n /= 2.0;
    }

    for (int i = 0; i < 100; i++){
        std::cout << "N[" << i << "] = " << std::fixed << std::setprecision(4) << array[i] << std::endl;
    }
}       
