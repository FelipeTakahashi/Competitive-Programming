#include <iostream>

using namespace std;

int main() {
    int n;
        cin  >> n;
    
    if (n % 2 == 0) {
        cout << (n*n)/2 << " casas brancas e " << (n*n)/2 << " casas pretas" << "\n";
    }
    else {
        cout << (n*n)/2 + 1 << " casas brancas e " << (n*n)/2 << " casas pretas" << "\n";
    }
    return 0;
}
