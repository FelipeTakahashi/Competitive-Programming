#include <iostream>

using namespace std;

int main() {
    
    string input, end;
    
        cin  >> input;

    int i;
    for(i = input.length() - 1; i >= 0; i--) {
       end += input[i];
    }
        cout << end << endl;

    return 0;

}
