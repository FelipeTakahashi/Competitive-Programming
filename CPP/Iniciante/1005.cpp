#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    double a, b;

    cin  >> a;
    cin  >> b;

    cout << fixed << setprecision(5);
    cout << "MEDIA = " << ((3.5*a) + (7.5*b))/11 << "\n";

    return 0;

}
