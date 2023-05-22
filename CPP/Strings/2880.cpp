#include <iostream>

using namespace std;

int main() {
    string coded, crib, test;
        cin >> coded;
        cin >> crib;

    int possible = 0;

    bool igualdade;
    for (int temp = 0; temp < coded.length() - crib.length() + 1; temp++) {
        igualdade = true;
        test = coded.substr(temp, crib.length() + temp);

        for (int letter = 0; letter < crib.length(); letter++) {
            if (test[letter] == crib[letter]) {
                igualdade = false;
                break;
            }
        }

        if (igualdade) {
            possible += 1;
        }
    }
        cout << possible << endl;
    return 0;
}
