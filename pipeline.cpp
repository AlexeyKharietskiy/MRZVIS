// Лабораторная работа №1 по дисциплине МРЗвИС
// Вариант 10: алгоритм вычисления произведения пары 6-разрядных чисел умножением 
// со старших разрядов со сдвигом частичного произведения влево
// Выполнил студент группы 221701 БГУИР Харецкий Алексей Дмитриевич

#include "pipeline.h"
#include <iostream>
#include <conio.h>
#include <iomanip>

Pipeline::Pipeline(vector<int> a, vector<int> b) {
	set_pairs(a, b);
}

void Pipeline::set_pairs(vector<int> a, vector<int> b) {
	if (a.size() != b.size())
		throw runtime_error("Input error!");
	for (int i = 0; i < a.size(); i++)
	{
		PairData pair(a[i], b[i]);
		this->pair_list.push_back(pair);
	}
}

void Pipeline::run_pipeline() {
	print_stages();
	int result_number = 0;
	bool queue_end;
	while (this->in_work == true)
	{
		this->tact++;
		queue_end = true;
		for (PairData pair : pair_list)
		{
			if (pair.in_queue) {
				queue_end = false;
				break;
			}
		}
		if (queue_end == true)
			stage_list[0].is_active = false;
		if (!queue_end) {
			pair_list[tact - 1].in_queue = false;
			stage_list[0].data = pair_list[tact - 1];
			stage_list[0].is_active = true;
		}
		this->in_work = false;
		for (int j = 0; j < stage_list.size(); j++)
		{
			if (stage_list[j].is_active && j < stage_list.size()) {
				stage_list[j].data.multiply(j);
				stage_list[j].data.add_product();
			}
			if (stage_list[j].is_active && j == stage_list.size() - 1) {
				this->pair_list[result_number++] = this->stage_list[j].data;
			}
		}
		print_stages();
		this->stage_shift();
		for (Stage stage : stage_list)
		{
			if (stage.is_active) {
				in_work = true;
				break;
			}
		}
	}
	print_result();
}

void Pipeline::stage_shift() {
	for (int i = 5; i > 0; --i) {
		this->stage_list[i] = this->stage_list[i - 1];
	}
}

void Pipeline::print_stages() {
	cout << "Input queue: " << endl;
	for (int i = 0; i < this->pair_list.size(); i++)
	{
		if (this->pair_list[i].in_queue)
			cout << pair_list[i].first_num << " " << pair_list[i].second_num << endl;
	}
	cout << "Tact " << this->tact << ":\n";
	cout << setw(10) << "Stage" << setw(20) << "Num1" << setw(20) << "Num2" << setw(26) << "Partial product" << setw(22) << "Partial sum" << endl;
	for (int i = 0; i < 6; ++i) {
		cout << setw(10) << i + 1;
		if (stage_list[i].is_active) {
			cout << setw(16);
			stage_list[i].data.print_binary(stage_list[i].data.get_first_multiplier(), false);
			cout << setw(15);
			stage_list[i].data.print_binary(stage_list[i].data.get_second_multiplier(), false);
			cout << setw(10);
			stage_list[i].data.print_binary(stage_list[i].data.get_partial_product(), true);
			cout << setw(10);
			stage_list[i].data.print_binary(stage_list[i].data.get_product(), true);
		}
		else {
			cout << setw(20) << "---" << setw(20) << "---" << setw(20) << "---" << setw(24) << "---";
		}
		cout << endl;
	}
	cout << "-------------------------------------------------------------------------------------------------------\n";
	std::cin.get();
	system("cls");
}
void Pipeline::print_result() {
	cout << "Global Result:" << endl;
	for (int i = 0; i < this->pair_list.size(); i++)
	{
		cout << "The first multiplier: ";
		pair_list[i].print_binary(pair_list[i].get_first_multiplier(), false);
		cout << ", the second multiplier: ";
		pair_list[i].print_binary(pair_list[i].get_second_multiplier(), false);
		cout << ", binary result: ";
		pair_list[i].print_binary(pair_list[i].get_product(), true);
		cout << ", normal result: " << this->pair_list[i].get_normal_product() << endl;
	}
}