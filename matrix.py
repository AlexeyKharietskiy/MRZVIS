"""Лабораторная работа 2 по дисциплине 'Модели решения задач в интеллектуальных системах'
Реализация модели решения задач в интеллектуальных системах
Выполнил: студент гр.221701  Харецкий А. Д.
Вариант 3: (~) = /1\\; /~\\ = /2\\; x~>y = 1 + x * (y - 1)
https://github.com/rastsislaux/bsuir/tree/main/semester-6/MRZvIS
Модели решения задач в интеллектуальных системах.
В 2 ч. Ч.1: Формальные модели обработки информации и параллельные модели решения задач:
учеб.-метод. пособие/ В. П. Ивашенко. – Минск : БГУИР, 2020. – 79 с.
15.05.2025
"""

import random


class Matrix:
    def __init__(self, length: int, hight: int):
        self.length: int = length
        self.hight: int = hight
        self.values = [
            [
                round(
                    random.uniform(-1, 1.001), 
                    3
                    )
                for _ in range(self.hight)
                ]
            for i in range(self.length)
        ]
        
    def show(self):
        for i in range(self.length):
            print('[', end=' ')
            for j in range(self.hight):
                print(f'{self.values[i][j]}', end=' ')
            print(']')