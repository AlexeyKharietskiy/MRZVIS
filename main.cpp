// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#include <stdexcept>
#include "pipeline.h"
#include "dataread.cpp"

int main() {
	vector<int> vector1, vector2;
	read_data("data.txt", vector1, vector2);
	try {
		Pipeline pipeline(vector1, vector2);
		pipeline.run_pipeline();
	}
	catch (const exception& e) {
		cerr << e.what() << endl;
	}
}

