from PIL import Image
import numpy as np
from collections import deque as Q

black_pixel = np.array(Image.open("full_black.jpg"))[0][0]
white_pixel = np.array(Image.open("full_white.jpg"))[0][0]

diff = np.array([10,10,10])


def bfs(loc, grid, visited: set):

    q = Q()
    q.append(loc)
    visited.add(loc)

    while len(q) != 0:

        x = q.popleft()

        p1 = (x[0] + 1, x[1])
        p2 = (x[0], x[1] + 1)
        p3 = (x[0] - 1, x[1])
        p4 = (x[0], x[1]-1)
        for i in [p1,p2,p3,p4]:
            if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[i[0]]) and (grid[i[0]][i[1]] <= black_pixel+diff).all() and i not in visited:
                q.append(i)
                visited.add(i)

def count_shapes(grid):

    visited = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if (grid[i][j] <= black_pixel+diff).all() and (i,j) not in visited:
                bfs((i,j), grid, visited)
                count += 1

    return count



def program(target: str):
    grid = np.array(Image.open(target+".jpg"))

    return count_shapes(grid)


file_name = input("file name(without extension): ")

print(f"there are {program(file_name)} black objects")