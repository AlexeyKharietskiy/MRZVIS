// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#pragma once
#include <iostream>
#include <vector>
using namespace std;

class PairData {
public:
    PairData(int, int);
    PairData() {};
    bool in_queue = true;
    int first_num = 0;
    int second_num = 0;
    void add_product();
    int get_normal_product();
    vector<int> get_first_multiplier();
    vector<int> get_second_multiplier();
    vector<int> get_product();
    vector<int> get_partial_product();
    void multiply(int);
    static void print_binary(vector<int>, bool);
private:
    vector<int> first_multiplier = { 0,0,0,0,0,0 };
    vector<int> second_multiplier = { 0,0,0,0,0,0 };
    vector<int> partial_product = { 0,0,0,0,0,0,0,0,0,0,0,0 };
    vector<int> product = { 0,0,0,0,0,0,0,0,0,0,0,0 };
    int normal_product = 0;
    int multiplier_length = 6;
    vector<int> make_binary(int);
    static int make_normal(vector<int>);
    static vector<int> sum_numbers(vector<int>, vector<int>);
    static vector<int> leftshift(vector<int>);
};