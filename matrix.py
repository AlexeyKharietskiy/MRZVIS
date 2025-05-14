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
                for _ in range(self.length)
                ]
            for i in range(self.hight)
        ]
        
    def show(self):
        for i in range(self.hight):
            print('[', end=' ')
            for j in range(self.length):
                print(f'{self.values[i][j]}', end=' ')
            print(']')