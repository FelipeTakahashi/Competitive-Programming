#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    int km;
    double gas;

        cin >> km;
        cin >> gas;

        cout << fixed << setprecision(3);
        cout << km/gas << " km/l" << endl;

    return 0;
  
}
