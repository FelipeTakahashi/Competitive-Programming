#include <iostream>

using namespace std;

int main() {
    
    int number, highest, index;
    
      highest = 0;
      index = 0;
    
    for (int i = 0; i < 100; i++) {
        cin >> number;
      
            if (number > highest) {
                highest = number;
                index = i;
              
            }
        
    }
    
      cout << highest << "\n";
      cout << index + 1 << "\n";
    
    return 0;
}
