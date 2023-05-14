#include <iostream>

using namespace std;

int main() {

    int a, b, c;

        cin  >> a >> b >> c;

    int valores[3] = {a, b, c};
    
        if (valores[0] > valores[1]) {
            swap(valores[0], valores[1]);
        }
        if (valores[0] > valores[2]) {
            swap(valores[0], valores[2]);
        }
        if (valores[1] > valores[2]) {
            swap(valores[1], valores[2]);
        }

    cout << valores[1] << endl;
    
    return 0;
}
