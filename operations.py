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

from matrix import Matrix
consistent_tacts = 0

def sum(a, b):
    global consistent_tacts
    consistent_tacts += 1
    return a + b

def mult(a, b):
    global consistent_tacts
    consistent_tacts += 1
    return a * b

def diff(a, b):
    global consistent_tacts
    consistent_tacts += 1
    return a - b

def conj(a, b):
    global consistent_tacts
    consistent_tacts += 1
    return min(a, b)

def tnorm(a, b):
    global consistent_tacts
    consistent_tacts += 1
    return a * b

def impl(a, b):
    return sum(1, mult(a, diff(b, 1)))

def reduction1(arr: list, k):
#|~\
    global consistent_tacts
    res = 1
    for i in range(k):
        res = mult(res, arr[i])
    consistent_tacts -= 1   
    return res   

def reduction2(arr: list, k):
#\~|
    global consistent_tacts
    res = 1
    for i in range(k):
        res = mult(
            res,
            diff(
                1,
                arr[i]
            )
        )
    return 1 - res 

def get_f(
    i: int, 
    j: int, 
    k: int, 
    a: Matrix, 
    b: Matrix, 
    e: Matrix
    ):
    a_impl_b = impl(
        a.values[i][k], 
        b.values[k][j]
        )
    res = (
        sum(
            mult(
                mult(
                    a_impl_b,
                    diff(
                        mult(
                            2,
                            e.values[0][k],
                        ),
                        1
                    )
                ),
                e.values[0][k]
            ),
            mult(
                mult(
                    impl(
                        b.values[k][j],
                        a.values[i][k]
                        ),
                    sum(
                        1, 
                        mult(
                            diff(
                                mult(
                                    4,
                                    a_impl_b
                                    ),
                                2
                                ),
                            e.values[0][k]
                            )
                        )
                    ),
                diff(
                    1,
                    e.values[0][k]
                    )
                )  
        )
    )
    return res
    
def get_d(  
    i: int,
    j: int,
    k: int,
    a: Matrix,
    b: Matrix
):
    tnorm_list = [
        tnorm(
            a.values[i][_],
            b.values[_][j]
            )
        for _ in range(k)
        ]
    res = reduction2(tnorm_list, k)
    return res

def get_c_el(
    i: int,
    j: int,
    k: int,
    a: Matrix,
    b: Matrix,
    e: Matrix,
    g: Matrix
):
    f_list = []
    for k_it in range(k):
        f_list.append(
            get_f(i, j, k_it, a, b, e)
            )
    f_reduction = reduction1(f_list, k)
    g_val = g.values[i][j]
    d = get_d(i, j, k, a, b)
    res = (
        sum(
            mult(
                mult(
                    f_reduction,
                    diff(
                        mult(
                            3,
                            g_val
                        ),
                        2
                    )
                ),
                g_val
            ),
            mult(
                diff(
                        1,
                        g_val
                ),
                mult(
                    sum(
                        d,
                        diff(
                            mult(
                                4,
                                conj(
                                    f_reduction,
                                    d
                                )
                            ),
                            mult(
                                3,
                                d
                            )
                        ),  
                    ),
                    g_val 
                ),
            )
            
        )
    )
    return round(res, 2)

def get_consistent_tacts():
    global consistent_tacts
    a = consistent_tacts
    consistent_tacts = 0
    return a