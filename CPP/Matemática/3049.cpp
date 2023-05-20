#include <iostream>

using namespace std;

int main() {
    int b, t;
        cin  >> b;
        cin  >> t;
    
    int area_t, area_n;
        area_t = (b+t) * 35;
        area_n = 11200 - area_t;
    
        if(area_t>area_n) {
            cout << "1" << endl;
        }

        else if (area_n>area_t) {
            cout << "2" << endl;
        }
        
        else {
            cout << "0" << endl;
        }

    return 0;
}
