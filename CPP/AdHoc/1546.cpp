#include <iostream>

using namespace std;

int main() {
    int dias, caso, numero;
        cin >> dias;

    for(int i = 0; i < dias; i++) {
        cin >> caso;
        for (int j = 0; i < caso; j++) {
            cin >> numero;

            if (numero == 1) {
                cout << "Rolien" << endl;
            }

            if (numero == 2) {
                cout << "Naej" << endl;
            }

            if (numero == 3) {
                cout << "Elehcim" << endl;
            }

            if (numero == 4) {
                cout << "Odranoel" << endl;
            }

        }
    }
    return 0;
}
