from matrix import Matrix
from operations import get_c_el


if __name__ == "__main__":
    m = int(input("m = "))
    p = int(input("p = "))
    q = int(input("q = "))
    n = int(input("n = "))
    
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