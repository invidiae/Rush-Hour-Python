import numpy as np
import copy
cars = np.array([[[2, 0], [2, 1], [np.nan, np.nan]],
                 [[3, 0], [3, 1], [3, 2]],
                 [[0, 5], [0, 4], [np.nan, np.nan]],
                 [[5, 5], [4, 5], [3, 5]],
                 [[0, 2], [1, 2], [2, 2]]])

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class Rush_Hour():
    def __init__(self, cars):
        self.cars = cars
        self.horizontal = []
        self.board = np.zeros((6, 6), dtype=int)

    def cars_in_board(self):
        board2 = np.zeros((6, 6), dtype=int)
        for index, car in enumerate(self.cars):
            counter = 0
            for coordinate in car:
                if not np.isnan(coordinate[0]):
                    counter += 1
                    if board2[int(coordinate[0]), int(coordinate[1])] != 0:
                        raise Exception(
                            "\nEine Koordinate Wurde Doppelt Eingegeben")
                    else:
                        board2[int(coordinate[0]),
                               int(coordinate[1])] = index + 1
                        if counter == 2:
                            if self.cars[index][0][0] == coordinate[0]:
                                self.horizontal.append(True)
                            else:
                                self.horizontal.append(False)
        self.board = board2

    def get_input(self):
        print(self.board)
        i = input("Welchen Zug möchtest du gehen? (Form:1u)")
        return i

    def up(self):
        if self.horizontal[self.inp_car]:
            print(color.RED + color.BOLD + "\nAuto hat falsche Ausrichtung!"+ color.END)
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 0] = [i - 1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 0]]
            if np.any(
                    self.hyp_new_coor[:, 0] < 0) or np.any(
                    self.hyp_new_coor[:, 0] > 5):
                print(color.RED + color.BOLD + "\nDu willst gegen eine Wand fahren" + color.END)
            else:
                wrong = None
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                wrong = 1
                if wrong is not None:
                    wrong = None
                    print(color.RED + color.BOLD + "Du willst gegen ein anderes Auto fahren" + color.END)
                else:
                    self.insert()


    def down(self):
        if self.horizontal[self.inp_car]:
            print(color.RED + color.BOLD + "\nAuto hat falsche Ausrichtung!"+ color.END)
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 0] = [i + 1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 0]]
            if np.any(
                    self.hyp_new_coor[:, 0] < 0) or np.any(
                    self.hyp_new_coor[:, 0] > 5):
                print(color.RED + color.BOLD + "\nDu willst gegen eine Wand fahren" + color.END)
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                wrong = 1
                if wrong is not None:
                    wrong = None
                    print(color.RED + color.BOLD + "Du willst gegen ein anderes Auto fahren" + color.END)
                else:
                    self.insert()

    def left(self):
        if not self.horizontal[self.inp_car]:
            print(color.RED + color.BOLD + "\nAuto hat falsche Ausrichtung!"+ color.END)
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 1] = [i - 1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 1]]
            if np.any(
                    self.hyp_new_coor[:, 1] < 0) or np.any(
                    self.hyp_new_coor[:, 1] > 5):
                print(color.RED + color.BOLD + "\nDu willst gegen eine Wand fahren" + color.END)
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                wrong = 1
                if wrong is not None:
                    wrong = None
                    print(color.RED + color.BOLD + "Du willst gegen ein anderes Auto fahren" + color.END)
                else:
                    self.insert()

    def right(self):
        if not self.horizontal[self.inp_car]:
            print(color.RED + color.BOLD + "\nAuto hat falsche Ausrichtung!"+ color.END)
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 1] = [i + 1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 1]]
            if np.any(
                    self.hyp_new_coor[:, 1] < 0) or np.any(
                    self.hyp_new_coor[:, 1] > 5):
                print(color.RED + color.BOLD + "\nDu willst gegen eine Wand fahren" + color.END)
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                wrong = 1
                if wrong is not None:
                    wrong = None
                    print(color.RED + color.BOLD + "Du willst gegen ein anderes Auto fahren" + color.END)
                else:
                    self.insert()

    def select(self):
        inp = self.get_input()
        inp_move = inp[1]
        self.inp_car = int(inp[0]) - 1
        if inp_move == "u":
            self.up()
        elif inp_move == "d":
            self.down()
        elif inp_move == "r":
            self.right()
        elif inp_move == "l":
            self.left()

    def insert(self):
        self.cars[self.inp_car] = self.hyp_new_coor
        self.cars_in_board()

    def check(self):
        if self.board[2, 5] == 1:
            return True
        else:
            return False


a = Rush_Hour(cars)
a.cars_in_board()
counter = 0
while not a.check():
    counter += 1
    print(counter)
    a.select()
print("Du hast gewonnen")
