# 큐브 모듈화

import wx
import random
import sqlite3 as sq
import time
import keyboard
import Cube2


class Cube:
    def __init__(self, mix_num=60, time=0.01):
        self.mix_num = mix_num
        self.time = time

    def Create_Cube(self):
        """큐브의 환경을 조성한다."""
        global Cube, CUBE
        global Resister, resister
        CUBE = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        Cube = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        Resister = [[[None, None, None], [None, None, None], [None, None, None], [None, None], [None], [None, None],
                     [None, None, None], [None, None], [None, None, None]],
                    [[None, None], [None], [None, None], [None], [None], [None], [None, None], [None], [None, None]],
                    [[None, None, None], [None, None], [None, None, None], [None, None], [None], [None, None],
                     [None, None, None], [None, None], [None, None, None]]]
        resister = [None, None, None]

    def Element_Right(self, floor, piece):
        """큐브의 모서리조각을 시계방향으로 돌려준다.  입력방식 : Element_Right(floor, piece)"""
        resister[0:3] = Cube[floor][piece][0:3]
        Cube[floor][piece][0] = resister[1]
        Cube[floor][piece][1] = resister[2]
        Cube[floor][piece][2] = resister[0]

    def Element_Left(self, floor, piece):
        """큐브의 모서리조각을 반시계방향으로 돌려준다.  입력방식 : Element_Left(floor, piece)"""
        resister[0:3] = Cube[floor][piece][0:3]
        Cube[floor][piece][0] = resister[2]
        Cube[floor][piece][1] = resister[0]
        Cube[floor][piece][2] = resister[1]

    def Element_Mirror(self, floor, piece):
        """큐브의 엣지조각을 반전시킨다.  입력방식 : Element_Mirror(floor, piece)"""
        resister[0:2] = Cube[floor][piece][0:2]
        Cube[floor][piece][0] = resister[1]
        Cube[floor][piece][1] = resister[0]

    def Up_Right(self):
        """윗면을 시계방향으로 회전한다."""
        Resister[0][0:9] = Cube[0][0:9]
        Cube[0][0] = Resister[0][2]
        Cube[0][1] = Resister[0][5]
        Cube[0][2] = Resister[0][8]
        Cube[0][3] = Resister[0][1]
        Cube[0][5] = Resister[0][7]
        Cube[0][6] = Resister[0][0]
        Cube[0][7] = Resister[0][3]
        Cube[0][8] = Resister[0][6]

    def Up_Left(self):
        """윗면을 시계 반대방향으로 회전한다."""
        Resister[0][0:9] = Cube[0][0:9]
        Cube[0][0] = Resister[0][6]
        Cube[0][1] = Resister[0][3]
        Cube[0][2] = Resister[0][0]
        Cube[0][3] = Resister[0][7]
        Cube[0][5] = Resister[0][1]
        Cube[0][6] = Resister[0][8]
        Cube[0][7] = Resister[0][5]
        Cube[0][8] = Resister[0][2]

    def Horizon_Right(self):
        """윗면과 아랫면 사이층을 시계방향으로 회전한다."""
        Resister[1][0:9] = Cube[1][0:9]
        Cube[1][0] = Resister[1][2]
        Cube[1][1] = Resister[1][5]
        Cube[1][2] = Resister[1][8]
        Cube[1][3] = Resister[1][1]
        Cube[1][5] = Resister[1][7]
        Cube[1][6] = Resister[1][0]
        Cube[1][7] = Resister[1][3]
        Cube[1][8] = Resister[1][6]
        self.Element_Mirror(1, 0)
        self.Element_Mirror(1, 2)
        self.Element_Mirror(1, 6)
        self.Element_Mirror(1, 8)

    def Horizon_Left(self):
        """윗면과 아랫면 사이층을 시계 반대방향으로 회전한다."""
        Resister[1][0:9] = Cube[1][0:9]
        Cube[1][0] = Resister[1][6]
        Cube[1][1] = Resister[1][3]
        Cube[1][2] = Resister[1][0]
        Cube[1][3] = Resister[1][7]
        Cube[1][5] = Resister[1][1]
        Cube[1][6] = Resister[1][8]
        Cube[1][7] = Resister[1][5]
        Cube[1][8] = Resister[1][2]
        self.Element_Mirror(1, 0)
        self.Element_Mirror(1, 2)
        self.Element_Mirror(1, 6)
        self.Element_Mirror(1, 8)

    def Down_Right(self):
        """아랫면을 시계방향으로 회전한다."""
        Resister[2][0:9] = Cube[2][0:9]
        Cube[2][0] = Resister[2][6]
        Cube[2][1] = Resister[2][3]
        Cube[2][2] = Resister[2][0]
        Cube[2][3] = Resister[2][7]
        Cube[2][5] = Resister[2][1]
        Cube[2][6] = Resister[2][8]
        Cube[2][7] = Resister[2][5]
        Cube[2][8] = Resister[2][2]

    def Down_Left(self):
        """아랫면을 시계 반대방향으로 회전한다."""
        Resister[2][0:9] = Cube[2][0:9]
        Cube[2][0] = Resister[2][2]
        Cube[2][1] = Resister[2][5]
        Cube[2][2] = Resister[2][8]
        Cube[2][3] = Resister[2][1]
        Cube[2][5] = Resister[2][7]
        Cube[2][6] = Resister[2][0]
        Cube[2][7] = Resister[2][3]
        Cube[2][8] = Resister[2][6]

    def Right_Right(self):
        """오른쪽 면을 시계방향으로 회전한다."""
        Resister[0][0:3] = Cube[0][0:3]
        Resister[1][0:3] = Cube[1][0:3]
        Resister[2][0:3] = Cube[2][0:3]
        Cube[0][0] = Resister[2][0]
        Cube[0][1] = Resister[1][0]
        Cube[0][2] = Resister[0][0]
        Cube[1][0] = Resister[2][1]
        Cube[1][2] = Resister[0][1]
        Cube[2][0] = Resister[2][2]
        Cube[2][1] = Resister[1][2]
        Cube[2][2] = Resister[0][2]
        self.Element_Left(0, 0)
        self.Element_Right(0, 2)
        self.Element_Right(2, 0)
        self.Element_Left(2, 2)

    def Right_Left(self):
        """오른쪽 면을 시계 반대방향으로 회전한다."""
        Resister[0][0:3] = Cube[0][0:3]
        Resister[1][0:3] = Cube[1][0:3]
        Resister[2][0:3] = Cube[2][0:3]
        Cube[0][0] = Resister[0][2]
        Cube[0][1] = Resister[1][2]
        Cube[0][2] = Resister[2][2]
        Cube[1][0] = Resister[0][1]
        Cube[1][2] = Resister[2][1]
        Cube[2][0] = Resister[0][0]
        Cube[2][1] = Resister[1][0]
        Cube[2][2] = Resister[2][0]
        self.Element_Left(0, 0)
        self.Element_Right(0, 2)
        self.Element_Right(2, 0)
        self.Element_Left(2, 2)

    def Middle_Right(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계방향으로 회전한다."""
        Resister[0][3:6] = Cube[0][3:6]
        Resister[1][3:6] = Cube[1][3:6]
        Resister[2][3:6] = Cube[2][3:6]
        Cube[0][3] = Resister[2][3]
        Cube[0][4] = Resister[1][3]
        Cube[0][5] = Resister[0][3]
        Cube[1][3] = Resister[2][4]
        Cube[1][5] = Resister[0][4]
        Cube[2][3] = Resister[2][5]
        Cube[2][4] = Resister[1][5]
        Cube[2][5] = Resister[0][5]
        self.Element_Mirror(0, 3)
        self.Element_Mirror(0, 5)
        self.Element_Mirror(2, 3)
        self.Element_Mirror(2, 5)

    def Middle_Left(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계 반대방향으로 회전한다."""
        Resister[0][3:6] = Cube[0][3:6]
        Resister[1][3:6] = Cube[1][3:6]
        Resister[2][3:6] = Cube[2][3:6]
        Cube[0][3] = Resister[0][5]
        Cube[0][4] = Resister[1][5]
        Cube[0][5] = Resister[2][5]
        Cube[1][3] = Resister[0][4]
        Cube[1][5] = Resister[2][4]
        Cube[2][3] = Resister[0][3]
        Cube[2][4] = Resister[1][3]
        Cube[2][5] = Resister[2][3]
        self.Element_Mirror(0, 3)
        self.Element_Mirror(0, 5)
        self.Element_Mirror(2, 3)
        self.Element_Mirror(2, 5)

    def Left_Right(self):
        """왼쪽 면을 시계방향으로 회전한다."""
        Resister[0][6:9] = Cube[0][6:9]
        Resister[1][6:9] = Cube[1][6:9]
        Resister[2][6:9] = Cube[2][6:9]
        Cube[0][6] = Resister[0][8]
        Cube[0][7] = Resister[1][8]
        Cube[0][8] = Resister[2][8]
        Cube[1][6] = Resister[0][7]
        Cube[1][8] = Resister[2][7]
        Cube[2][6] = Resister[0][6]
        Cube[2][7] = Resister[1][6]
        Cube[2][8] = Resister[2][6]
        self.Element_Right(0, 6)
        self.Element_Left(0, 8)
        self.Element_Left(2, 6)
        self.Element_Right(2, 8)

    def Left_Left(self):
        """왼쪽 면을 시계 반대방향으로 회전한다."""
        Resister[0][6:9] = Cube[0][6:9]
        Resister[1][6:9] = Cube[1][6:9]
        Resister[2][6:9] = Cube[2][6:9]
        Cube[0][6] = Resister[2][6]
        Cube[0][7] = Resister[1][6]
        Cube[0][8] = Resister[0][6]
        Cube[1][6] = Resister[2][7]
        Cube[1][8] = Resister[0][7]
        Cube[2][6] = Resister[2][8]
        Cube[2][7] = Resister[1][8]
        Cube[2][8] = Resister[0][8]
        self.Element_Right(0, 6)
        self.Element_Left(0, 8)
        self.Element_Left(2, 6)
        self.Element_Right(2, 8)

    def Front_Right(self):
        """앞면을 시계방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][6], Cube[0][3], Cube[0][0]]
        Resister[1][0:2] = [Cube[1][6], Cube[1][0]]
        Resister[2][0:3] = [Cube[2][6], Cube[2][3], Cube[2][0]]
        Cube[0][6] = Resister[2][0]
        Cube[0][3] = Resister[1][0]
        Cube[0][0] = Resister[0][0]
        Cube[1][6] = Resister[2][1]
        Cube[1][0] = Resister[0][1]
        Cube[2][6] = Resister[2][2]
        Cube[2][3] = Resister[1][1]
        Cube[2][0] = Resister[0][2]
        self.Element_Left(0, 6)
        self.Element_Mirror(0, 3)
        self.Element_Right(0, 0)
        self.Element_Mirror(1, 6)
        self.Element_Mirror(1, 0)
        self.Element_Right(2, 6)
        self.Element_Mirror(2, 3)
        self.Element_Left(2, 0)

    def Front_Left(self):
        """앞면을 시계 반대방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][6], Cube[0][3], Cube[0][0]]
        Resister[1][0:2] = [Cube[1][6], Cube[1][0]]
        Resister[2][0:3] = [Cube[2][6], Cube[2][3], Cube[2][0]]
        Cube[0][6] = Resister[0][2]
        Cube[0][3] = Resister[1][1]
        Cube[0][0] = Resister[2][2]
        Cube[1][6] = Resister[0][1]
        Cube[1][0] = Resister[2][1]
        Cube[2][6] = Resister[0][0]
        Cube[2][3] = Resister[1][0]
        Cube[2][0] = Resister[2][0]
        self.Element_Left(0, 6)
        self.Element_Mirror(0, 3)
        self.Element_Right(0, 0)
        self.Element_Mirror(1, 6)
        self.Element_Mirror(1, 0)
        self.Element_Right(2, 6)
        self.Element_Mirror(2, 3)
        self.Element_Left(2, 0)

    def Side_Right(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][7], Cube[0][4], Cube[0][1]]
        Resister[1][0:2] = [Cube[1][7], Cube[1][1]]
        Resister[2][0:3] = [Cube[2][7], Cube[2][4], Cube[2][1]]
        Cube[0][7] = Resister[2][0]
        Cube[0][4] = Resister[1][0]
        Cube[0][1] = Resister[0][0]
        Cube[1][7] = Resister[2][1]
        Cube[1][1] = Resister[0][1]
        Cube[2][7] = Resister[2][2]
        Cube[2][4] = Resister[1][1]
        Cube[2][1] = Resister[0][2]
        self.Element_Mirror(0, 7)
        self.Element_Mirror(0, 1)
        self.Element_Mirror(2, 7)
        self.Element_Mirror(2, 1)

    def Side_Left(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계 반대방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][7], Cube[0][4], Cube[0][1]]
        Resister[1][0:2] = [Cube[1][7], Cube[1][1]]
        Resister[2][0:3] = [Cube[2][7], Cube[2][4], Cube[2][1]]
        Cube[0][7] = Resister[0][2]
        Cube[0][4] = Resister[1][1]
        Cube[0][1] = Resister[2][2]
        Cube[1][7] = Resister[0][1]
        Cube[1][1] = Resister[2][1]
        Cube[2][7] = Resister[0][0]
        Cube[2][4] = Resister[1][0]
        Cube[2][1] = Resister[2][0]
        self.Element_Mirror(0, 7)
        self.Element_Mirror(0, 1)
        self.Element_Mirror(2, 7)
        self.Element_Mirror(2, 1)

    def Back_Right(self):
        """뒷면을 시계방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][8], Cube[0][5], Cube[0][2]]
        Resister[1][0:2] = [Cube[1][8], Cube[1][2]]
        Resister[2][0:3] = [Cube[2][8], Cube[2][5], Cube[2][2]]
        Cube[0][2] = Resister[2][2]
        Cube[0][5] = Resister[1][1]
        Cube[0][8] = Resister[0][2]
        Cube[1][2] = Resister[2][1]
        Cube[1][8] = Resister[0][1]
        Cube[2][2] = Resister[2][0]
        Cube[2][5] = Resister[1][0]
        Cube[2][8] = Resister[0][0]
        self.Element_Left(0, 2)
        self.Element_Mirror(0, 5)
        self.Element_Right(0, 8)
        self.Element_Mirror(1, 2)
        self.Element_Mirror(1, 8)
        self.Element_Right(2, 2)
        self.Element_Mirror(2, 5)
        self.Element_Left(2, 8)

    def Back_Left(self):
        """뒷면을 시계방향으로 회전한다."""
        Resister[0][0:3] = [Cube[0][8], Cube[0][5], Cube[0][2]]
        Resister[1][0:2] = [Cube[1][8], Cube[1][2]]
        Resister[2][0:3] = [Cube[2][8], Cube[2][5], Cube[2][2]]
        Cube[0][2] = Resister[0][0]
        Cube[0][5] = Resister[1][0]
        Cube[0][8] = Resister[2][0]
        Cube[1][2] = Resister[0][1]
        Cube[1][8] = Resister[2][1]
        Cube[2][2] = Resister[0][2]
        Cube[2][5] = Resister[1][1]
        Cube[2][8] = Resister[2][2]
        self.Element_Left(0, 2)
        self.Element_Mirror(0, 5)
        self.Element_Right(0, 8)
        self.Element_Mirror(1, 2)
        self.Element_Mirror(1, 8)
        self.Element_Right(2, 2)
        self.Element_Mirror(2, 5)
        self.Element_Left(2, 8)

    def X_Right(self):
        """큐브 전체를 앞면 축에 대해 시계방향으로 회전한다."""
        self.Front_Right()
        self.Side_Right()
        self.Back_Left()

    def X_Left(self):
        """큐브 전체를 앞면 축에 대해 시계 반대방향으로 회전한다."""
        self.Front_Left()
        self.Side_Left()
        self.Back_Right()

    def Y_Right(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계방향으로 회전한다."""
        self.Right_Right()
        self.Middle_Right()
        self.Left_Left()

    def Y_Left(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계 반대방향으로 회전한다."""
        self.Right_Left()
        self.Middle_Left()
        self.Left_Right()

    def Z_Right(self):
        """큐브 전체를 윗면의 축에 대해 시계방향으로 회전한다."""
        self.Up_Right()
        self.Horizon_Right()
        self.Down_Left()

    def Z_Left(self):
        """큐브 전체를 윗면의 축에 대해 시계 반대방향으로 회전한다."""
        self.Up_Left()
        self.Horizon_Left()
        self.Down_Right()

    def Clear_Cube(self):
        """큐브 전체를 24가지 경우로 돌려보며 모두 맞춰졌는지 판별하는 함수"""

        def If_Clear(self):
            """큐브의 모든 조각들의 요소가 맞춰져있는지 판별하는 함수."""
            if (CUBE[0][0] == Cube[0][0]):
                if (CUBE[0][1] == Cube[0][1]):
                    if (CUBE[0][2] == Cube[0][2]):
                        if (CUBE[0][3] == Cube[0][3]):
                            if (CUBE[0][4] == Cube[0][4]):
                                if (CUBE[0][5] == Cube[0][5]):
                                    if (CUBE[0][6] == Cube[0][6]):
                                        if (CUBE[0][7] == Cube[0][7]):
                                            if (CUBE[0][8] == Cube[0][8]):
                                                if (CUBE[1][0] == Cube[1][0]):
                                                    if (CUBE[1][1] == Cube[1][1]):
                                                        if (CUBE[1][2] == Cube[1][2]):
                                                            if (CUBE[1][3] == Cube[1][3]):
                                                                if (CUBE[1][5] == Cube[1][5]):
                                                                    if (CUBE[1][6] == Cube[1][6]):
                                                                        if (CUBE[1][7] == Cube[1][7]):
                                                                            if (CUBE[1][8] == Cube[1][8]):
                                                                                if (CUBE[2][0] == Cube[2][0]):
                                                                                    if (CUBE[2][1] == Cube[2][1]):
                                                                                        if (CUBE[2][2] == Cube[2][2]):
                                                                                            if (CUBE[2][3] == Cube[2][
                                                                                                3]):
                                                                                                if (CUBE[2][4] ==
                                                                                                        Cube[2][4]):
                                                                                                    if (CUBE[2][5] ==
                                                                                                            Cube[2][5]):
                                                                                                        if (CUBE[2][
                                                                                                            6] ==
                                                                                                                Cube[2][
                                                                                                                    6]):
                                                                                                            if (CUBE[2][
                                                                                                                7] ==
                                                                                                                    Cube[
                                                                                                                        2][
                                                                                                                        7]):
                                                                                                                if (
                                                                                                                        CUBE[
                                                                                                                            2][
                                                                                                                            8] ==
                                                                                                                        Cube[
                                                                                                                            2][
                                                                                                                            8]):
                                                                                                                    return 1
                                                                                                                else:
                                                                                                                    return 0
                                                                                                            else:
                                                                                                                return 0
                                                                                                        else:
                                                                                                            return 0
                                                                                                    else:
                                                                                                        return 0
                                                                                                else:
                                                                                                    return 0
                                                                                            else:
                                                                                                return 0
                                                                                        else:
                                                                                            return 0
                                                                                    else:
                                                                                        return 0
                                                                                else:
                                                                                    return 0
                                                                            else:
                                                                                return 0
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                                    else:
                                                        return 0
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0

        find1 = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        find2 = [[None, None, None, None], [None, None, None, None]]
        find3 = [None, None]

        for xy in range(4):
            for x in range(4):
                self.X_Right()
                if (self.If_Clear() == 1):
                    find1[xy][x] = 1
                else:
                    find1[xy][x] = 0
            self.Y_Right()

        for zxzx in range(2):
            self.Z_Right()
            for x in range(4):
                self.X_Right()
                if (self.If_Clear() == 1):
                    find2[zxzx][x] = 1
                else:
                    find2[zxzx][x] = 0
            self.Z_Right()
            self.X_Right()
            if (self.If_Clear() == 1):
                find3[zxzx] = 1
            else:
                find3[zxzx] = 0

        if (find1[0][0] == 1 or find1[0][1] == 1 or find1[0][2] == 1 or find1[0][3] == 1):
            return 0
        elif (find1[1][0] == 1 or find1[1][1] == 1 or find1[1][2] == 1 or find1[1][3] == 1):
            return 0
        elif (find1[2][0] == 1 or find1[2][1] == 1 or find1[2][2] == 1 or find1[2][3] == 1):
            return 0
        elif (find1[3][0] == 1 or find1[3][1] == 1 or find1[3][2] == 1 or find1[3][3] == 1):
            return 0
        elif (find2[0][0] == 1 or find2[0][1] == 1 or find2[0][2] == 1 or find2[0][3] == 1):
            return 0
        elif (find2[1][0] == 1 or find2[1][1] == 1 or find2[1][2] == 1 or find2[1][3] == 1):
            return 0
        elif (find3[0] == 1 or find3[1] == 1):
            return 0
        else:
            return 1

    def Mix_Cube(self):
        self.Cube_Mix_Ceed = random.randint(1, 18)

        if (self.Cube_Mix_Ceed == 1):
            self.Up_Right()
        elif (self.Cube_Mix_Ceed == 2):
            self.Up_Left()
        elif (self.Cube_Mix_Ceed == 3):
            self.Horizon_Right()
        elif (self.Cube_Mix_Ceed == 4):
            self.Horizon_Left()
        elif (self.Cube_Mix_Ceed == 5):
            self.Down_Right()
        elif (self.Cube_Mix_Ceed == 6):
            self.Down_Left()
        elif (self.Cube_Mix_Ceed == 7):
            self.Right_Right()
        elif (self.Cube_Mix_Ceed == 8):
            self.Right_Left()
        elif (self.Cube_Mix_Ceed == 9):
            self.Middle_Right()
        elif (self.Cube_Mix_Ceed == 10):
            self.Middle_Left()
        elif (self.Cube_Mix_Ceed == 11):
            self.Left_Right()
        elif (self.Cube_Mix_Ceed == 12):
            self.Left_Left()
        elif (self.Cube_Mix_Ceed == 13):
            self.Front_Right()
        elif (self.Cube_Mix_Ceed == 14):
            self.Front_Left()
        elif (self.Cube_Mix_Ceed == 15):
            self.Side_Right()
        elif (self.Cube_Mix_Ceed == 16):
            self.Side_Left()
        elif (self.Cube_Mix_Ceed == 17):
            self.Back_Right()
        elif (self.Cube_Mix_Ceed == 18):
            self.Back_Left()

    def save_Cube(self):
        """큐브 데이터를 저장하는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        self.def_Number()

        cursor.execute("""DROP TABLE IF EXISTS pieceAddr""")
        cursor.execute("""CREATE TABLE pieceAddr(Floor int, Position int, Element int)""")

        ElementList = (
            (Cube[0][0][0]), (Cube[0][0][1]), (Cube[0][0][2]),
            (Cube[0][1][0]), (Cube[0][1][1]),
            (Cube[0][2][0]), (Cube[0][2][1]), (Cube[0][2][2]),
            (Cube[0][3][0]), (Cube[0][3][1]),
            (Cube[0][4][0]),
            (Cube[0][5][0]), (Cube[0][5][1]),
            (Cube[0][6][0]), (Cube[0][6][1]), (Cube[0][6][2]),
            (Cube[0][7][0]), (Cube[0][7][1]),
            (Cube[0][8][0]), (Cube[0][8][1]), (Cube[0][8][2]),
            (Cube[1][0][0]), (Cube[1][0][1]),
            (Cube[1][1][0]),
            (Cube[1][2][0]), (Cube[1][2][1]),
            (Cube[1][3][0]),
            (Cube[1][5][0]),
            (Cube[1][6][0]), (Cube[1][6][1]),
            (Cube[1][7][0]),
            (Cube[1][8][0]), (Cube[1][8][1]),
            (Cube[2][0][0]), (Cube[2][0][1]), (Cube[2][0][2]),
            (Cube[2][1][0]), (Cube[2][1][1]),
            (Cube[2][2][0]), (Cube[2][2][1]), (Cube[2][2][2]),
            (Cube[2][3][0]), (Cube[2][3][1]),
            (Cube[2][4][0]),
            (Cube[2][5][0]), (Cube[2][5][1]),
            (Cube[2][6][0]), (Cube[2][6][1]), (Cube[2][6][2]),
            (Cube[2][7][0]), (Cube[2][7][1]),
            (Cube[2][8][0]), (Cube[2][8][1]), (Cube[2][8][2]),
        )

        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 0, ElementList[0]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 1, ElementList[1]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 2, ElementList[2]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 3, ElementList[3]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 4, ElementList[4]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 5, ElementList[5]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 6, ElementList[6]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 7, ElementList[7]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 8, ElementList[8]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 9, ElementList[9]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 10, ElementList[10]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 11, ElementList[11]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 12, ElementList[12]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 13, ElementList[13]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 14, ElementList[14]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 15, ElementList[15]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 16, ElementList[16]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 17, ElementList[17]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 18, ElementList[18]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 19, ElementList[19]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 20, ElementList[20]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 21, ElementList[21]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 22, ElementList[22]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 23, ElementList[23]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 24, ElementList[24]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 25, ElementList[25]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 26, ElementList[26]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 27, ElementList[27]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 28, ElementList[28]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 29, ElementList[29]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 30, ElementList[30]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 31, ElementList[31]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 32, ElementList[32]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 33, ElementList[33]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 34, ElementList[34]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 35, ElementList[35]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 36, ElementList[36]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 37, ElementList[37]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 38, ElementList[38]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 39, ElementList[39]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 40, ElementList[40]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 41, ElementList[41]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 42, ElementList[42]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 43, ElementList[43]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 44, ElementList[44]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 45, ElementList[45]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 46, ElementList[46]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 47, ElementList[47]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 48, ElementList[48]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 49, ElementList[49]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 50, ElementList[50]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 51, ElementList[51]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 52, ElementList[52]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (2, 53, ElementList[53]))

        self.def_Color()

        con.commit()

        cursor.close()
        con.close()

    def Load_Cube(self):
        """저장했던 큐브 데이터를 불러오는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        NUM = []
        for n in range(54):
            NUM.append(n)
        for n in range(54):
            NUM[n] = n

        ElementList = []
        for x in range(54):
            ElementList.append(x)

        for x in range(54):
            cursor.execute("SELECT Element FROM pieceAddr WHERE Position = '%d'" % x)
            ElementList[x] = cursor.fetchone()

        Cube[0][0][0] = ElementList[0][0]
        Cube[0][0][1] = ElementList[1][0]
        Cube[0][0][2] = ElementList[2][0]
        Cube[0][1][0] = ElementList[3][0]
        Cube[0][1][1] = ElementList[4][0]
        Cube[0][2][0] = ElementList[5][0]
        Cube[0][2][1] = ElementList[6][0]
        Cube[0][2][2] = ElementList[7][0]
        Cube[0][3][0] = ElementList[8][0]
        Cube[0][3][1] = ElementList[9][0]
        Cube[0][4][0] = ElementList[10][0]
        Cube[0][5][0] = ElementList[11][0]
        Cube[0][5][1] = ElementList[12][0]
        Cube[0][6][0] = ElementList[13][0]
        Cube[0][6][1] = ElementList[14][0]
        Cube[0][6][2] = ElementList[15][0]
        Cube[0][7][0] = ElementList[16][0]
        Cube[0][7][1] = ElementList[17][0]
        Cube[0][8][0] = ElementList[18][0]
        Cube[0][8][1] = ElementList[19][0]
        Cube[0][8][2] = ElementList[20][0]
        Cube[1][0][0] = ElementList[21][0]
        Cube[1][0][1] = ElementList[22][0]
        Cube[1][1][0] = ElementList[23][0]
        Cube[1][2][0] = ElementList[24][0]
        Cube[1][2][1] = ElementList[25][0]
        Cube[1][3][0] = ElementList[26][0]
        Cube[1][5][0] = ElementList[27][0]
        Cube[1][6][0] = ElementList[28][0]
        Cube[1][6][1] = ElementList[29][0]
        Cube[1][7][0] = ElementList[30][0]
        Cube[1][8][0] = ElementList[31][0]
        Cube[1][8][1] = ElementList[32][0]
        Cube[2][0][0] = ElementList[33][0]
        Cube[2][0][1] = ElementList[34][0]
        Cube[2][0][2] = ElementList[35][0]
        Cube[2][1][0] = ElementList[36][0]
        Cube[2][1][1] = ElementList[37][0]
        Cube[2][2][0] = ElementList[38][0]
        Cube[2][2][1] = ElementList[39][0]
        Cube[2][2][2] = ElementList[40][0]
        Cube[2][3][0] = ElementList[41][0]
        Cube[2][3][1] = ElementList[42][0]
        Cube[2][4][0] = ElementList[43][0]
        Cube[2][5][0] = ElementList[44][0]
        Cube[2][5][1] = ElementList[45][0]
        Cube[2][6][0] = ElementList[46][0]
        Cube[2][6][1] = ElementList[47][0]
        Cube[2][6][2] = ElementList[48][0]
        Cube[2][7][0] = ElementList[49][0]
        Cube[2][7][1] = ElementList[50][0]
        Cube[2][8][0] = ElementList[51][0]
        Cube[2][8][1] = ElementList[52][0]
        Cube[2][8][2] = ElementList[53][0]

        self.def_Color()

        con.commit()

        cursor.close()
        con.close()

    def dist_Color(self, floor, piece, color):
        """각 큐브 조각의 색을 디코딩"""
        if (Cube[floor][piece][color] == 1):
            Cube[floor][piece][color] = wx.YELLOW
        elif (Cube[floor][piece][color] == 2):
            Cube[floor][piece][color] = wx.BLUE
        elif (Cube[floor][piece][color] == 3):
            Cube[floor][piece][color] = wx.RED
        elif (Cube[floor][piece][color] == 4):
            Cube[floor][piece][color] = wx.Colour(0, 150, 0, 0)
        elif (Cube[floor][piece][color] == 5):
            Cube[floor][piece][color] = wx.Colour(250, 125, 0, 0)
        elif (Cube[floor][piece][color] == 6):
            Cube[floor][piece][color] = wx.WHITE
        else:
            return 0

    def def_Color(self):
        """각 큐브조각의 값을 색으로 변환하는 함수"""
        for i in range(0, 3, 2):
            self.dist_Color(i, 4, 0)
            for l in range(1, 5):
                for m in range(2):
                    self.dist_Color(i, 2 * l - 1, m)
            for n in range(2):
                self.dist_Color(1, i, n)
                self.dist_Color(1, i + 6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.dist_Color(i, j, k)
                    self.dist_Color(i, j + 6, k)
        for p in range(4):
            self.dist_Color(1, 2 * p + 1, 0)

    def dist_Number(self, floor, piece, color):
        """각 큐브 조각의 색을 데이터로 인코딩"""
        if (Cube[floor][piece][color] == wx.YELLOW):
            Cube[floor][piece][color] = 1
        elif (Cube[floor][piece][color] == wx.BLUE):
            Cube[floor][piece][color] = 2
        elif (Cube[floor][piece][color] == wx.RED):
            Cube[floor][piece][color] = 3
        elif (Cube[floor][piece][color] == wx.Colour(0, 150, 0, 0)):
            Cube[floor][piece][color] = 4
        elif (Cube[floor][piece][color] == wx.Colour(250, 125, 0, 0)):
            Cube[floor][piece][color] = 5
        elif (Cube[floor][piece][color] == wx.WHITE):
            Cube[floor][piece][color] = 6
        else:
            return 0

    def def_Number(self):
        """각 큐브조각의 색을 데이터로 변환하는 함수"""
        for i in range(0, 3, 2):
            self.dist_Number(i, 4, 0)
            for l in range(1, 5):
                for m in range(2):
                    self.dist_Number(i, 2 * l - 1, m)
            for n in range(2):
                self.dist_Number(1, i, n)
                self.dist_Number(1, i + 6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.dist_Number(i, j, k)
                    self.dist_Number(i, j + 6, k)
        for p in range(4):
            self.dist_Number(1, 2 * p + 1, 0)

    #
    #    함수
    #    종료
    #


# import wx
# import time
# import Cube2
# import keyboard

Cube2 = Cube(mix_num=60, time=0.01)
MIX_NUM = 60
TIME = 0.01

Cube2.Create_Cube()
Cube2.def_Color()

app = wx.App(0)

start_frame = wx.Frame(None, title='큐브 2.2ver')
main_frame = wx.Frame(None, title="큐브 리모컨")

Cube_up = wx.Frame(main_frame, title="큐브 윗면")
Cube_front = wx.Frame(main_frame, title="큐브 앞면")
Cube_down = wx.Frame(main_frame, title="큐브 밑면")
Cube_right = wx.Frame(main_frame, title="큐브 오른쪽면")
Cube_left = wx.Frame(main_frame, title="큐브 왼쪽면")
Cube_back = wx.Frame(main_frame, title="큐브 뒷면")

Cube_Graphic_Option = wx.Frame(main_frame, title="큐브그래픽 화면설정")
Cube_Graphic_Option.SetSize(wx.Size(200, 250))
Cube_Graphic_Option.SetPosition(wx.Point(700, 250))
Cube_Graphic_Option.SetWindowStyle(wx.CAPTION)

implementation_frame = wx.Frame(None, title="큐브 1.0ver")
implementation_frame.SetSize(wx.Size(200, 250))
implementation_frame.SetPosition(wx.Point(700, 250))
implementation_frame.SetWindowStyle(wx.CAPTION)

# 메인 프레임(메인 리모콘 윈도우)
main_frame.SetPosition(wx.Point(650, 200))
main_frame.SetSize(wx.Size(470, 330))

# 시작화면
start_frame.SetPosition(wx.Point(450, 400))
start_frame.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
start_frame.SetBackgroundColour(wx.WHITE)
# for x in range(254):
#    for y in range(254):
#        for z in range(254):
#            time.sleep(0.2)
#            frame2.SetBackgroundColour(wx.Colour(x, y, z, 0))
#            frame2.Refresh()


# 큐브윗면 프레임

Cube_up.SetSize(wx.Size(182, 182))
Cube_up.SetPosition(wx.Point(250, 70))
Cube_up.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_up.SetWindowStyle(wx.SYSTEM_MENU)

# 큐브앞면 프레임

Cube_front.SetSize(wx.Size(182, 182))
Cube_front.SetPosition(wx.Point(250, 250))
Cube_front.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_front.SetWindowStyle(wx.SYSTEM_MENU)

# 큐브밑면 프레임

Cube_down.SetSize(wx.Size(182, 182))
Cube_down.SetPosition(wx.Point(250, 430))
Cube_down.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_down.SetWindowStyle(wx.SYSTEM_MENU)

# 큐브오른쪽면 프레임

Cube_right.SetSize(wx.Size(182, 182))
Cube_right.SetPosition(wx.Point(430, 250))
Cube_right.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_right.SetWindowStyle(wx.SYSTEM_MENU)

# 큐브왼쪽면 프레임

Cube_left.SetSize(wx.Size(182, 182))
Cube_left.SetPosition(wx.Point(70, 250))
Cube_left.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_left.SetWindowStyle(wx.SYSTEM_MENU)

# 큐브뒷면 프레임

Cube_back.SetSize(wx.Size(182, 182))
Cube_back.SetPosition(wx.Point(250, 625))
Cube_back.SetBackgroundColour(wx.Colour(100, 100, 100, 0))
Cube_back.SetWindowStyle(wx.SYSTEM_MENU)

# ## 시작화면 셋팅

btn = wx.Button(start_frame, label="시작")


def OnClick(event):
    wx.MessageBox("큐브 2.2ver 프로그램을 시작합니다!", "알림", wx.OK)
    start_frame.Close()
    main_frame.Show(True)
    Cube_up.Show(True)
    Cube_front.Show(True)
    Cube_down.Show(True)
    Cube_right.Show(True)
    Cube_left.Show(True)
    Cube_back.Show(True)


btn.Bind(wx.EVT_BUTTON, OnClick)

empty1 = wx.StaticText(start_frame, label=" ")
empty2 = wx.StaticText(start_frame, label=" ")
lbl1 = wx.StaticText(start_frame, label="큐브 2.2 \n")
lbl2 = wx.StaticText(start_frame, label="Cube 2.2 ver")
lbl3 = wx.StaticText(start_frame, label="Made By 한승준")

box = wx.BoxSizer(wx.VERTICAL)
start_frame.SetSizer(box)
box.Add(empty1, border=50, flag=wx.TOP)
box.Add(lbl1, flag=wx.ALIGN_CENTER)
box.Add(btn, flag=wx.ALIGN_CENTER)
box.Add(empty2, border=40, flag=wx.TOP)
box.Add(lbl2, flag=wx.ALIGN_RIGHT)
box.Add(lbl3, flag=wx.ALIGN_RIGHT)


# 큐브윗면 그래픽 디자인

def On_UP_Paint(event):
    dc = wx.PaintDC(Cube_up)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][8][0]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][5][0]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][2][0]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][7][0]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][4][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][1][0]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][6][0]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][3][0]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][0][0]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)


# 큐브앞면 그래픽 디자인

def On_FRONT_Paint(event):
    dc = wx.PaintDC(Cube_front)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][6][2]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][3][1]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][0][1]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][6][0]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][3][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][0][0]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][6][1]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][3][1]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][0][2]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)


# 큐브밑면 그래픽 디자인

def On_DOWN_Paint(event):
    dc = wx.PaintDC(Cube_down)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][6][0]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][3][0]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][0][0]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][7][0]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][4][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][1][0]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][8][0]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][5][0]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][2][0]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)


# 큐브오른쪽면 디자인

def On_RIGHT_Paint(event):
    dc = wx.PaintDC(Cube_right)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][0][2]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][1][1]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][2][1]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][0][1]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][1][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][2][1]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][0][1]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][1][1]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][2][2]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)


# 큐브왼쪽면 디자인

def On_LEFT_Paint(event):
    dc = wx.PaintDC(Cube_left)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][8][2]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][7][1]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][6][1]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][8][1]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][7][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][6][1]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][8][1]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][7][1]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][6][2]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)


# 큐브뒷면 디자인

def On_BACK_Paint(event):
    dc = wx.PaintDC(Cube_back)
    dc.SetPen(wx.BLACK_PEN)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][2][2]))
    dc.DrawRectangle(0, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][5][1]))
    dc.DrawRectangle(60, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[0][8][1]))
    dc.DrawRectangle(120, 0, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][2][0]))
    dc.DrawRectangle(0, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][5][0]))
    dc.DrawRectangle(60, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[1][8][0]))
    dc.DrawRectangle(120, 60, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][2][1]))
    dc.DrawRectangle(0, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][5][1]))
    dc.DrawRectangle(60, 120, 60, 60)
    dc.SetBrush(wx.Brush(Cube2.Cube[2][8][2]))
    dc.DrawRectangle(120, 120, 60, 60)


Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)

### 메인 리모콘 윈도우 셋팅 (버튼 & 설명)

panel_Btn = wx.Panel(main_frame)
U_R = wx.Button(panel_Btn, label="U")
U_L = wx.Button(panel_Btn, label="U'")
H_R = wx.Button(panel_Btn, label="H")
H_L = wx.Button(panel_Btn, label="H'")
D_R = wx.Button(panel_Btn, label="D")
D_L = wx.Button(panel_Btn, label="D'")
R_R = wx.Button(panel_Btn, label="R")
R_L = wx.Button(panel_Btn, label="R'")
M_R = wx.Button(panel_Btn, label="M")
M_L = wx.Button(panel_Btn, label="M'")
L_R = wx.Button(panel_Btn, label="L")
L_L = wx.Button(panel_Btn, label="L'")
F_R = wx.Button(panel_Btn, label="F")
F_L = wx.Button(panel_Btn, label="F'")
S_R = wx.Button(panel_Btn, label="S")
S_L = wx.Button(panel_Btn, label="S'")
B_R = wx.Button(panel_Btn, label="B")
B_L = wx.Button(panel_Btn, label="B'")
X_R = wx.Button(panel_Btn, label="X")
X_L = wx.Button(panel_Btn, label="X'")
Y_R = wx.Button(panel_Btn, label="Y")
Y_L = wx.Button(panel_Btn, label="Y'")
Z_R = wx.Button(panel_Btn, label="Z")
Z_L = wx.Button(panel_Btn, label="Z'")

panel_Inform = wx.Panel(main_frame)
Inform1 = wx.StaticText(panel_Inform, label="큐브 회전은 키보드 입력으로도 가능합니다. (예: 오른쪽 면 시계방향 회전은 r 입력.)")
Inform2 = wx.StaticText(panel_Inform, label="반시계방향 회전은 쉬프트를 누른 상태로 입력합니다.")
Inform3 = wx.StaticText(panel_Inform, label="저장 및 불러오기는 각각 Ctrl+S, Ctrl+L을 입력합니다.(나머지 단축키는 메뉴를 참조)")

grid = wx.GridSizer(6, 4, 15, 15)
grid.Add(U_R, 0, wx.SHAPED)
grid.Add(H_R, 0, wx.SHAPED)
grid.Add(D_R, 0, wx.SHAPED)
grid.Add(Z_R, 0, wx.SHAPED)
grid.Add(U_L, 0, wx.SHAPED)
grid.Add(H_L, 0, wx.SHAPED)
grid.Add(D_L, 0, wx.SHAPED)
grid.Add(Z_L, 0, wx.SHAPED)
grid.Add(R_R, 0, wx.SHAPED)
grid.Add(M_R, 0, wx.SHAPED)
grid.Add(L_R, 0, wx.SHAPED)
grid.Add(Y_R, 0, wx.SHAPED)
grid.Add(R_L, 0, wx.SHAPED)
grid.Add(M_L, 0, wx.SHAPED)
grid.Add(L_L, 0, wx.SHAPED)
grid.Add(Y_L, 0, wx.SHAPED)
grid.Add(F_R, 0, wx.SHAPED)
grid.Add(S_R, 0, wx.SHAPED)
grid.Add(B_R, 0, wx.SHAPED)
grid.Add(X_R, 0, wx.SHAPED)
grid.Add(F_L, 0, wx.SHAPED)
grid.Add(S_L, 0, wx.SHAPED)
grid.Add(B_L, 0, wx.SHAPED)
grid.Add(X_L, 0, wx.SHAPED)
panel_Btn.SetSizer(grid)

Inform1.SetPosition(wx.Point(0, 0))
Inform2.SetPosition(wx.Point(0, 20))
Inform3.SetPosition(wx.Point(0, 40))

box = wx.BoxSizer(wx.VERTICAL)
main_frame.SetSizer(box)
box.Add(panel_Btn)
box.Add(panel_Inform)


# 큐브 회전이벤트 함수 생성

def spin_U():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


def spin_H():
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


def spin_D():
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


def spin_R():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


def spin_M():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


def spin_L():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


def spin_F():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


def spin_S():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


def spin_B():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


def spin_All():
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


# 키보드 이벤트 설정(단축키 지정 및 키보드 입력 이벤트)

def SAVE():
    Cube2.Side_Left()
    spin_S()
    dialog1 = wx.MessageDialog(main_frame, "저장하시겠습니까?", "저장", wx.CANCEL)
    if dialog1.ShowModal() == wx.ID_OK:
        Cube2.save_Cube()
        wx.MessageBox("저장했습니다!", "알림", wx.OK)
    else:
        pass
    dialog1.Destroy()


keyboard.add_hotkey('ctrl+s', lambda: SAVE())


def LOAD():
    Cube2.Left_Left()
    spin_L()
    dialog2 = wx.MessageDialog(main_frame, "저장파일을 불러오시겠습니까?", "불러오기", wx.CANCEL)
    if dialog2.ShowModal() == wx.ID_OK:
        Cube2.Load_Cube()
        Cube_up.Refresh()
        Cube_front.Refresh()
        Cube_right.Refresh()
        Cube_left.Refresh()
        Cube_back.Refresh()
        Cube_down.Refresh()
    else:
        pass
    dialog2.Destroy()


keyboard.add_hotkey('ctrl+l', lambda: LOAD())


def MIX():
    for mix_num in range(MIX_NUM):
        Cube2.def_Number()
        Cube2.Mix_Cube()
        time.sleep(TIME)
        Cube2.def_Color()
        spin_All()


keyboard.add_hotkey('ctrl+m', lambda: MIX())


def CLEAN():
    Cube2.Create_Cube()
    Cube2.def_Color()
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


keyboard.add_hotkey('ctrl+c', lambda: CLEAN())


def QUIT():
    dialog = wx.MessageDialog(main_frame, "종료하시겠습니까?", "종료", wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        main_frame.Close()
    else:
        pass
    dialog.Destroy()


keyboard.add_hotkey('ctrl+q', lambda: QUIT())


def Left_U():
    Cube2.Up_Left()
    Cube2.Up_Left()
    spin_U()
    time.sleep(TIME)


keyboard.add_hotkey("shift+u", lambda: Left_U())


def Left_H():
    Cube2.Horizon_Left()
    Cube2.Horizon_Left()
    spin_H()
    time.sleep(TIME)


keyboard.add_hotkey("shift+h", lambda: Left_H())


def Left_D():
    Cube2.Down_Left()
    Cube2.Down_Left()
    spin_D()
    time.sleep(TIME)


keyboard.add_hotkey("shift+d", lambda: Left_D())


def Left_R():
    Cube2.Right_Left()
    Cube2.Right_Left()
    spin_R()
    time.sleep(TIME)


keyboard.add_hotkey("shift+r", lambda: Left_R())


def Left_M():
    Cube2.Middle_Left()
    Cube2.Middle_Left()
    spin_M()
    time.sleep(TIME)


keyboard.add_hotkey("shift+m", lambda: Left_M())


def Left_L():
    Cube2.Left_Left()
    Cube2.Left_Left()
    spin_L()
    time.sleep(TIME)


keyboard.add_hotkey("shift+l", lambda: Left_L())


def Left_F():
    Cube2.Front_Left()
    Cube2.Front_Left()
    spin_F()
    time.sleep(TIME)


keyboard.add_hotkey("shift+f", lambda: Left_F())


def Left_S():
    Cube2.Side_Left()
    Cube2.Side_Left()
    spin_S()
    time.sleep(TIME)


keyboard.add_hotkey("shift+s", lambda: Left_S())


def Left_B():
    Cube2.Back_Left()
    Cube2.Back_Left()
    spin_B()
    time.sleep(TIME)


keyboard.add_hotkey("shift+b", lambda: Left_B())


def Left_X():
    Cube2.X_Left()
    Cube2.X_Left()
    spin_All()
    time.sleep(TIME)


keyboard.add_hotkey("shift+x", lambda: Left_X())


def Left_Y():
    Cube2.Y_Left()
    Cube2.Y_Left()
    spin_All()
    time.sleep(TIME)


keyboard.add_hotkey("shift+y", lambda: Left_Y())


def Left_Z():
    Cube2.Z_Left()
    Cube2.Z_Left()
    spin_All()
    time.sleep(TIME)


keyboard.add_hotkey("shift+z", lambda: Left_Z())


def on_Key(event):
    if keyboard.is_pressed('u'):
        Cube2.Up_Right()
        spin_U()
        time.sleep(TIME)
    elif keyboard.is_pressed('h'):
        Cube2.Horizon_Right()
        spin_H()
        time.sleep(TIME)
    elif keyboard.is_pressed('d'):
        Cube2.Down_Right()
        spin_D()
        time.sleep(TIME)
    elif keyboard.is_pressed('r'):
        Cube2.Right_Right()
        spin_R()
        time.sleep(TIME)
    elif keyboard.is_pressed('m'):
        Cube2.Middle_Right()
        spin_M()
        time.sleep(TIME)
    elif keyboard.is_pressed('l'):
        Cube2.Left_Right()
        spin_L()
        time.sleep(TIME)
    elif keyboard.is_pressed('f'):
        Cube2.Front_Right()
        spin_F()
        time.sleep(TIME)
    elif keyboard.is_pressed('s'):
        Cube2.Side_Right()
        spin_S()
        time.sleep(TIME)
    elif keyboard.is_pressed('b'):
        Cube2.Back_Right()
        spin_B()
        time.sleep(TIME)
    elif keyboard.is_pressed('x'):
        Cube2.X_Right()
        spin_All()
        time.sleep(TIME)
    elif keyboard.is_pressed('y'):
        Cube2.Y_Right()
        spin_All()
        time.sleep(TIME)
    elif keyboard.is_pressed('z'):
        Cube2.Z_Right()
        spin_All()
        time.sleep(TIME)
    else:
        pass


main_frame.Bind(wx.EVT_KEY_DOWN, on_Key)


# 버튼 이벤트 설정

def onU_R(event):
    Cube2.Up_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


U_R.Bind(wx.EVT_BUTTON, onU_R)


def onU_L(event):
    Cube2.Up_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


U_L.Bind(wx.EVT_BUTTON, onU_L)


def onH_R(event):
    Cube2.Horizon_Right()
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


H_R.Bind(wx.EVT_BUTTON, onH_R)


def onH_L(event):
    Cube2.Horizon_Left()
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


H_L.Bind(wx.EVT_BUTTON, onH_L)


def onD_R(event):
    Cube2.Down_Right()
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


D_R.Bind(wx.EVT_BUTTON, onD_R)


def onD_L(event):
    Cube2.Down_Left()
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


D_L.Bind(wx.EVT_BUTTON, onD_L)


def onR_R(event):
    Cube2.Right_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


R_R.Bind(wx.EVT_BUTTON, onR_R)


def onR_L(event):
    Cube2.Right_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


R_L.Bind(wx.EVT_BUTTON, onR_L)


def onM_R(event):
    Cube2.Middle_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


M_R.Bind(wx.EVT_BUTTON, onM_R)


def onM_L(event):
    Cube2.Middle_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


M_L.Bind(wx.EVT_BUTTON, onM_L)


def onL_R(event):
    Cube2.Left_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


L_R.Bind(wx.EVT_BUTTON, onL_R)


def onL_L(event):
    Cube2.Left_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


L_L.Bind(wx.EVT_BUTTON, onL_L)


def onF_R(event):
    Cube2.Front_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


F_R.Bind(wx.EVT_BUTTON, onF_R)


def onF_L(event):
    Cube2.Front_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


F_L.Bind(wx.EVT_BUTTON, onF_L)


def onS_R(event):
    Cube2.Side_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


S_R.Bind(wx.EVT_BUTTON, onS_R)


def onS_L(event):
    Cube2.Side_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_up.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_down.Refresh()


S_L.Bind(wx.EVT_BUTTON, onS_L)


def onB_R(event):
    Cube2.Back_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


B_R.Bind(wx.EVT_BUTTON, onB_R)


def onB_L(event):
    Cube2.Back_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_down.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()


B_L.Bind(wx.EVT_BUTTON, onB_L)


def onX_R(event):
    Cube2.X_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


X_R.Bind(wx.EVT_BUTTON, onX_R)


def onX_L(event):
    Cube2.X_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


X_L.Bind(wx.EVT_BUTTON, onX_L)


def onY_R(event):
    Cube2.Y_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


Y_R.Bind(wx.EVT_BUTTON, onY_R)


def onY_L(event):
    Cube2.Y_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


Y_L.Bind(wx.EVT_BUTTON, onY_L)


def onZ_R(event):
    Cube2.Z_Right()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


Z_R.Bind(wx.EVT_BUTTON, onZ_R)


def onZ_L(event):
    Cube2.Z_Left()
    Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
    Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
    Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
    Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
    Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
    Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


Z_L.Bind(wx.EVT_BUTTON, onZ_L)

# 메인 프레임 메뉴바
menubar = wx.MenuBar()
menu = wx.Menu()
menubar.Append(menu, "File")

edit = wx.Menu()
menubar.Append(edit, "Edit")

tool = wx.Menu()
menubar.Append(tool, "Tool")

option = wx.Menu()
menubar.Append(option, "Option")

# 메뉴-파일

about = wx.MenuItem(id=wx.ID_ANY, text='소개')
menu.Append(about)
menu.AppendSeparator()

save = wx.MenuItem(id=wx.ID_ANY, text="저장(ctrl+S)")
menu.Append(save)
menu.AppendSeparator()

load = wx.MenuItem(id=wx.ID_ANY, text="불러오기(ctrl+L)")
menu.Append(load)
menu.AppendSeparator()

quit = wx.MenuItem(id=wx.ID_ANY, text="종료(ctrl+Q)")
menu.Append(quit)
menu.AppendSeparator()

# 메뉴-편집

u_r = wx.MenuItem(id=wx.ID_ANY, text="윗면을 시계방향으로 회전(U)")
edit.Append(u_r)
edit.AppendSeparator()

u_l = wx.MenuItem(id=wx.ID_ANY, text="윗면을 반시계방향으로 회전(Shift+U')")
edit.Append(u_l)
edit.AppendSeparator()

h_r = wx.MenuItem(id=wx.ID_ANY, text='윗면과 아랫면 사이층을 시계방향으로 회전(H)')
edit.Append(h_r)
edit.AppendSeparator()

h_l = wx.MenuItem(id=wx.ID_ANY, text="윗면과 아랫면 사이층을 반시계방향으로 회전(Shift+H')")
edit.Append(h_l)
edit.AppendSeparator()

d_r = wx.MenuItem(id=wx.ID_ANY, text='아랫면을 시계방향으로 회전(D)')
edit.Append(d_r)
edit.AppendSeparator()

d_l = wx.MenuItem(id=wx.ID_ANY, text="아랫면을 반시계방향으로 회전(Shift+D')")
edit.Append(d_l)
edit.AppendSeparator()

r_r = wx.MenuItem(id=wx.ID_ANY, text='오른쪽면을 시계방향으로 회전(R)')
edit.Append(r_r)
edit.AppendSeparator()

r_l = wx.MenuItem(id=wx.ID_ANY, text="오른쪽면을 반시계방향으로 회전(Shift+R')")
edit.Append(r_l)
edit.AppendSeparator()

m_r = wx.MenuItem(id=wx.ID_ANY, text='오른쪽면과 왼쪽면의 사이층을 시계방향으로 회전(M)')
edit.Append(m_r)
edit.AppendSeparator()

m_l = wx.MenuItem(id=wx.ID_ANY, text="오른쪽면과 왼쪽면의 사이층을 반시계방향으로 회전(Shift+M')")
edit.Append(m_l)
edit.AppendSeparator()

l_r = wx.MenuItem(id=wx.ID_ANY, text="왼쪽면을 시계방향으로 회전(L)")
edit.Append(l_r)
edit.AppendSeparator()

l_l = wx.MenuItem(id=wx.ID_ANY, text="왼쪽면을 반시계방향으로 회전(Shift+L')")
edit.Append(l_l)
edit.AppendSeparator()

f_r = wx.MenuItem(id=wx.ID_ANY, text="앞면을 시계방향으로 회전(F)")
edit.Append(f_r)
edit.AppendSeparator()

f_l = wx.MenuItem(id=wx.ID_ANY, text="앞면을 반시계방향으로 회전(Shift+F')")
edit.Append(f_l)
edit.AppendSeparator()

s_r = wx.MenuItem(id=wx.ID_ANY, text='앞면과 뒷면의 사이층을 시계방향으로 회전(S)')
edit.Append(s_r)
edit.AppendSeparator()

s_l = wx.MenuItem(id=wx.ID_ANY, text="앞면과 뒷면의 사이층을 반시계방향으로 회전(Shift+S')")
edit.Append(s_l)
edit.AppendSeparator()

b_r = wx.MenuItem(id=wx.ID_ANY, text='뒷면을 시계방향으로 회전(B)')
edit.Append(b_r)
edit.AppendSeparator()

b_l = wx.MenuItem(id=wx.ID_ANY, text="뒷면을 반시계방향으로 회전(Shift+B')")
edit.Append(b_l)
edit.AppendSeparator()

x_r = wx.MenuItem(id=wx.ID_ANY, text='앞면을 축으로 큐브전체를 시계방향으로 회전(X)')
edit.Append(x_r)
edit.AppendSeparator()

x_l = wx.MenuItem(id=wx.ID_ANY, text="앞면을 축으로 큐브전체를 반시계방향으로 회전(Shift+X')")
edit.Append(x_l)
edit.AppendSeparator()

y_r = wx.MenuItem(id=wx.ID_ANY, text='오른쪽면을 축으로 큐브전체를 시계방향으로 회전(Y)')
edit.Append(y_r)
edit.AppendSeparator()

y_l = wx.MenuItem(id=wx.ID_ANY, text="오른쪽면을 축으로 큐브전체를 반시계방향으로 회전(Shift+Y')")
edit.Append(y_l)
edit.AppendSeparator()

z_r = wx.MenuItem(id=wx.ID_ANY, text='윗면을 축으로 시계방향으로 회전(Z)')
edit.Append(z_r)
edit.AppendSeparator()

z_l = wx.MenuItem(id=wx.ID_ANY, text="윗면을 축으로 반시계방향으로 회전(Shift+Z')")
edit.Append(z_l)
edit.AppendSeparator()

# 메뉴-도구

mix = wx.MenuItem(id=wx.ID_ANY, text='큐브 섞기(ctrl+M)')
tool.Append(mix)
tool.AppendSeparator()

clean = wx.MenuItem(id=wx.ID_ANY, text='원상태로 되돌리기(ctrl+F)')
tool.Append(clean)
tool.AppendSeparator()

# 메뉴-옵션
visible = wx.MenuItem(id=wx.ID_ANY, text='큐브그래픽 화면설정')
option.Append(visible)
option.AppendSeparator()

implementation = wx.MenuItem(id=wx.ID_ANY, text='큐브1.0ver 재구현')
option.Append(implementation)
option.AppendSeparator()
main_frame.SetMenuBar(menubar)


# 메뉴-파일(세부설정)

def onAbout(event):
    wx.MessageBox(
        "큐브를 회전시켜 맞추는 파이썬기반의 프로그램입니다.\n제작자 : 한승준\n1.0버전 : 큐브 환경 구현 및 조작함수 제작 (2019.2.23 ~ 2019.3.)\n2.0.0버전 : GUI 구현 (2019.4.1 ~ 2019.4.7)\n2.1버전 : 저장 및 불러오기 구현 (2021.7.14 ~ 2021.7.19)\n2.2버전 : 키보드 조작 및 단축키 구현 (2021.7.20 ~ 2021.7.21)",
        "알림", wx.OK)


main_frame.Bind(wx.EVT_MENU, onAbout, about)


def onSave(event):
    Cube2.save_Cube()
    wx.MessageBox("저장했습니다!", "알림", wx.OK)


main_frame.Bind(wx.EVT_MENU, onSave, save)


def onLoad(event):
    Cube2.Load_Cube()
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


main_frame.Bind(wx.EVT_MENU, onLoad, load)


def onQuit(event):
    dialog = wx.MessageDialog(main_frame, "종료하시겠습니까?", "종료", wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        main_frame.Close()
    else:
        pass
    dialog.Destroy()


main_frame.Bind(wx.EVT_MENU, onQuit, quit)

# 메뉴-편집(세부설정)

main_frame.Bind(wx.EVT_MENU, onU_R, u_r)
main_frame.Bind(wx.EVT_MENU, onU_L, u_l)
main_frame.Bind(wx.EVT_MENU, onH_R, h_r)
main_frame.Bind(wx.EVT_MENU, onH_L, h_l)
main_frame.Bind(wx.EVT_MENU, onD_R, d_r)
main_frame.Bind(wx.EVT_MENU, onD_L, d_l)
main_frame.Bind(wx.EVT_MENU, onR_R, r_r)
main_frame.Bind(wx.EVT_MENU, onR_L, r_l)
main_frame.Bind(wx.EVT_MENU, onM_R, m_r)
main_frame.Bind(wx.EVT_MENU, onM_L, m_l)
main_frame.Bind(wx.EVT_MENU, onL_R, l_r)
main_frame.Bind(wx.EVT_MENU, onL_L, l_l)
main_frame.Bind(wx.EVT_MENU, onF_R, f_r)
main_frame.Bind(wx.EVT_MENU, onF_L, f_l)
main_frame.Bind(wx.EVT_MENU, onS_R, s_r)
main_frame.Bind(wx.EVT_MENU, onS_L, s_l)
main_frame.Bind(wx.EVT_MENU, onB_R, b_r)
main_frame.Bind(wx.EVT_MENU, onB_L, b_l)
main_frame.Bind(wx.EVT_MENU, onX_R, x_r)
main_frame.Bind(wx.EVT_MENU, onX_L, x_l)
main_frame.Bind(wx.EVT_MENU, onY_R, y_r)
main_frame.Bind(wx.EVT_MENU, onY_L, y_l)
main_frame.Bind(wx.EVT_MENU, onZ_R, z_r)
main_frame.Bind(wx.EVT_MENU, onZ_L, z_l)


# 메뉴-도구(세부설정)

def onMix(event):
    Cube2.def_Number()
    for mix_num in range(MIX_NUM):
        Cube2.Mix_Cube()
        time.sleep(TIME)
        Cube_up.Bind(wx.EVT_PAINT, On_UP_Paint)
        Cube_front.Bind(wx.EVT_PAINT, On_FRONT_Paint)
        Cube_down.Bind(wx.EVT_PAINT, On_DOWN_Paint)
        Cube_right.Bind(wx.EVT_PAINT, On_RIGHT_Paint)
        Cube_left.Bind(wx.EVT_PAINT, On_LEFT_Paint)
        Cube_back.Bind(wx.EVT_PAINT, On_BACK_Paint)
        Cube_up.Refresh()
        Cube_front.Refresh()
        Cube_right.Refresh()
        Cube_left.Refresh()
        Cube_back.Refresh()
        Cube_down.Refresh()
    Cube2.def_Color()


main_frame.Bind(wx.EVT_MENU, onMix, mix)


def onClean(event):
    Cube2.Create_Cube()
    Cube2.def_Color()
    Cube_up.Refresh()
    Cube_front.Refresh()
    Cube_right.Refresh()
    Cube_left.Refresh()
    Cube_back.Refresh()
    Cube_down.Refresh()


main_frame.Bind(wx.EVT_MENU, onClean, clean)


# 메뉴-옵션(세부설정)

def onCube_Frame(event):
    Cube_Graphic_Option.Show(True)


main_frame.Bind(wx.EVT_MENU, onCube_Frame, visible)


def onCube_Implementation(event):
    implementation_frame.Show(True)


main_frame.Bind(wx.EVT_MENU, onCube_Implementation, implementation)

# 화면 체크박스 셋팅

Up_visible = wx.CheckBox(Cube_Graphic_Option, label="윗면 보임")
Right_visible = wx.CheckBox(Cube_Graphic_Option, label="오른쪽면 보임")
Front_visible = wx.CheckBox(Cube_Graphic_Option, label="앞면 보임")
Down_visible = wx.CheckBox(Cube_Graphic_Option, label="아랫면 보임")
Left_visible = wx.CheckBox(Cube_Graphic_Option, label="왼쪽면 보임")
Back_visible = wx.CheckBox(Cube_Graphic_Option, label="뒷면 보임")
frame_style_change = wx.CheckBox(Cube_Graphic_Option, label="큐브화면 자유이동 가능")
exit_btn = wx.Button(Cube_Graphic_Option, label="확인")

Right_visible.SetValue(wx.CHK_CHECKED)


def onR_visible(event):
    if Right_visible.GetValue() == wx.CHK_CHECKED:
        Cube_right.Show(True)
    else:
        Cube_right.Show(False)


Right_visible.Bind(wx.EVT_CHECKBOX, onR_visible)

Left_visible.SetValue(wx.CHK_CHECKED)


def onL_visible(event):
    if Left_visible.GetValue() == wx.CHK_CHECKED:
        Cube_left.Show(True)
    else:
        Cube_left.Show(False)


Left_visible.Bind(wx.EVT_CHECKBOX, onL_visible)

Up_visible.SetValue(wx.CHK_CHECKED)


def onU_visible(event):
    if Up_visible.GetValue() == wx.CHK_CHECKED:
        Cube_up.Show(True)
    else:
        Cube_up.Show(False)


Up_visible.Bind(wx.EVT_CHECKBOX, onU_visible)

Down_visible.SetValue(wx.CHK_CHECKED)


def onD_visible(event):
    if Down_visible.GetValue() == wx.CHK_CHECKED:
        Cube_down.Show(True)
    else:
        Cube_down.Show(False)


Down_visible.Bind(wx.EVT_CHECKBOX, onD_visible)

Front_visible.SetValue(wx.CHK_CHECKED)


def onF_visible(event):
    if Front_visible.GetValue() == wx.CHK_CHECKED:
        Cube_front.Show(True)
    else:
        Cube_front.Show(False)


Front_visible.Bind(wx.EVT_CHECKBOX, onF_visible)

Back_visible.SetValue(wx.CHK_CHECKED)


def onB_visible(event):
    if Back_visible.GetValue() == wx.CHK_CHECKED:
        Cube_back.Show(True)
    else:
        Cube_back.Show(False)


Back_visible.Bind(wx.EVT_CHECKBOX, onB_visible)

frame_style_change.SetValue(wx.CHK_CHECKED)


def onStyle_Change(event):
    if frame_style_change.GetValue() == wx.CHK_CHECKED:
        Cube_up.SetWindowStyle(wx.SYSTEM_MENU)
        Cube_right.SetWindowStyle(wx.SYSTEM_MENU)
        Cube_down.SetWindowStyle(wx.SYSTEM_MENU)
        Cube_left.SetWindowStyle(wx.SYSTEM_MENU)
        Cube_front.SetWindowStyle(wx.SYSTEM_MENU)
        Cube_back.SetWindowStyle(wx.SYSTEM_MENU)
    else:
        Cube_up.SetWindowStyle(wx.CAPTION)
        Cube_right.SetWindowStyle(wx.CAPTION)
        Cube_down.SetWindowStyle(wx.CAPTION)
        Cube_left.SetWindowStyle(wx.CAPTION)
        Cube_front.SetWindowStyle(wx.CAPTION)
        Cube_back.SetWindowStyle(wx.CAPTION)


frame_style_change.Bind(wx.EVT_CHECKBOX, onStyle_Change)


def onExit_btn(event):
    Cube_Graphic_Option.Show(False)


exit_btn.Bind(wx.EVT_BUTTON, onExit_btn)

empty = wx.StaticText(Cube_Graphic_Option, label="\n\n")

box = wx.BoxSizer(wx.VERTICAL)
Cube_Graphic_Option.SetSizer(box)
box.Add(Up_visible)
box.Add(Right_visible)
box.Add(Front_visible)
box.Add(Down_visible)
box.Add(Left_visible)
box.Add(Back_visible)
box.Add(frame_style_change)
box.Add(empty)
box.Add(exit_btn)

# 큐브 1.0 재구현 프레임 셋팅

text_explan = wx.StaticText(implementation_frame, label="큐브 회전패턴을 입력하세요.\n(시계방향은 소문자, 반시계방향은\n대문자 입력. (예: ruRU))")
turn_point = 0
turn_list = ["u", "U", "h", "H", "d", "D", "r", "R", "m", "M", "l", "L", "f", "F", "d", "S", "b", "B", "x", "X", "y",
             "Y", "z", "Z"]

# class Node():
#    def __init__(self):
#        self.data = ''
#        self.p_Next = []

turn_num = wx.TextCtrl(implementation_frame)
btn_imple = wx.Button(implementation_frame, label="입력")
result = wx.StaticText(implementation_frame, label='결과: ' + '%d' % turn_point)


#    text = Node()
def onClick_imple(event):
    Cube2.Create_Cube()
    Cube2.def_Color()
    spin_All()

    def TURN_NUM(event):
        turn_point = 0
        while True:
            text = turn_num.GetValue()
            #            text.p_Next.append(text)
            for t in text:
                Cube2.def_Number()
                turn_point += 1
                if t == 'u':
                    Cube2.Up_Right()
                    spin_U()
                    time.sleep(TIME)
                elif t == 'U':
                    Cube2.Up_Left()
                    spin_U()
                    time.sleep(TIME)
                elif t == 'd':
                    Cube2.Down_Right()
                    spin_D()
                    time.sleep(TIME)
                elif t == 'D':
                    Cube2.Down_Left()
                    spin_D()
                    time.sleep(TIME)
                elif t == 'r':
                    Cube2.Right_Right()
                    spin_R()
                    time.sleep(TIME)
                elif t == 'R':
                    Cube2.Right_Left()
                    spin_R()
                    time.sleep(TIME)
                elif t == 'l':
                    Cube2.Left_Right()
                    spin_L()
                    time.sleep(TIME)
                elif t == 'L':
                    Cube2.Left_Left()
                    spin_L()
                    time.sleep(TIME)
                elif t == 'f':
                    Cube2.Front_Right()
                    spin_F()
                    time.sleep(TIME)
                elif t == 'F':
                    Cube2.Front_Left()
                    spin_F()
                    time.sleep(TIME)
                elif t == 'b':
                    Cube2.Back_Right()
                    spin_B()
                    time.sleep(TIME)
                elif t == 'B':
                    Cube2.Back_Left()
                    spin_B()
                    time.sleep(TIME)
                elif t == 'h':
                    Cube2.Horizon_Right()
                    spin_H()
                    time.sleep(TIME)
                elif t == 'H':
                    Cube2.Horizon_Left()
                    spin_H()
                    time.sleep(TIME)
                elif t == 'm':
                    Cube2.Middle_Right()
                    spin_M()
                    time.sleep(TIME)
                elif t == 'M':
                    Cube2.Middle_Left()
                    spin_M()
                    time.sleep(TIME)
                elif t == 's':
                    Cube2.Side_Right()
                    spin_S()
                    time.sleep(TIME)
                elif t == 'S':
                    Cube2.Side_Left()
                    spin_S()
                    time.sleep(TIME)
                elif t == 'x':
                    Cube2.X_Right()
                    spin_All()
                    time.sleep(TIME)
                elif t == 'X':
                    Cube2.X_Left()
                    spin_All()
                    time.sleep(TIME)
                elif t == 'y':
                    Cube2.Y_Right()
                    spin_All()
                    time.sleep(TIME)
                elif t == 'Y':
                    Cube2.Y_Left()
                    spin_All()
                    time.sleep(TIME)
                elif t == 'z':
                    Cube2.Z_Right()
                    spin_All()
                    time.sleep(TIME)
                elif t == 'Z':
                    Cube2.Z_Left()
                    spin_All()
                    time.sleep(TIME)
                elif t != turn_list[0:23]:
                    wx.MessageBox('%c' % t + "는 잘못된 입력값 입니다.", "경고", wx.OK)
                    break
                elif (Cube2.Clear_Cube() == 0):
                    result.SetLabel('결과: ' + '%d' % turn_point)
                    Cube2.def_Color()
                    break
                else:
                    continue

    turn_num.Bind(wx.EVT_TEXT, TURN_NUM)


btn_imple.Bind(wx.EVT_BUTTON, onClick_imple)

exit_btn_imple = wx.Button(implementation_frame, label="종료")


def onExit_btn_imple(event):
    implementation_frame.Show(False)


exit_btn_imple.Bind(wx.EVT_BUTTON, onExit_btn_imple)

empty_imple = wx.StaticText(implementation_frame, label="\n\n")

box = wx.BoxSizer(wx.VERTICAL)
implementation_frame.SetSizer(box)
box.Add(text_explan)
box.Add(turn_num)
box.Add(btn_imple)
box.Add(result)
box.Add(empty_imple)
box.Add(exit_btn_imple, flag=wx.ALIGN_CENTER_HORIZONTAL)

# 프레임 초기상태
start_frame.Show(True)
main_frame.Show(False)
Cube_up.Show(False)
Cube_front.Show(False)
Cube_down.Show(False)
Cube_right.Show(False)
Cube_left.Show(False)
Cube_back.Show(False)
Cube_Graphic_Option.Show(False)
implementation_frame.Show(False)

app.MainLoop()