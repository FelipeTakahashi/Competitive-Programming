#include <iostream>
#include <math.h>

using namespace std;

int main() {

    int l, a, p, r;
    double diagonal;

        cin  >> l >> a >> p >> r;

    diagonal = sqrt(((l*l) + (a*a) + (p*p)));

        if (diagonal <= r*2) {
            cout << "S\n";
    }
        else {
            cout << "N\n";
    }
    return 0;
}
