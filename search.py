from copy import deepcopy

CUBE_MOVES = 12
SIZE_CONST = 3
FACE_CONST = 6


def check_move(moves, i):
    """
    if len(moves) >= 1 and (
            ((moves[-1] + 1) % 2 == 0 and moves[-1] + 1 == i) or ((moves[-1] - 1) % 2 == 1 and moves[-1] - 1 == i)):
        return False

    if len(moves) >= 3 and moves[-1] == i and moves[-2] == i and moves[-3] == i:
        return False
    """
    return True


def depth_limit_search(state, depth):
    if state.check_cube_solved():
        state.print_cube()
        state.print_moves()
        return True
    elif depth == 0:
        return False
    else:
        for i in range(CUBE_MOVES):

            if check_move(state.moves, i + 1):
                new_state = deepcopy(state)
                new_state.make_move(i + 1, 0, 0)
                new_state.print_cube()
                new_state.moves.append(i + 1)

                if (depth_limit_search(new_state, depth - 1)):
                    return True

    return False


def IDFS(state, maxDepth):
    for i in range(maxDepth + 1):
        print("Using depth limit search with max depth " + str(i))
        if (depth_limit_search(state, i)):
            return True

    return False


def hash_cube(cube):
    combo = ""

    index = 0

    for face in range(FACE_CONST):
        combo += cube[index, 0]
        combo += cube[index, 2]
        index += 2
        combo += cube[index, 0]
        combo += cube[index, 2]
        index += 1

    return combo


def generate_pattern_database(state, depth, file_name):
    data_file = open(file_name, 'w')
    queue = []

    queue.append(state)
    nodes = 1

    for d in range(depth):
        counter = nodes
        nodes = 0
        for j in range(counter):
            s = queue.pop(0)

            for i in range(CUBE_MOVES):
                if check_move(s.moves, i + 1):
                    new_state = deepcopy(s)
                    new_state.make_move(i + 1, 0, 0)
                    new_state.moves.append(i + 1)
                    combo = hash_cube(new_state.cube)
                    data_file.write(combo + "," + str(d) + '\n')
                    queue.append(new_state)
                    nodes += 1

# def search():

# def IDA_star():
