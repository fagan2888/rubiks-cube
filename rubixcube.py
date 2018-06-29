import numpy as np

FACE_CONST = 6
SIZE_CONST = 3


def match_color(input):
    if 'R' in input:
        return 'R'
    elif 'G' in input:
        return 'G'
    elif 'B' in input:
        return 'B'
    elif 'W' in input:
        return 'W'
    elif 'Y' in input:
        return 'Y'
    elif 'O' in input:
        return 'O'
    else:
        return 'X'


class RubixCube:
    def __init__(self, cube, moves):
        self.cube = cube
        self.moves = moves

    def read_cube(self, file_name):
        input_file = open(file_name, 'r')
        self.cube = np.empty((0, 3))

        for line in input_file:
            input = line.split(' ')
            counter = 0
            arr = []

            for element in input:
                color = match_color(element)
                if color != 'X':
                    arr.append(color)
                    counter += 1
                    if counter == 3:
                        self.cube = np.append(self.cube, [arr], axis=0)
                        arr = []
                        counter = 0

    def FrontCW(self):  # action 1
        self.cube[6:9, 0:3] = np.fliplr(self.cube[6:9, 0:3].transpose())
        temp1 = np.array(self.cube[2, 0:3])
        temp2 = np.array(self.cube[9:12, 0])
        temp3 = np.array(self.cube[15, 0:3])
        temp4 = np.array(self.cube[3:6, 2])
        self.cube[2, 0:3] = np.fliplr([temp4])[0]
        self.cube[9:12, 0] = temp1
        self.cube[15, 0:3] = np.fliplr([temp2])[0]
        self.cube[3:6, 2] = temp3

    def FrontACW(self):  # action 2
        self.FrontCW()
        self.FrontCW()
        self.FrontCW()

    def UpCW(self):  # action 3
        self.cube[0:3, 0:3] = np.fliplr(self.cube[0:3, 0:3].transpose())
        temp1 = np.array(self.cube[12, 0:3])
        temp2 = np.array(self.cube[9, 0:3])
        temp3 = np.array(self.cube[6, 0:3])
        temp4 = np.array(self.cube[3, 0:3])
        self.cube[12, 0:3] = temp4
        self.cube[9, 0:3] = temp1
        self.cube[6, 0:3] = temp2
        self.cube[3, 0:3] = temp3

    def UpACW(self):  # acion 4
        self.UpCW()
        self.UpCW()
        self.UpCW()

    def DownCW(self):  # action 5 Front down clock wise
        self.cube[15:18, 0:3] = np.fliplr(self.cube[15:18, 0:3].transpose())
        temp1 = np.array(self.cube[8, 0:3])
        temp2 = np.array(self.cube[11, 0:3])
        temp3 = np.array(self.cube[14, 0:3])
        temp4 = np.array(self.cube[5, 0:3])
        self.cube[8, 0:3] = temp4
        self.cube[11, 0:3] = temp1
        self.cube[14, 0:3] = temp2
        self.cube[5, 0:3] = temp3

    def DownACW(self):  # action 6
        self.DownCW()
        self.DownCW()
        self.DownCW()

    def LeftCW(self):  # action 7

        self.cube[3:6, 0:3] = np.fliplr(self.cube[3:6, 0:3].transpose())
        temp1 = np.array(self.cube[0:3, 0])
        temp2 = np.array(self.cube[6:9, 0])
        temp3 = np.array(self.cube[15:18, 0])
        temp4 = np.array(self.cube[12:15, 2])
        self.cube[0:3, 0] = np.fliplr([temp4])[0]
        self.cube[6:9, 0] = temp1
        self.cube[15:18, 0] = temp2
        self.cube[12:15, 2] = np.fliplr([temp3])[0]

    def LeftACW(self):  # action 8
        self.LeftCW()
        self.LeftCW()
        self.LeftCW()

    def RightCW(self):  # action 9 Front right clock wise

        self.cube[9:12, 0:3] = np.fliplr(self.cube[9:12, 0:3].transpose())
        temp1 = np.array(self.cube[0:3, 2])
        temp2 = np.array(self.cube[12:15, 0])
        temp3 = np.array(self.cube[15:18, 2])
        temp4 = np.array(self.cube[6:9, 2])
        self.cube[0:3, 2] = temp4
        self.cube[12:15, 0] = np.fliplr([temp1])[0]
        self.cube[15:18, 2] = np.fliplr([temp2])[0]
        self.cube[6:9, 2] = temp3

    def RightACW(self):  # action 10
        self.RightCW()
        self.RightCW()
        self.RightCW()

    def BackCW(self):  # action 11 Front  back clock wise

        self.cube[12:15, :] = np.fliplr(self.cube[12:15, :].transpose())
        temp1 = np.array(self.cube[0, 0:3])
        temp2 = np.array(self.cube[3:6, 0])
        temp3 = np.array(self.cube[17, 0:3])
        temp4 = np.array(self.cube[9:12, 2])
        self.cube[0, 0:3] = temp4
        self.cube[3:6, 0] = np.fliplr([temp1])[0]
        self.cube[17, 0:3] = temp2
        self.cube[9:12, 2] = np.fliplr([temp3])[0]

    def BackACW(self):  # action 12
        self.BackCW()
        self.BackCW()
        self.BackCW()

    def make_move(self, move, reverse, printCube):
        # move number
        # reverse if 0 original move if 1 reverse of input move
        # printCube 0/1 if 0 dont print else print

        if reverse == 1:
            if move % 2 == 0:
                move = move - 1
            else:
                move = move + 1

        if move == 1:
            self.FrontCW()
            print("FrontCW")
        elif move == 2:
            self.FrontACW()
            print("FrontACW")
        elif move == 3:
            self.UpCW()
            print("UpCW")
        elif move == 4:
            self.UpACW()
            print("UpACW")
        elif move == 5:
            self.DownCW()
            print("DownCW")
        elif move == 6:
            self.DownACW()
            print("DownACW")
        elif move == 7:
            self.LeftCW()
            print("LeftCW")
        elif move == 8:
            self.LeftACW()
            print("LeftACW")
        elif move == 9:
            self.RightCW()
            print("RightCW")
        elif move == 10:
            self.RightACW()
            print("RightACW")
        elif move == 11:
            self.BackCW()
            print("BackCW")
        elif move == 12:
            self.BackACW()
            print("BackACW")

        if printCube == 1:
            self.print_cube()

    def print_cube(self):
        print("             ", self.cube[0, 0:3])
        print("             ", self.cube[1, 0:3])
        print("             ", self.cube[2, 0:3])
        print(self.cube[3, 0:3], self.cube[6, 0:3], self.cube[9, 0:3], self.cube[12, 0:3])
        print(self.cube[4, 0:3], self.cube[7, 0:3], self.cube[10, 0:3], self.cube[13, 0:3])
        print(self.cube[5, 0:3], self.cube[8, 0:3], self.cube[11, 0:3], self.cube[14, 0:3])
        print("             ", self.cube[15, 0:3], " ", " ", " ")
        print("             ", self.cube[16, 0:3], " ", " ", " ")
        print("             ", self.cube[17, 0:3], " ", " ", " ")

    def check_cube_solved(self):
        index = 0

        for face in range(FACE_CONST):
            color = self.cube[index, 0]

            for i in range(SIZE_CONST):

                for j in range(SIZE_CONST):
                    if self.cube[index, j] == color:
                        pass
                    else:
                        return False

                index += 1

        return True

    def print_moves(self):
        print("Moves to reach solution (from start to finish)")

        for move in self.moves:
            if move == 1:
                print("FrontCW")
            elif move == 2:
                print("FrontACW")
            elif move == 3:
                print("UpCW")
            elif move == 4:
                print("UpACW")
            elif move == 5:
                print("DownCW")
            elif move == 6:
                print("DownACW")
            elif move == 7:
                print("LeftCW")
            elif move == 8:
                print("LeftACW")
            elif move == 9:
                print("RightCW")
            elif move == 10:
                print("RightACW")
            elif move == 11:
                print("BackCW")
            elif move == 12:
                print("BackACW")
