#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 큐브 모듈화

import wx
import random
import sqlite3 as sq


# 클래스 이름, 전역 함수 이름 : PascalCase
# 클래스 내 함수 이름(메소드), 인스턴스변수, 클래스 변수 : camelCase
# 상수 : CAPITAL_SNAKE

class Cube:
    def __init__(self, mix_num=60, time=0.01):
        self.mix_num = mix_num
        self.time = time

    def createCube(self):
        """큐브의 환경을 조성한다."""
        global myCube, sampleCube  # global은 되도록 쓰지 않는 것이 좋다.
        global Register, register
        sampleCube = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                      [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                      [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        myCube = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                  [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                  [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        Register = [[[None, None, None], [None, None, None], [None, None, None], [None, None], [None], [None, None],
                     [None, None, None], [None, None], [None, None, None]],
                    [[None, None], [None], [None, None], [None], [None], [None], [None, None], [None], [None, None]],
                    [[None, None, None], [None, None], [None, None, None], [None, None], [None], [None, None],
                     [None, None, None], [None, None], [None, None, None]]]
        register = [None, None, None]

    def elementRight(self, floor, piece):
        """큐브의 모서리조각을 시계방향으로 돌려준다.  입력방식 : Element_Right(floor, piece)"""
        register[0:3] = myCube[floor][piece][0:3]
        myCube[floor][piece][0] = register[1]
        myCube[floor][piece][1] = register[2]
        myCube[floor][piece][2] = register[0]

    def elementLeft(self, floor, piece):
        """큐브의 모서리조각을 반시계방향으로 돌려준다.  입력방식 : Element_Left(floor, piece)"""
        register[0:3] = myCube[floor][piece][0:3]
        myCube[floor][piece][0] = register[2]
        myCube[floor][piece][1] = register[0]
        myCube[floor][piece][2] = register[1]

    def elementMirror(self, floor, piece):
        """큐브의 엣지조각을 반전시킨다.  입력방식 : Element_Mirror(floor, piece)"""
        register[0:2] = myCube[floor][piece][0:2]
        myCube[floor][piece][0] = register[1]
        myCube[floor][piece][1] = register[0]

    def upRight(self):
        """윗면을 시계방향으로 회전한다."""
        Register[0][0:9] = myCube[0][0:9]
        myCube[0][0] = Register[0][2]
        myCube[0][1] = Register[0][5]
        myCube[0][2] = Register[0][8]
        myCube[0][3] = Register[0][1]
        myCube[0][5] = Register[0][7]
        myCube[0][6] = Register[0][0]
        myCube[0][7] = Register[0][3]
        myCube[0][8] = Register[0][6]

    def upLeft(self):
        """윗면을 시계 반대방향으로 회전한다."""
        Register[0][0:9] = myCube[0][0:9]
        myCube[0][0] = Register[0][6]
        myCube[0][1] = Register[0][3]
        myCube[0][2] = Register[0][0]
        myCube[0][3] = Register[0][7]
        myCube[0][5] = Register[0][1]
        myCube[0][6] = Register[0][8]
        myCube[0][7] = Register[0][5]
        myCube[0][8] = Register[0][2]

    def horizonRight(self):
        """윗면과 아랫면 사이층을 시계방향으로 회전한다."""
        Register[1][0:9] = myCube[1][0:9]
        myCube[1][0] = Register[1][2]
        myCube[1][1] = Register[1][5]
        myCube[1][2] = Register[1][8]
        myCube[1][3] = Register[1][1]
        myCube[1][5] = Register[1][7]
        myCube[1][6] = Register[1][0]
        myCube[1][7] = Register[1][3]
        myCube[1][8] = Register[1][6]
        self.elementMirror(1, 0)
        self.elementMirror(1, 2)
        self.elementMirror(1, 6)
        self.elementMirror(1, 8)

    def horizonLeft(self):
        """윗면과 아랫면 사이층을 시계 반대방향으로 회전한다."""
        Register[1][0:9] = myCube[1][0:9]
        myCube[1][0] = Register[1][6]
        myCube[1][1] = Register[1][3]
        myCube[1][2] = Register[1][0]
        myCube[1][3] = Register[1][7]
        myCube[1][5] = Register[1][1]
        myCube[1][6] = Register[1][8]
        myCube[1][7] = Register[1][5]
        myCube[1][8] = Register[1][2]
        self.elementMirror(1, 0)
        self.elementMirror(1, 2)
        self.elementMirror(1, 6)
        self.elementMirror(1, 8)

    def downRight(self):
        """아랫면을 시계방향으로 회전한다."""
        Register[2][0:9] = myCube[2][0:9]
        myCube[2][0] = Register[2][6]
        myCube[2][1] = Register[2][3]
        myCube[2][2] = Register[2][0]
        myCube[2][3] = Register[2][7]
        myCube[2][5] = Register[2][1]
        myCube[2][6] = Register[2][8]
        myCube[2][7] = Register[2][5]
        myCube[2][8] = Register[2][2]

    def downLeft(self):
        """아랫면을 시계 반대방향으로 회전한다."""
        Register[2][0:9] = myCube[2][0:9]
        myCube[2][0] = Register[2][2]
        myCube[2][1] = Register[2][5]
        myCube[2][2] = Register[2][8]
        myCube[2][3] = Register[2][1]
        myCube[2][5] = Register[2][7]
        myCube[2][6] = Register[2][0]
        myCube[2][7] = Register[2][3]
        myCube[2][8] = Register[2][6]

    def rightRight(self):
        """오른쪽 면을 시계방향으로 회전한다."""
        Register[0][0:3] = myCube[0][0:3]
        Register[1][0:3] = myCube[1][0:3]
        Register[2][0:3] = myCube[2][0:3]
        myCube[0][0] = Register[2][0]
        myCube[0][1] = Register[1][0]
        myCube[0][2] = Register[0][0]
        myCube[1][0] = Register[2][1]
        myCube[1][2] = Register[0][1]
        myCube[2][0] = Register[2][2]
        myCube[2][1] = Register[1][2]
        myCube[2][2] = Register[0][2]
        self.elementLeft(0, 0)
        self.elementRight(0, 2)
        self.elementRight(2, 0)
        self.elementLeft(2, 2)

    def rightLeft(self):
        """오른쪽 면을 시계 반대방향으로 회전한다."""
        Register[0][0:3] = myCube[0][0:3]
        Register[1][0:3] = myCube[1][0:3]
        Register[2][0:3] = myCube[2][0:3]
        myCube[0][0] = Register[0][2]
        myCube[0][1] = Register[1][2]
        myCube[0][2] = Register[2][2]
        myCube[1][0] = Register[0][1]
        myCube[1][2] = Register[2][1]
        myCube[2][0] = Register[0][0]
        myCube[2][1] = Register[1][0]
        myCube[2][2] = Register[2][0]
        self.elementLeft(0, 0)
        self.elementRight(0, 2)
        self.elementRight(2, 0)
        self.elementLeft(2, 2)

    def middleRight(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계방향으로 회전한다."""
        Register[0][3:6] = myCube[0][3:6]
        Register[1][3:6] = myCube[1][3:6]
        Register[2][3:6] = myCube[2][3:6]
        myCube[0][3] = Register[2][3]
        myCube[0][4] = Register[1][3]
        myCube[0][5] = Register[0][3]
        myCube[1][3] = Register[2][4]
        myCube[1][5] = Register[0][4]
        myCube[2][3] = Register[2][5]
        myCube[2][4] = Register[1][5]
        myCube[2][5] = Register[0][5]
        self.elementMirror(0, 3)
        self.elementMirror(0, 5)
        self.elementMirror(2, 3)
        self.elementMirror(2, 5)

    def middleLeft(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계 반대방향으로 회전한다."""
        Register[0][3:6] = myCube[0][3:6]
        Register[1][3:6] = myCube[1][3:6]
        Register[2][3:6] = myCube[2][3:6]
        myCube[0][3] = Register[0][5]
        myCube[0][4] = Register[1][5]
        myCube[0][5] = Register[2][5]
        myCube[1][3] = Register[0][4]
        myCube[1][5] = Register[2][4]
        myCube[2][3] = Register[0][3]
        myCube[2][4] = Register[1][3]
        myCube[2][5] = Register[2][3]
        self.elementMirror(0, 3)
        self.elementMirror(0, 5)
        self.elementMirror(2, 3)
        self.elementMirror(2, 5)

    def leftRight(self):
        """왼쪽 면을 시계방향으로 회전한다."""
        Register[0][6:9] = myCube[0][6:9]
        Register[1][6:9] = myCube[1][6:9]
        Register[2][6:9] = myCube[2][6:9]
        myCube[0][6] = Register[0][8]
        myCube[0][7] = Register[1][8]
        myCube[0][8] = Register[2][8]
        myCube[1][6] = Register[0][7]
        myCube[1][8] = Register[2][7]
        myCube[2][6] = Register[0][6]
        myCube[2][7] = Register[1][6]
        myCube[2][8] = Register[2][6]
        self.elementRight(0, 6)
        self.elementLeft(0, 8)
        self.elementLeft(2, 6)
        self.elementRight(2, 8)

    def leftLeft(self):
        """왼쪽 면을 시계 반대방향으로 회전한다."""
        Register[0][6:9] = myCube[0][6:9]
        Register[1][6:9] = myCube[1][6:9]
        Register[2][6:9] = myCube[2][6:9]
        myCube[0][6] = Register[2][6]
        myCube[0][7] = Register[1][6]
        myCube[0][8] = Register[0][6]
        myCube[1][6] = Register[2][7]
        myCube[1][8] = Register[0][7]
        myCube[2][6] = Register[2][8]
        myCube[2][7] = Register[1][8]
        myCube[2][8] = Register[0][8]
        self.elementRight(0, 6)
        self.elementLeft(0, 8)
        self.elementLeft(2, 6)
        self.elementRight(2, 8)

    def frontRight(self):
        """앞면을 시계방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][6], myCube[0][3], myCube[0][0]]
        Register[1][0:2] = [myCube[1][6], myCube[1][0]]
        Register[2][0:3] = [myCube[2][6], myCube[2][3], myCube[2][0]]
        myCube[0][6] = Register[2][0]
        myCube[0][3] = Register[1][0]
        myCube[0][0] = Register[0][0]
        myCube[1][6] = Register[2][1]
        myCube[1][0] = Register[0][1]
        myCube[2][6] = Register[2][2]
        myCube[2][3] = Register[1][1]
        myCube[2][0] = Register[0][2]
        self.elementLeft(0, 6)
        self.elementMirror(0, 3)
        self.elementRight(0, 0)
        self.elementMirror(1, 6)
        self.elementMirror(1, 0)
        self.elementRight(2, 6)
        self.elementMirror(2, 3)
        self.elementLeft(2, 0)

    def frontLeft(self):
        """앞면을 시계 반대방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][6], myCube[0][3], myCube[0][0]]
        Register[1][0:2] = [myCube[1][6], myCube[1][0]]
        Register[2][0:3] = [myCube[2][6], myCube[2][3], myCube[2][0]]
        myCube[0][6] = Register[0][2]
        myCube[0][3] = Register[1][1]
        myCube[0][0] = Register[2][2]
        myCube[1][6] = Register[0][1]
        myCube[1][0] = Register[2][1]
        myCube[2][6] = Register[0][0]
        myCube[2][3] = Register[1][0]
        myCube[2][0] = Register[2][0]
        self.elementLeft(0, 6)
        self.elementMirror(0, 3)
        self.elementRight(0, 0)
        self.elementMirror(1, 6)
        self.elementMirror(1, 0)
        self.elementRight(2, 6)
        self.elementMirror(2, 3)
        self.elementLeft(2, 0)

    def sideRight(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][7], myCube[0][4], myCube[0][1]]
        Register[1][0:2] = [myCube[1][7], myCube[1][1]]
        Register[2][0:3] = [myCube[2][7], myCube[2][4], myCube[2][1]]
        myCube[0][7] = Register[2][0]
        myCube[0][4] = Register[1][0]
        myCube[0][1] = Register[0][0]
        myCube[1][7] = Register[2][1]
        myCube[1][1] = Register[0][1]
        myCube[2][7] = Register[2][2]
        myCube[2][4] = Register[1][1]
        myCube[2][1] = Register[0][2]
        self.elementMirror(0, 7)
        self.elementMirror(0, 1)
        self.elementMirror(2, 7)
        self.elementMirror(2, 1)

    def sideLeft(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계 반대방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][7], myCube[0][4], myCube[0][1]]
        Register[1][0:2] = [myCube[1][7], myCube[1][1]]
        Register[2][0:3] = [myCube[2][7], myCube[2][4], myCube[2][1]]
        myCube[0][7] = Register[0][2]
        myCube[0][4] = Register[1][1]
        myCube[0][1] = Register[2][2]
        myCube[1][7] = Register[0][1]
        myCube[1][1] = Register[2][1]
        myCube[2][7] = Register[0][0]
        myCube[2][4] = Register[1][0]
        myCube[2][1] = Register[2][0]
        self.elementMirror(0, 7)
        self.elementMirror(0, 1)
        self.elementMirror(2, 7)
        self.elementMirror(2, 1)

    def backRight(self):
        """뒷면을 시계방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][8], myCube[0][5], myCube[0][2]]
        Register[1][0:2] = [myCube[1][8], myCube[1][2]]
        Register[2][0:3] = [myCube[2][8], myCube[2][5], myCube[2][2]]
        myCube[0][2] = Register[2][2]
        myCube[0][5] = Register[1][1]
        myCube[0][8] = Register[0][2]
        myCube[1][2] = Register[2][1]
        myCube[1][8] = Register[0][1]
        myCube[2][2] = Register[2][0]
        myCube[2][5] = Register[1][0]
        myCube[2][8] = Register[0][0]
        self.elementLeft(0, 2)
        self.elementMirror(0, 5)
        self.elementRight(0, 8)
        self.elementMirror(1, 2)
        self.elementMirror(1, 8)
        self.elementRight(2, 2)
        self.elementMirror(2, 5)
        self.elementLeft(2, 8)

    def backLeft(self):
        """뒷면을 시계방향으로 회전한다."""
        Register[0][0:3] = [myCube[0][8], myCube[0][5], myCube[0][2]]
        Register[1][0:2] = [myCube[1][8], myCube[1][2]]
        Register[2][0:3] = [myCube[2][8], myCube[2][5], myCube[2][2]]
        myCube[0][2] = Register[0][0]
        myCube[0][5] = Register[1][0]
        myCube[0][8] = Register[2][0]
        myCube[1][2] = Register[0][1]
        myCube[1][8] = Register[2][1]
        myCube[2][2] = Register[0][2]
        myCube[2][5] = Register[1][1]
        myCube[2][8] = Register[2][2]
        self.elementLeft(0, 2)
        self.elementMirror(0, 5)
        self.elementRight(0, 8)
        self.elementMirror(1, 2)
        self.elementMirror(1, 8)
        self.elementRight(2, 2)
        self.elementMirror(2, 5)
        self.elementLeft(2, 8)

    def xRight(self):
        """큐브 전체를 앞면 축에 대해 시계방향으로 회전한다."""
        self.frontRight()
        self.sideRight()
        self.backLeft()

    def xLeft(self):
        """큐브 전체를 앞면 축에 대해 시계 반대방향으로 회전한다."""
        self.frontLeft()
        self.sideLeft()
        self.backRight()

    def yRight(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계방향으로 회전한다."""
        self.rightRight()
        self.middleRight()
        self.leftLeft()

    def yLeft(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계 반대방향으로 회전한다."""
        self.rightLeft()
        self.middleLeft()
        self.leftRight()

    def zRight(self):
        """큐브 전체를 윗면의 축에 대해 시계방향으로 회전한다."""
        self.upRight()
        self.horizonRight()
        self.downLeft()

    def zLeft(self):
        """큐브 전체를 윗면의 축에 대해 시계 반대방향으로 회전한다."""
        self.upLeft()
        self.horizonLeft()
        self.downRight()

    def clearCube(self):
        """큐브 전체를 24가지 경우로 돌려보며 모두 맞춰졌는지 판별하는 함수"""

        def ifClear(self):
            """큐브의 모든 조각들의 요소가 맞춰져있는지 판별하는 함수."""
            if (sampleCube[0][0] == myCube[0][0] and sampleCube[0][1] == myCube[0][1] and sampleCube[0][2] == myCube[0][2] and
                sampleCube[0][3] == myCube[0][3] and sampleCube[0][4] == myCube[0][4] and sampleCube[0][5] == myCube[0][5] and
                sampleCube[0][6] == myCube[0][6] and sampleCube[0][7] == myCube[0][7] and sampleCube[0][8] == myCube[0][8] and
                sampleCube[1][0] == myCube[1][0] and sampleCube[1][1] == myCube[1][1] and sampleCube[1][2] == myCube[1][2] and
                sampleCube[1][3] == myCube[1][3] and sampleCube[1][5] == myCube[1][5] and sampleCube[1][6] == myCube[1][6] and
                sampleCube[1][7] == myCube[1][7] and sampleCube[1][8] == myCube[1][8] and
                sampleCube[2][0] == myCube[2][0] and sampleCube[2][1] == myCube[2][1] and sampleCube[2][2] == myCube[2][2] and
                sampleCube[2][3] == myCube[2][3] and sampleCube[2][4] == myCube[2][4] and sampleCube[2][5] == myCube[2][5] and
                sampleCube[2][6] == myCube[2][6] and sampleCube[2][7] == myCube[2][7] and sampleCube[2][8] == myCube[2][8]):

                return 1
            else:
                return 0

        find1 = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        find2 = [[None, None, None, None], [None, None, None, None]]
        find3 = [None, None]

        for xy in range(4):
            for x in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find1[xy][x] = 1
                else:
                    find1[xy][x] = 0
            self.yRight()

        for zxzx in range(2):
            self.zRight()
            for x in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find2[zxzx][x] = 1
                else:
                    find2[zxzx][x] = 0
            self.zRight()
            self.xRight()
            if (self.ifClear() == 1):
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
            self.upRight()
        elif (self.Cube_Mix_Ceed == 2):
            self.upLeft()
        elif (self.Cube_Mix_Ceed == 3):
            self.horizonRight()
        elif (self.Cube_Mix_Ceed == 4):
            self.horizonLeft()
        elif (self.Cube_Mix_Ceed == 5):
            self.downRight()
        elif (self.Cube_Mix_Ceed == 6):
            self.downLeft()
        elif (self.Cube_Mix_Ceed == 7):
            self.rightRight()
        elif (self.Cube_Mix_Ceed == 8):
            self.rightLeft()
        elif (self.Cube_Mix_Ceed == 9):
            self.middleRight()
        elif (self.Cube_Mix_Ceed == 10):
            self.middleLeft()
        elif (self.Cube_Mix_Ceed == 11):
            self.leftRight()
        elif (self.Cube_Mix_Ceed == 12):
            self.leftLeft()
        elif (self.Cube_Mix_Ceed == 13):
            self.frontRight()
        elif (self.Cube_Mix_Ceed == 14):
            self.frontLeft()
        elif (self.Cube_Mix_Ceed == 15):
            self.sideRight()
        elif (self.Cube_Mix_Ceed == 16):
            self.sideLeft()
        elif (self.Cube_Mix_Ceed == 17):
            self.backRight()
        elif (self.Cube_Mix_Ceed == 18):
            self.backLeft()

    def save_Cube(self):
        """큐브 데이터를 저장하는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        self.def_Number()

        cursor.execute("""DROP TABLE IF EXISTS pieceAddr""")
        cursor.execute("""CREATE TABLE pieceAddr(Floor int, Position int, Element int)""")

        ElementList = (
            (myCube[0][0][0]), (myCube[0][0][1]), (myCube[0][0][2]),
            (myCube[0][1][0]), (myCube[0][1][1]),
            (myCube[0][2][0]), (myCube[0][2][1]), (myCube[0][2][2]),
            (myCube[0][3][0]), (myCube[0][3][1]),
            (myCube[0][4][0]),
            (myCube[0][5][0]), (myCube[0][5][1]),
            (myCube[0][6][0]), (myCube[0][6][1]), (myCube[0][6][2]),
            (myCube[0][7][0]), (myCube[0][7][1]),
            (myCube[0][8][0]), (myCube[0][8][1]), (myCube[0][8][2]),
            (myCube[1][0][0]), (myCube[1][0][1]),
            (myCube[1][1][0]),
            (myCube[1][2][0]), (myCube[1][2][1]),
            (myCube[1][3][0]),
            (myCube[1][5][0]),
            (myCube[1][6][0]), (myCube[1][6][1]),
            (myCube[1][7][0]),
            (myCube[1][8][0]), (myCube[1][8][1]),
            (myCube[2][0][0]), (myCube[2][0][1]), (myCube[2][0][2]),
            (myCube[2][1][0]), (myCube[2][1][1]),
            (myCube[2][2][0]), (myCube[2][2][1]), (myCube[2][2][2]),
            (myCube[2][3][0]), (myCube[2][3][1]),
            (myCube[2][4][0]),
            (myCube[2][5][0]), (myCube[2][5][1]),
            (myCube[2][6][0]), (myCube[2][6][1]), (myCube[2][6][2]),
            (myCube[2][7][0]), (myCube[2][7][1]),
            (myCube[2][8][0]), (myCube[2][8][1]), (myCube[2][8][2]),
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

        myCube[0][0][0] = ElementList[0][0]
        myCube[0][0][1] = ElementList[1][0]
        myCube[0][0][2] = ElementList[2][0]
        myCube[0][1][0] = ElementList[3][0]
        myCube[0][1][1] = ElementList[4][0]
        myCube[0][2][0] = ElementList[5][0]
        myCube[0][2][1] = ElementList[6][0]
        myCube[0][2][2] = ElementList[7][0]
        myCube[0][3][0] = ElementList[8][0]
        myCube[0][3][1] = ElementList[9][0]
        myCube[0][4][0] = ElementList[10][0]
        myCube[0][5][0] = ElementList[11][0]
        myCube[0][5][1] = ElementList[12][0]
        myCube[0][6][0] = ElementList[13][0]
        myCube[0][6][1] = ElementList[14][0]
        myCube[0][6][2] = ElementList[15][0]
        myCube[0][7][0] = ElementList[16][0]
        myCube[0][7][1] = ElementList[17][0]
        myCube[0][8][0] = ElementList[18][0]
        myCube[0][8][1] = ElementList[19][0]
        myCube[0][8][2] = ElementList[20][0]
        myCube[1][0][0] = ElementList[21][0]
        myCube[1][0][1] = ElementList[22][0]
        myCube[1][1][0] = ElementList[23][0]
        myCube[1][2][0] = ElementList[24][0]
        myCube[1][2][1] = ElementList[25][0]
        myCube[1][3][0] = ElementList[26][0]
        myCube[1][5][0] = ElementList[27][0]
        myCube[1][6][0] = ElementList[28][0]
        myCube[1][6][1] = ElementList[29][0]
        myCube[1][7][0] = ElementList[30][0]
        myCube[1][8][0] = ElementList[31][0]
        myCube[1][8][1] = ElementList[32][0]
        myCube[2][0][0] = ElementList[33][0]
        myCube[2][0][1] = ElementList[34][0]
        myCube[2][0][2] = ElementList[35][0]
        myCube[2][1][0] = ElementList[36][0]
        myCube[2][1][1] = ElementList[37][0]
        myCube[2][2][0] = ElementList[38][0]
        myCube[2][2][1] = ElementList[39][0]
        myCube[2][2][2] = ElementList[40][0]
        myCube[2][3][0] = ElementList[41][0]
        myCube[2][3][1] = ElementList[42][0]
        myCube[2][4][0] = ElementList[43][0]
        myCube[2][5][0] = ElementList[44][0]
        myCube[2][5][1] = ElementList[45][0]
        myCube[2][6][0] = ElementList[46][0]
        myCube[2][6][1] = ElementList[47][0]
        myCube[2][6][2] = ElementList[48][0]
        myCube[2][7][0] = ElementList[49][0]
        myCube[2][7][1] = ElementList[50][0]
        myCube[2][8][0] = ElementList[51][0]
        myCube[2][8][1] = ElementList[52][0]
        myCube[2][8][2] = ElementList[53][0]

        self.def_Color()

        con.commit()

        cursor.close()
        con.close()

    def dist_Color(self, floor, piece, color):
        """각 큐브 조각의 색을 디코딩"""
        if (myCube[floor][piece][color] == 1):
            myCube[floor][piece][color] = wx.YELLOW
        elif (myCube[floor][piece][color] == 2):
            myCube[floor][piece][color] = wx.BLUE
        elif (myCube[floor][piece][color] == 3):
            myCube[floor][piece][color] = wx.RED
        elif (myCube[floor][piece][color] == 4):
            myCube[floor][piece][color] = wx.Colour(0, 150, 0, 0)
        elif (myCube[floor][piece][color] == 5):
            myCube[floor][piece][color] = wx.Colour(250, 125, 0, 0)
        elif (myCube[floor][piece][color] == 6):
            myCube[floor][piece][color] = wx.WHITE
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
        if (myCube[floor][piece][color] == wx.YELLOW):
            myCube[floor][piece][color] = 1
        elif (myCube[floor][piece][color] == wx.BLUE):
            myCube[floor][piece][color] = 2
        elif (myCube[floor][piece][color] == wx.RED):
            myCube[floor][piece][color] = 3
        elif (myCube[floor][piece][color] == wx.Colour(0, 150, 0, 0)):
            myCube[floor][piece][color] = 4
        elif (myCube[floor][piece][color] == wx.Colour(250, 125, 0, 0)):
            myCube[floor][piece][color] = 5
        elif (myCube[floor][piece][color] == wx.WHITE):
            myCube[floor][piece][color] = 6
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


if __name__ == "__main__":
    print()
