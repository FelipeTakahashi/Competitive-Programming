#include <iostream>

int main() {
    std::string cpf, parts_item, parts[4];
        std::cin >> cpf;

    int parts_index = 0;
    for (int i = 0; i < cpf.length(); i++) {
        if (cpf[i] == '-' or cpf[i] == '.') {
            parts[parts_index] = parts_item;
            parts_index += 1;
            parts_item = "";
        } 
        else {
            parts_item += cpf[i];
        }
    }

    parts[3] = parts_item;

    for (int j = 0; j < 4; j++) {
        std::cout << parts[j] << std::endl;
    }
}
