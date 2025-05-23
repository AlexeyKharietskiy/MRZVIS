// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#include "pair_data.h"
#include <algorithm>
#include <cmath>

PairData::PairData(int a, int b) {
    this->first_num = a;
    this->second_num = b;
	this->first_multiplier = this->make_binary(a);
	this->second_multiplier = this->make_binary(b);
 }

vector<int> PairData::make_binary(int multiplier){
		vector<int> binary = { 0,0,0,0,0,0 };
		for (int i = this->multiplier_length - 1; i >= 0 && multiplier != 0; i--)
		{
			binary[i] = multiplier % 2 == 0 ? 0 : 1;
			multiplier /= 2;
		}
		return binary;
}

void PairData::add_product() {
    this->product = leftshift(this->product);
    this->product = sum_numbers(this->product, this->partial_product);
}


vector<int> PairData::sum_numbers(vector<int> a, vector<int> b) {
    std::vector<int> result;
    int carry = 0;

    for (int i = a.size()-1; i >= 0; i--) {
        int sum = a[i] + b[i] + carry;
        result.push_back(sum % 2);
        carry = sum / 2;
    }
    reverse(result.begin(), result.end());
    return result;
}
void PairData::multiply(int bit_number) {
    for (int i = this->multiplier_length - 1; i >= 0; i--)
    {
        this->partial_product[this->multiplier_length + i] =
            this->first_multiplier[bit_number] * this->second_multiplier[i];
    }
}
int PairData::make_normal(vector<int> binary) {
    int decimal_value = 0;
    for (int i = binary.size() - 1; i >= 0; --i) {
        decimal_value += binary[i] * pow(2, binary.size() - i - 1);
    }

    return decimal_value;
}



int PairData::get_normal_product() {
    this->normal_product = make_normal(this->product);
    return this->normal_product;
}
vector<int> PairData::get_first_multiplier() {
    return this->first_multiplier;
}
vector<int> PairData::get_second_multiplier() {
    return this->second_multiplier;

}
vector<int> PairData::get_product() {
    return this->product;
}
vector<int> PairData::get_partial_product() {
    return this->partial_product;
}

void PairData::print_binary(vector<int> binary, bool division) {
    int space = 0;
    for (int i = 0; i < binary.size(); i++)
    {
        if (space % 4 == 0 && division == true)
            cout << " ";
        cout << binary[i];
        space++;
    }
}

vector<int> PairData::leftshift(vector<int> binary_num){
    for (int i = 0; i < binary_num.size()-1; i++)
    {
        binary_num[i] = binary_num[i + 1];
    }
    binary_num[binary_num.size() - 1] = 0;
    return binary_num;
}
