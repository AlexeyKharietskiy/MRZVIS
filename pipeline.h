// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#pragma once
#include "pair_data.h"
#include "stage.h"
#include <array>

class Pipeline {
private:
	vector<PairData> pair_list;
	array<Stage, 6> stage_list;
	bool in_work = true;
	int tact = 0;
	void stage_shift();
	void print_stages();
	void print_result();
public:
	Pipeline(vector<int>, vector<int>);
	void set_pairs(vector<int>, vector<int>);
	void run_pipeline();
};