import numpy as np
from copy import deepcopy
from rubixcube import *
from search import *
from random import randint
import math

cubeInitial = np.array(
    [
        # ['00', '01', '02'],
        # ['10', '11', '12'],
        # ['20', '21', '22'],
        # ['30', '31', '32'],
        # ['40', '41', '42'],
        # ['50', '51', '52'],
        # ['60', '61', '62'],
        # ['70', '71', '72'],
        # ['80', '81', '82'],
        # ['90', '91', '92'],
        # ['100', '101', '102'],
        # ['110', '111', '112'],
        # ['120', '121', '122'],
        # ['130', '131', '132'],
        # ['140', '141', '142'],
        # ['150', '151', '152'],
        # ['160', '161', '162'],
        # ['170', '171', '172']

        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']

    ]
)

cube = RubixCube(deepcopy(cubeInitial), [])
#generate_pattern_database(cube,7,"output.txt")

cube.read_cube("input1.txt")

# pick random moves
total_move = 4
my_randoms = [randint(1, 12) for x in range(total_move)]

cube.print_cube()

#for move in my_randoms:
    #cube.make_move(move,0,0)

IDFS(cube, 3)
