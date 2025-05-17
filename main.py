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

from matrix import Matrix
from operations import get_c_el, get_consistent_tacts
from tact_calculator import calculate_parallel_tacts




if __name__ == "__main__":
    m = int(input("m = "))
    p = int(input("p = "))
    q = int(input("q = "))
    n = int(input("n = "))
    global T1, Tn, Ky, r, e, L_avg, D
    A = Matrix(p, m)
    B = Matrix(m, q)
    E = Matrix(1, m)
    G = Matrix(p, q)
    C = Matrix(p, q)
    
    for i in range(p):
        for j in range(q):
            C.values[i][j] = get_c_el(
                i,
                j,
                m,
                A,
                B,
                E,
                G
            )
            
    print(f'\nA:')
    A.show()
    print(f'\nB:')
    B.show()
    print(f'\nE:')
    E.show()
    print(f'\nG:')
    G.show()
    print(f'\nC:')
    C.show()
    T1 = get_consistent_tacts()
    Tn = calculate_parallel_tacts(p, q, m, n) if n > 1 else T1
    Ky = T1 / Tn
    e = Ky / n
    r = p * q + p * m + q * m + 1 * m + p * q
    L_avg = T1/ r
    D = Tn / L_avg
    print(f'\n\n{T1=}')
    print(f'{Tn=}')
    print(f'{Ky=}')
    print(f'{e=}')
    print(f'{r=}')
    print(f'{L_avg=}')
    print(f'{D=}\n\n')