import numpy as np
import copy

cars = np.array([[[0, 0], [0, 1], [np.nan, np.nan]],
                 [[3, 1], [4, 1], [5, 1]],
                 [[3, 3], [3, 2], [np.nan, np.nan]],
                 [[5, 3], [4, 3], [np.nan, np.nan]],
                 [[1, 5], [0, 5], [np.nan, np.nan]],
                 [[5, 0], [4, 0], [np.nan, np.nan]],
                 [[2, 0], [1, 0], [np.nan, np.nan]]])


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
                               int(coordinate[1])] = index+1
                        if counter == 2:
                            if self.cars[index][0][0] == coordinate[0]:
                                self.horizontal.append(True)
                            else:
                                self.horizontal.append(False)
        self.board = board2

    def get_input(self):
        print(self.board)
        return input("Welchen Zug möchtest du gehen? Form:1u\n")

    def up(self):
        if self.horizontal[self.inp_car]:
            raise Exception("\nAuto hat falsche Ausrichtung!")
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 0] = [i-1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 0]]
            if np.any(
                    self.hyp_new_coor[:, 0] < 0) or np.any(
                    self.hyp_new_coor[:, 0] > 5):
                raise Exception("\nDu willst gegen eine Wand fahren")
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                raise Exception(    # FIXME
                                   "\nDu willst gegen ein Auto fahren")
                self.insert()

    def down(self):
        if self.horizontal[self.inp_car]:
            raise Exception("\nAuto hat falsche Ausrichtung!")
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 0] = [i+1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 0]]
            if np.any(
                    self.hyp_new_coor[:, 0] < 0) or np.any(
                    self.hyp_new_coor[:, 0] > 5):
                raise Exception("\nDu willst gegen eine Wand fahren")
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                raise Exception(    # FIXME
                                   "\nDu willst gegen ein Auto fahren")
                self.insert()

    def left(self):
        if not self.horizontal[self.inp_car]:
            raise Exception("\nAuto hat falsche Ausrichtung!")
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 1] = [i-1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 1]]
            if np.any(
                    self.hyp_new_coor[:, 1] < 0) or np.any(
                    self.hyp_new_coor[:, 1] > 5):
                raise Exception("\nDu willst gegen eine Wand fahren")
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                raise Exception(
                                   "\nDu willst gegen ein Auto fahren")
                self.insert()

    def right(self):
        if not self.horizontal[self.inp_car]:
            raise Exception("\nAuto hat falsche Ausrichtung!")
        else:
            self.hyp_new_coor = copy.deepcopy(self.cars)[self.inp_car]
            bo_wo_scar = np.delete(copy.deepcopy(
                self.cars), self.inp_car, axis=0)
            self.hyp_new_coor[:, 1] = [i+1 if not np.isnan(i) else i
                                       for i in self.hyp_new_coor[:, 1]]
            if np.any(
                    self.hyp_new_coor[:, 1] < 0) or np.any(
                    self.hyp_new_coor[:, 1] > 5):
                raise Exception("\nDu willst gegen eine Wand fahren")
            else:
                for c_coor in self.hyp_new_coor:
                    for car in bo_wo_scar:
                        for coor in car:
                            if c_coor.tolist() == coor.tolist():
                                raise Exception(
                                   "\nDu willst gegen ein Auto fahren")
                self.insert()

    def select(self):
        inp = self.get_input()
        inp_move = inp[1]
        self.inp_car = int(inp[0])-1
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


a = Rush_Hour(cars)
a.cars_in_board()
for i in range(10):
    a.select()
