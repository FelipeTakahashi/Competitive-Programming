#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    
    int raio;
    
      cin  >> raio;
    
      cout << fixed << setprecision(3);
      cout << "VOLUME = " << (4.0/3.0) * 3.14159 * raio * raio * raio << "\n";

    return 0;
    
}
