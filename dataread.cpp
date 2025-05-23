// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;
void inline read_data(const string& filename, vector<int>& vec1, vector<int>& vec2) {
    ifstream file(filename);
    if (!file) {
        cerr << "File open error!" << endl;
        return;
    }

    string line;
    int number;

    if (getline(file, line)) {
        istringstream stream(line);
        while (stream >> number) {
            vec1.push_back(number);
        }
    }

    if (getline(file, line)) {
        istringstream stream(line);
        while (stream >> number) {
            vec2.push_back(number);
        }
    }
}