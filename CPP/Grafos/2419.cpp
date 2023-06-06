#include <iostream>

using namespace std;

int main() {
    int m, n;
        std::cin >> m >> n;

    char M[m][n];
        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < n; ++j) {
                cin >> M[i][j];
            }
        }

    int count = 0;
    for(int i = 0; i < m; ++i) {
        for(int j = 0; j < n; ++j) {
            if (M[i][j] == '.') continue;
            else {
                if (i != m-1) {
                        if (M[i+1][j] == '.') {
                            count++; 
                            continue;
                        }
                }

                if (j != n-1) {
                        if (M[i][j+1] == '.') {
                            count++; 
                            continue;
                        }
                }

                if (i != 0) {
                        if (M[i-1][j] == '.') {
                            count++; 
                            continue;
                        }
                }

                if (j != 0) {
                        if (M[i][j-1] == '.') {
                            count++; 
                            continue;
                    }
                }

                if (j == 0 or i == m-1 or j == n-1 or i == 0) {
                    if (M[i][j] == '#');
                    count++;
                    continue;
                }
            }
        }
    }
    cout << count << endl;
}
