#include <iostream>

using namespace std;

int main() {
    int tabs, actions;
        cin >> tabs >> actions;
    
    string action;
    for(int i = 0; i < actions; i++) {
        cin >> action;
        if (action == "fechou") {
            tabs += 1;
        }
        else {
            tabs -= 1;
        }
    }
        cout << tabs << endl;

    return 0;
}
