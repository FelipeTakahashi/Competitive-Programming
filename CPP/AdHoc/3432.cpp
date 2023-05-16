#include <iostream>

using namespace std;

int main() {
    int sequel[8];
    int i;

    bool Flag;

    Flag = true;

        for(i = 0; i < 8; i++) {
            cin >> sequel[i];
            if (sequel[i] == 9) {
                Flag = false;
                break;
            }
        }

    if(Flag) {
        cout << "S" << endl;
    }

    else {
        cout << "F" << endl;
    }

    return 0;
    
}
