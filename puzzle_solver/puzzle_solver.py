from typing import List, Tuple, Set, Optional
from copy import deepcopy


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0 :
        return 0
    total_seen_cells = 1  # 1 for the [row][col] cell that is not black
    for i in range(row-1, -1, -1) :
        if picture[i][col] == 0 :
            break
        total_seen_cells += 1
    for j in range(row+1,len(picture) ) :
        if picture[j][col] == 0:
            break
        total_seen_cells += 1
    for x in range(col-1, -1, -1) :
        if picture[row][x] == 0 :
            break
        total_seen_cells += 1
    for y in range(col+1, len(picture[0])) :
        if picture[row][y] == 0 :
            break
        total_seen_cells += 1
    return total_seen_cells

pic =  [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
# print(max_seen_cells(pic, 1, 1))


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0 or picture[row][col] == -1 :
        return 0
    total_seen_cells = 1  # 1 for the [row][col] cell that is not black
    for i in range(row-1, -1, -1) :
        if picture[i][col] == 0 or picture[i][col] == -1 :
            break
        total_seen_cells += 1
    for j in range(row+1,len(picture) ) :
        if picture[j][col] == 0 or picture[j][col] == -1 :
            break
        total_seen_cells += 1
    for x in range(col-1, -1, -1) :
        if picture[row][x] == 0 or picture[row][x] == -1  :
            break
        total_seen_cells += 1
    for y in range(col+1, len(picture[0])) :
        if picture[row][y] == 0 or picture[row][y] == -1  :
            break
        total_seen_cells += 1
    return total_seen_cells



def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    good_counter = 0
    might_be_good = 0
    for con in constraints_set :
        row = con[0]
        col = con[1]
        seen = con[2]
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)
        if max_seen == min_seen == seen :
            good_counter += 1
        elif min_seen <= seen <= max_seen :
            might_be_good += 1

    if good_counter == len(constraints_set) and might_be_good == 0 :
        return 1
    elif good_counter + might_be_good < len(constraints_set) :
        return 0
    return 2


def _solve_puzzle_helper(con_set: Set[Constraint], row_index: int, col_index: int, picture: List[List[int]]) -> Optional[Picture] :

    check = check_constraints(picture, con_set)

    if check == 1 :
        return picture

    if col_index == len(picture[0]) :
        col_index = 0
        row_index += 1

    if row_index == len(picture) :
        return None

    if picture[row_index][col_index] == 0 or picture[row_index][col_index] == 1 :
        return _solve_puzzle_helper(con_set, row_index, col_index+1, picture)

    if check == 2:
        picture[row_index][col_index] = 0
        try1 = _solve_puzzle_helper(con_set, row_index, col_index + 1, picture)
        if try1 != None :
            return try1
        picture[row_index][col_index] = 1
        try2 = _solve_puzzle_helper(con_set, row_index, col_index + 1, picture)
        if try2 != None :
            return try2
        return None

    if check == 0 :
        return None

def con_is_1(picture: List[List[int]], x: int, y: int) -> List[List[int]] :

    if x-1 >= 0 :
        picture[x-1][y] = 0
    if x+1 < len(picture) :
        picture[x+1][y] = 0
    if y-1 >= 0 :
        picture[x][y-1] = 0
    if y+1 < len(picture[0]) :
        picture[x][y+1] =0
    return picture


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    picture = []
    if not constraints_set :
        for i in range(n):
            temp_row = []
            for j in range(m):
                temp_row.append(0)
            picture.append(temp_row)
        return picture
    for i in range(n) :
        temp_row = []
        for j in range(m) :
            temp_row.append(-1)
        picture.append(temp_row)
    for con in constraints_set :  #adds black marks (0's) in the correct places if the constraint has a 0 or a 1
        if con[2] == 0 :
            picture[con[0]][con[1]] = 0
        if con[2] == 1 :
            picture = con_is_1(picture, con[0], con[1])
        if con[2] > 0 :
            picture[con[0]][con[1]] = 1

    if check_constraints(picture, constraints_set) == 0 :
        return None

    solution = _solve_puzzle_helper(constraints_set, 0, 0, picture)

    for i in range(len(picture)) :
        for j in range(len(picture[0])) :
            if solution[i][j] == -1 :
                solution[i][j] = 0

    return solution


def _how_many_solutions_helper(con_set: set[Constraint], row_index, col_index, picture) :

    check = check_constraints(picture, con_set)

    if col_index == len(picture[0]) and row_index == len(picture)-1 :
        if check != 0 :
            return 1
        return 0

    if col_index == len(picture[0]) :
        col_index = 0
        row_index += 1

    if picture[row_index][col_index] == 0 or picture[row_index][col_index] == 1 :
        return _how_many_solutions_helper(con_set, row_index, col_index+1, picture)

    if check == 0 :
        picture[row_index][col_index] = -1
        return 0

    if check != 0:
        copy_pic1 = deepcopy(picture)
        copy_pic1[row_index][col_index] = 0
        try1 = _how_many_solutions_helper(con_set, row_index, col_index + 1, copy_pic1)
        copy_pic2 = deepcopy(picture)
        copy_pic2[row_index][col_index] = 1
        try2 = _how_many_solutions_helper(con_set, row_index, col_index + 1, copy_pic2)
        return try1 + try2



def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    solution_counter = 0
    picture = []
    if not constraints_set:
        return 2**(n*m)
    for i in range(n):
        temp_row = []
        for j in range(m):
            temp_row.append(-1)
        picture.append(temp_row)
    for con in constraints_set:  # adds black marks (0's) in the correct places if the constraint has a 0 or a 1
        if con[2] == 0:
            picture[con[0]][con[1]] = 0
        if con[2] == 1:
            picture = con_is_1(picture, con[0], con[1])
        if con[2] > 0 :
            picture[con[0]][con[1]] = 1
    if check_constraints(picture, constraints_set) == 0:
        return 0

    solution_counter = _how_many_solutions_helper(constraints_set, 0, 0, picture)

    return solution_counter



def generate_puzzle(picture: Picture) -> Set[Constraint]:

    con_set = set()
    rows = len(picture)
    cols = len(picture[0])
    for i in range(rows) :
        for j in range(cols) :
            seen = max_seen_cells(picture, i, j)
            con_set.add((i, j, seen))
            if how_many_solutions(con_set, rows, cols) == 1 :
                break
    return con_set
