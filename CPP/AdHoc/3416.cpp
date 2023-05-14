#include <iostream>
#include <math.h>

using namespace std;

int main() {

    int n, l, d;

        cin >> n >> l >> d;

        cout << l * (ceil((n*d)/(1000.0*l))) << endl;
    
    return 0;
}
