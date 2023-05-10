#include <iostream>

using namespace std;

int main() {

    int a, b, c;
    int lista[3];

        cin  >> a >> b >> c;
        
        lista[0] = a;
        lista[1] = b;
        lista[2] = c;

    int aux;

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(lista[i] < lista[j])   {
                aux = lista[j];
                lista[j] = lista[i];
                lista[i] = aux;
            }
        }
    }
  
        cout << lista[0] << "\n" << lista[1] << "\n" << lista[2] << "\n" << "\n";
        cout << a << "\n" << b << "\n" << c << "\n";
  
  return 0;
}
