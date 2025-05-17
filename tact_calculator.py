"""Лабораторная работа 2 по дисциплине 'Модели решения задач в интеллектуальных системах'
Реализация модели решения задач в интеллектуальных системах
Выполнил: студент гр.221701  Перников И. Е.
Вариант 1: (~) = /2\\; /~\\ = /2\\; x~>y = 1 + x * (y - 1)
https://github.com/rastsislaux/bsuir/tree/main/semester-6/MRZvIS
Модели решения задач в интеллектуальных системах.
В 2 ч. Ч.1: Формальные модели обработки информации и параллельные модели решения задач:
учеб.-метод. пособие/ В. П. Ивашенко. – Минск : БГУИР, 2020. – 79 с.
15.05.2025
"""

import math


def calculate_parallel_tacts(
    p: int,
    q: int,
    m: int,
    n: int
):
    # layers = 23
    # d_layers = 4
    # f_layers = 12
    # c_layers = 7
    # layers_1 = 13
    # layers_2 = 7
    # layers_3 = 3
    
    d_tacts = math.ceil(m / n) * 2 + 2
    f_tacts = math.ceil(3 * m / n) * 1 + math.ceil(2 * m / n) * 5 + math.ceil(m / n) + 5
    c_tacts = math.ceil(3 / n) * 2 + math.ceil(2 / n) * 2 + 3
    
    c_elements_num = p * q
    parallel_tacts = c_elements_num * (d_tacts + f_tacts + c_tacts)
    return parallel_tacts