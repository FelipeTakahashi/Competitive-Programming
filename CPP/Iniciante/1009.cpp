#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    string name;

        cin  >> name;

    double income, sales, answer;

        cin  >> income;
        cin  >> sales;

        cout << fixed << setprecision(2);
        cout << "TOTAL = R$ " << 0.15 * sales + income << "\n";
    
    return 0;

}
