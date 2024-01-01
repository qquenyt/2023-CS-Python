import sys
from typing import List


class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        new_state = []
        fish = 2
        shrimp = 3

        for i in range(len(self.state)):
            new_row = []
            for j in range(len(self.state[i])):
                if self.state[i][j] == 1:
                    new_row.append(1)
                else:
                    n_fish = 0
                    n_shrimp = 0
                    neighbors = [
                        (i - 1, j - 1),
                        (i - 1, j),
                        (i - 1, j + 1),
                        (i, j - 1),
                        (i, j + 1),
                        (i + 1, j - 1),
                        (i + 1, j),
                        (i + 1, j + 1),
                    ]
                    for ni, nj in neighbors:
                        if ni < 0 or nj < 0 or ni >= len(self.state) or nj >= len(self.state[i]):
                            continue
                        if self.state[ni][nj] == fish:
                            n_fish += 1
                        elif self.state[ni][nj] == shrimp:
                            n_shrimp += 1
                    if self.state[i][j] == fish:
                        if n_fish < 2 or n_fish > 3: 
                            new_row.append(0)
                        else:
                            new_row.append(2)
                    elif self.state[i][j] == shrimp:
                        if n_shrimp < 2 or n_shrimp > 3:  
                            new_row.append(0)
                        else:
                            new_row.append(3)
                    elif n_fish == fish and n_shrimp == shrimp:
                        new_row.append(2)
                    elif n_fish == 3: 
                        new_row.append(2)
                    else:
                        new_row.append(0)
            new_state.append(new_row)
        
        return Ocean(init_state=new_state)

if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
