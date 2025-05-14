from matrix import Matrix


def sum(a, b):
    return a + b

def mult(a, b):
    return a * b

def diff(a, b):
    return a - b

def conj(a, b):
    return min(a, b)

def tnorm(a, b):
    return a * b

def impl(a, b):
    return sum(1, mult(a, diff(b, 1)))

def reduction1(arr: list, k):
#|~\
    res = 1
    for i in range(k):
        res *= arr[i]
    return res   

def reduction2(arr: list, k):
#\~|
    res = 1
    for i in range(k):
        res *= 1 - arr[i]
    return 1 - res 

def get_f(
    i, 
    j, 
    k, 
    a: Matrix, 
    b: Matrix, 
    e: Matrix
    ):
    res = (
        sum(
            mult(
                mult(
                    impl(
                        a.values[i][k], 
                        b.values[k][j]
                        ),
                    diff(
                        mult(
                            2,
                            e.values[k][0],
                        ),
                        1
                    )
                ),
                e.values[k][0]
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
                                    impl(
                                        a.values[i][k],
                                        b.values[k][j]
                                        )
                                    ),
                                2
                                ),
                            e.values[k][0]
                            )
                        )
                    ),
                diff(
                    1,
                    e.values[k][0]
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
