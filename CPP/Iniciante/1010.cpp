#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
    
    int id, quantity;
    double price;
    
      cin  >> id >> quantity >> price;

    int id_2, quantity_2;
    double price_2;
    
      cin  >> id_2 >> quantity_2 >> price_2;
    
    double answer;
    
      answer = (quantity * price) + (quantity_2 * price_2);
    
      cout << fixed << setprecision(2);
      cout << "VALOR A PAGAR: R$ " << answer << "\n";
   
    return 0;
    
}
