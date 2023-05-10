#include <iostream>

using namespace std;

int main() {
    
    int num;
    while (cin >> num) {
        if (num == 0) {
            cout << "vai ter copa!\n";
        }
        else {
            cout << "vai ter duas!\n";
        }
    }
    return 0;
}
