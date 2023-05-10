#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    int a, b;

        cin  >> a;
        cin  >> b;

    double c;

        cin >> c;

        cout << "NUMBER = " << a << "\n";
        cout << fixed << setprecision(2);
        cout << "SALARY = U$ " << b*c << "\n";

    return 0;
  
}
