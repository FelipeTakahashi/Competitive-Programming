#include <iostream>

using namespace std;

int main() {
    string jon, doc;
        cin  >> jon;
        cin  >> doc;
    
    if (jon.length() >= doc.length()) {
        cout << "go" << endl;
    }
    else {
        cout << "no" << endl;
    }
    
    return 0;
}
