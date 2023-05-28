#include <iostream>

int main() {
    int reps, years, a, b;
        std::cin >> reps;   
    double rate_a, rate_b;

    for (int i = 0; i < reps; i++) {
        std::cin >> a >> b >> rate_a >> rate_b;
        
        years = 0;

        while(a <= b && years <= 100) {
            a += (a * rate_a)/100;
            b += (b * rate_b)/100;
            years += 1;
        }

        if (years > 100) {
            std::cout << "Mais de 1 seculo." << std::endl;
        }
        else {
            std::cout << years << " anos." << std::endl;
        } 
    }
}
