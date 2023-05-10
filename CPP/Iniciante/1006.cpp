#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    double a, b, c;

        cin  >> a;
        cin  >> b;
        cin  >> c;

        cout << fixed << setprecision(1);
        cout << "MEDIA = " << ((2*a) + (3*b) + (5*c))/10 << "\n";

    return 0;

}
