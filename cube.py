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

class CubeBody:

    def __init__(self, MIX_NUM=60, TIME=0.01):
        self.mix_num = MIX_NUM
        self.time = TIME

    def createCube(self):
        """큐브의 환경을 조성한다."""
        global myCube  # global은 되도록 쓰지 않는 것이 좋다.
        global sampleCube
        global cubeRegister
        global pieceRegister

        sampleCube = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                      [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                      [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        myCube = [[[1, 2, 3], [1, 3], [1, 3, 4], [1, 2], [1], [1, 4], [1, 5, 2], [1, 5], [1, 4, 5]],
                  [[2, 3], [3], [4, 3], [2], [], [4], [2, 5], [5], [4, 5]],
                  [[6, 3, 2], [6, 3], [6, 4, 3], [6, 2], [6], [6, 4], [6, 2, 5], [6, 5], [6, 5, 4]]]
        cubeRegister = [[[None, None, None], [None, None], [None, None, None],
                         [None, None], [None], [None, None],
                         [None, None, None], [None, None], [None, None, None]],
                        [[None, None], [None, None], [None, None],
                         [None], [None], [None],
                         [None, None], [None], [None, None]]]
        pieceRegister = [None, None, None]

    def elementClockwise(self, floor, piece):
        """큐브의 모서리조각을 시계방향으로 돌려준다.  입력방식 : Element_Right(floor, piece)"""
        pieceRegister[0:3] = myCube[floor][piece][0:3]
        myCube[floor][piece][0] = pieceRegister[1]
        myCube[floor][piece][1] = pieceRegister[2]
        myCube[floor][piece][2] = pieceRegister[0]

    def elementCounterclockwise(self, floor, piece):
        """큐브의 모서리조각을 반시계방향으로 돌려준다.  입력방식 : Element_Left(floor, piece)"""
        pieceRegister[0:3] = myCube[floor][piece][0:3]
        myCube[floor][piece][0] = pieceRegister[2]
        myCube[floor][piece][1] = pieceRegister[0]
        myCube[floor][piece][2] = pieceRegister[1]

    def elementReverse(self, floor, piece):
        """큐브의 엣지조각을 반전시킨다.  입력방식 : Element_Mirror(floor, piece)"""
        pieceRegister[0:2] = myCube[floor][piece][0:2]
        myCube[floor][piece][0] = pieceRegister[1]
        myCube[floor][piece][1] = pieceRegister[0]

    def upRight(self):
        """윗면을 시계방향으로 회전한다."""
        cubeRegister[0][0:9] = myCube[0][0:9]
        myCube[0][0] = cubeRegister[0][2]
        myCube[0][1] = cubeRegister[0][5]
        myCube[0][2] = cubeRegister[0][8]
        myCube[0][3] = cubeRegister[0][1]
        myCube[0][5] = cubeRegister[0][7]
        myCube[0][6] = cubeRegister[0][0]
        myCube[0][7] = cubeRegister[0][3]
        myCube[0][8] = cubeRegister[0][6]

    def upLeft(self):
        """윗면을 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:9] = myCube[0][0:9]
        myCube[0][0] = cubeRegister[0][6]
        myCube[0][1] = cubeRegister[0][3]
        myCube[0][2] = cubeRegister[0][0]
        myCube[0][3] = cubeRegister[0][7]
        myCube[0][5] = cubeRegister[0][1]
        myCube[0][6] = cubeRegister[0][8]
        myCube[0][7] = cubeRegister[0][5]
        myCube[0][8] = cubeRegister[0][2]

    def horizonRight(self):
        """윗면과 아랫면 사이층을 시계방향으로 회전한다."""
        cubeRegister[1][0:9] = myCube[1][0:9]
        myCube[1][0] = cubeRegister[1][2]
        myCube[1][1] = cubeRegister[1][5]
        myCube[1][2] = cubeRegister[1][8]
        myCube[1][3] = cubeRegister[1][1]
        myCube[1][5] = cubeRegister[1][7]
        myCube[1][6] = cubeRegister[1][0]
        myCube[1][7] = cubeRegister[1][3]
        myCube[1][8] = cubeRegister[1][6]
        self.elementReverse(1, 0)
        self.elementReverse(1, 2)
        self.elementReverse(1, 6)
        self.elementReverse(1, 8)

    def horizonLeft(self):
        """윗면과 아랫면 사이층을 시계 반대방향으로 회전한다."""
        cubeRegister[1][0:9] = myCube[1][0:9]
        myCube[1][0] = cubeRegister[1][6]
        myCube[1][1] = cubeRegister[1][3]
        myCube[1][2] = cubeRegister[1][0]
        myCube[1][3] = cubeRegister[1][7]
        myCube[1][5] = cubeRegister[1][1]
        myCube[1][6] = cubeRegister[1][8]
        myCube[1][7] = cubeRegister[1][5]
        myCube[1][8] = cubeRegister[1][2]
        self.elementReverse(1, 0)
        self.elementReverse(1, 2)
        self.elementReverse(1, 6)
        self.elementReverse(1, 8)

    def downRight(self):
        """아랫면을 시계방향으로 회전한다."""
        cubeRegister[0][0:9] = myCube[2][0:9]
        myCube[2][0] = cubeRegister[0][6]
        myCube[2][1] = cubeRegister[0][3]
        myCube[2][2] = cubeRegister[0][0]
        myCube[2][3] = cubeRegister[0][7]
        myCube[2][5] = cubeRegister[0][1]
        myCube[2][6] = cubeRegister[0][8]
        myCube[2][7] = cubeRegister[0][5]
        myCube[2][8] = cubeRegister[0][2]

    def downLeft(self):
        """아랫면을 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:9] = myCube[2][0:9]
        myCube[2][0] = cubeRegister[0][2]
        myCube[2][1] = cubeRegister[0][5]
        myCube[2][2] = cubeRegister[0][8]
        myCube[2][3] = cubeRegister[0][1]
        myCube[2][5] = cubeRegister[0][7]
        myCube[2][6] = cubeRegister[0][0]
        myCube[2][7] = cubeRegister[0][3]
        myCube[2][8] = cubeRegister[0][6]

    def rightRight(self):
        """오른쪽 면을 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = myCube[0][0:3]
        cubeRegister[0][3:6] = myCube[1][0:3]
        cubeRegister[0][6:9] = myCube[2][0:3]
        myCube[0][0] = cubeRegister[0][6]
        myCube[0][1] = cubeRegister[0][3]
        myCube[0][2] = cubeRegister[0][0]
        myCube[1][0] = cubeRegister[0][7]
        myCube[1][2] = cubeRegister[0][1]
        myCube[2][0] = cubeRegister[0][8]
        myCube[2][1] = cubeRegister[0][5]
        myCube[2][2] = cubeRegister[0][2]
        self.elementCounterclockwise(0, 0)
        self.elementClockwise(0, 2)
        self.elementClockwise(2, 0)
        self.elementCounterclockwise(2, 2)

    def rightLeft(self):
        """오른쪽 면을 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:3] = myCube[0][0:3]
        cubeRegister[0][3:6] = myCube[1][0:3]
        cubeRegister[0][6:9] = myCube[2][0:3]
        myCube[0][0] = cubeRegister[0][2]
        myCube[0][1] = cubeRegister[0][5]
        myCube[0][2] = cubeRegister[0][8]
        myCube[1][0] = cubeRegister[0][1]
        myCube[1][2] = cubeRegister[0][7]
        myCube[2][0] = cubeRegister[0][0]
        myCube[2][1] = cubeRegister[0][3]
        myCube[2][2] = cubeRegister[0][6]
        self.elementCounterclockwise(0, 0)
        self.elementClockwise(0, 2)
        self.elementClockwise(2, 0)
        self.elementCounterclockwise(2, 2)

    def middleRight(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계방향으로 회전한다."""
        cubeRegister[1][0:3] = myCube[0][3:6]
        cubeRegister[1][3:6] = myCube[1][3:6]
        cubeRegister[1][6:9] = myCube[2][3:6]
        myCube[0][3] = cubeRegister[1][6]
        myCube[0][4] = cubeRegister[1][3]
        myCube[0][5] = cubeRegister[1][0]
        myCube[1][3] = cubeRegister[1][7]
        myCube[1][5] = cubeRegister[1][1]
        myCube[2][3] = cubeRegister[1][8]
        myCube[2][4] = cubeRegister[1][5]
        myCube[2][5] = cubeRegister[1][2]
        self.elementReverse(0, 3)
        self.elementReverse(0, 5)
        self.elementReverse(2, 3)
        self.elementReverse(2, 5)

    def middleLeft(self):
        """오른쪽 면과 왼쪽 면의 사이층을 오른 축에 대해 시계 반대방향으로 회전한다."""
        cubeRegister[1][0:3] = myCube[0][3:6]
        cubeRegister[1][3:6] = myCube[1][3:6]
        cubeRegister[1][6:9] = myCube[2][3:6]
        myCube[0][3] = cubeRegister[1][2]
        myCube[0][4] = cubeRegister[1][5]
        myCube[0][5] = cubeRegister[1][8]
        myCube[1][3] = cubeRegister[1][1]
        myCube[1][5] = cubeRegister[1][7]
        myCube[2][3] = cubeRegister[1][0]
        myCube[2][4] = cubeRegister[1][3]
        myCube[2][5] = cubeRegister[1][6]
        self.elementReverse(0, 3)
        self.elementReverse(0, 5)
        self.elementReverse(2, 3)
        self.elementReverse(2, 5)

    def leftRight(self):
        """왼쪽 면을 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = myCube[0][6:9]
        cubeRegister[0][3:6] = myCube[1][6:9]
        cubeRegister[0][6:9] = myCube[2][6:9]
        myCube[0][6] = cubeRegister[0][2]
        myCube[0][7] = cubeRegister[0][5]
        myCube[0][8] = cubeRegister[0][8]
        myCube[1][6] = cubeRegister[0][1]
        myCube[1][8] = cubeRegister[0][7]
        myCube[2][6] = cubeRegister[0][0]
        myCube[2][7] = cubeRegister[0][3]
        myCube[2][8] = cubeRegister[0][6]
        self.elementClockwise(0, 6)
        self.elementCounterclockwise(0, 8)
        self.elementCounterclockwise(2, 6)
        self.elementClockwise(2, 8)

    def leftLeft(self):
        """왼쪽 면을 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:3] = myCube[0][6:9]
        cubeRegister[0][3:6] = myCube[1][6:9]
        cubeRegister[0][6:9] = myCube[2][6:9]
        myCube[0][6] = cubeRegister[0][6]
        myCube[0][7] = cubeRegister[0][3]
        myCube[0][8] = cubeRegister[0][0]
        myCube[1][6] = cubeRegister[0][7]
        myCube[1][8] = cubeRegister[0][1]
        myCube[2][6] = cubeRegister[0][8]
        myCube[2][7] = cubeRegister[0][5]
        myCube[2][8] = cubeRegister[0][2]
        self.elementClockwise(0, 6)
        self.elementCounterclockwise(0, 8)
        self.elementCounterclockwise(2, 6)
        self.elementClockwise(2, 8)

    def frontRight(self):
        """앞면을 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][6], myCube[0][3], myCube[0][0]]
        cubeRegister[1][0:2] = [myCube[1][6], myCube[1][0]]
        cubeRegister[0][6:9] = [myCube[2][6], myCube[2][3], myCube[2][0]]
        myCube[0][6] = cubeRegister[0][6]
        myCube[0][3] = cubeRegister[1][0]
        myCube[0][0] = cubeRegister[0][0]
        myCube[1][6] = cubeRegister[0][7]
        myCube[1][0] = cubeRegister[0][1]
        myCube[2][6] = cubeRegister[0][8]
        myCube[2][3] = cubeRegister[1][1]
        myCube[2][0] = cubeRegister[0][2]
        self.elementCounterclockwise(0, 6)
        self.elementReverse(0, 3)
        self.elementClockwise(0, 0)
        self.elementReverse(1, 6)
        self.elementReverse(1, 0)
        self.elementClockwise(2, 6)
        self.elementReverse(2, 3)
        self.elementCounterclockwise(2, 0)

    def frontLeft(self):
        """앞면을 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][6], myCube[0][3], myCube[0][0]]
        cubeRegister[1][0:2] = [myCube[1][6], myCube[1][0]]
        cubeRegister[0][6:9] = [myCube[2][6], myCube[2][3], myCube[2][0]]
        myCube[0][6] = cubeRegister[0][2]
        myCube[0][3] = cubeRegister[1][1]
        myCube[0][0] = cubeRegister[0][8]
        myCube[1][6] = cubeRegister[0][1]
        myCube[1][0] = cubeRegister[0][7]
        myCube[2][6] = cubeRegister[0][0]
        myCube[2][3] = cubeRegister[1][0]
        myCube[2][0] = cubeRegister[0][6]
        self.elementCounterclockwise(0, 6)
        self.elementReverse(0, 3)
        self.elementClockwise(0, 0)
        self.elementReverse(1, 6)
        self.elementReverse(1, 0)
        self.elementClockwise(2, 6)
        self.elementReverse(2, 3)
        self.elementCounterclockwise(2, 0)

    def sideRight(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][7], myCube[0][4], myCube[0][1]]
        cubeRegister[1][0:2] = [myCube[1][7], myCube[1][1]]
        cubeRegister[0][6:9] = [myCube[2][7], myCube[2][4], myCube[2][1]]
        myCube[0][7] = cubeRegister[0][6]
        myCube[0][4] = cubeRegister[1][0]
        myCube[0][1] = cubeRegister[0][0]
        myCube[1][7] = cubeRegister[0][7]
        myCube[1][1] = cubeRegister[0][1]
        myCube[2][7] = cubeRegister[0][8]
        myCube[2][4] = cubeRegister[1][1]
        myCube[2][1] = cubeRegister[0][2]
        self.elementReverse(0, 7)
        self.elementReverse(0, 1)
        self.elementReverse(2, 7)
        self.elementReverse(2, 1)

    def sideLeft(self):
        """앞면과 뒷면의 사이층을 앞축에 대해 시계 반대방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][7], myCube[0][4], myCube[0][1]]
        cubeRegister[1][0:2] = [myCube[1][7], myCube[1][1]]
        cubeRegister[0][6:9] = [myCube[2][7], myCube[2][4], myCube[2][1]]
        myCube[0][7] = cubeRegister[0][2]
        myCube[0][4] = cubeRegister[1][1]
        myCube[0][1] = cubeRegister[0][8]
        myCube[1][7] = cubeRegister[0][1]
        myCube[1][1] = cubeRegister[0][7]
        myCube[2][7] = cubeRegister[0][0]
        myCube[2][4] = cubeRegister[1][0]
        myCube[2][1] = cubeRegister[0][6]
        self.elementReverse(0, 7)
        self.elementReverse(0, 1)
        self.elementReverse(2, 7)
        self.elementReverse(2, 1)

    def backRight(self):
        """뒷면을 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][8], myCube[0][5], myCube[0][2]]
        cubeRegister[1][0:2] = [myCube[1][8], myCube[1][2]]
        cubeRegister[0][6:9] = [myCube[2][8], myCube[2][5], myCube[2][2]]
        myCube[0][2] = cubeRegister[0][8]
        myCube[0][5] = cubeRegister[1][1]
        myCube[0][8] = cubeRegister[0][2]
        myCube[1][2] = cubeRegister[0][7]
        myCube[1][8] = cubeRegister[0][1]
        myCube[2][2] = cubeRegister[0][6]
        myCube[2][5] = cubeRegister[1][0]
        myCube[2][8] = cubeRegister[0][0]
        self.elementCounterclockwise(0, 2)
        self.elementReverse(0, 5)
        self.elementClockwise(0, 8)
        self.elementReverse(1, 2)
        self.elementReverse(1, 8)
        self.elementClockwise(2, 2)
        self.elementReverse(2, 5)
        self.elementCounterclockwise(2, 8)

    def backLeft(self):
        """뒷면을 시계방향으로 회전한다."""
        cubeRegister[0][0:3] = [myCube[0][8], myCube[0][5], myCube[0][2]]
        cubeRegister[1][0:2] = [myCube[1][8], myCube[1][2]]
        cubeRegister[0][6:9] = [myCube[2][8], myCube[2][5], myCube[2][2]]
        myCube[0][2] = cubeRegister[0][0]
        myCube[0][5] = cubeRegister[1][0]
        myCube[0][8] = cubeRegister[0][6]
        myCube[1][2] = cubeRegister[0][1]
        myCube[1][8] = cubeRegister[0][7]
        myCube[2][2] = cubeRegister[0][2]
        myCube[2][5] = cubeRegister[1][1]
        myCube[2][8] = cubeRegister[0][8]
        self.elementCounterclockwise(0, 2)
        self.elementReverse(0, 5)
        self.elementClockwise(0, 8)
        self.elementReverse(1, 2)
        self.elementReverse(1, 8)
        self.elementClockwise(2, 2)
        self.elementReverse(2, 5)
        self.elementCounterclockwise(2, 8)

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

        for xy_rotate in range(4):
            for x_rotate in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find1[xy_rotate][x_rotate] = 1
                else:
                    find1[xy_rotate][x_rotate] = 0
            self.yRight()

        for zxzx_rotate in range(2):
            self.zRight()
            for x_rotate in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find2[zxzx_rotate][x_rotate] = 1
                else:
                    find2[zxzx_rotate][x_rotate] = 0
            self.zRight()
            self.xRight()
            if (self.ifClear() == 1):
                find3[zxzx_rotate] = 1
            else:
                find3[zxzx_rotate] = 0

        if (find1[0][0] == 1 or find1[0][1] == 1 or find1[0][2] == 1 or find1[0][3] == 1 or
            find1[1][0] == 1 or find1[1][1] == 1 or find1[1][2] == 1 or find1[1][3] == 1 or
            find1[2][0] == 1 or find1[2][1] == 1 or find1[2][2] == 1 or find1[2][3] == 1 or
            find1[3][0] == 1 or find1[3][1] == 1 or find1[3][2] == 1 or find1[3][3] == 1 or
            find2[0][0] == 1 or find2[0][1] == 1 or find2[0][2] == 1 or find2[0][3] == 1 or
            find2[1][0] == 1 or find2[1][1] == 1 or find2[1][2] == 1 or find2[1][3] == 1 or
            find3[0] == 1 or find3[1] == 1):
            return 0
        else:
            return 1

    def mixCube(self):
        self.CUBE_MIX_CEED = random.randint(1, 18)

        if (self.CUBE_MIX_CEED == 1):
            self.upRight()
        elif (self.CUBE_MIX_CEED == 2):
            self.upLeft()
        elif (self.CUBE_MIX_CEED == 3):
            self.horizonRight()
        elif (self.CUBE_MIX_CEED == 4):
            self.horizonLeft()
        elif (self.CUBE_MIX_CEED == 5):
            self.downRight()
        elif (self.CUBE_MIX_CEED == 6):
            self.downLeft()
        elif (self.CUBE_MIX_CEED == 7):
            self.rightRight()
        elif (self.CUBE_MIX_CEED == 8):
            self.rightLeft()
        elif (self.CUBE_MIX_CEED == 9):
            self.middleRight()
        elif (self.CUBE_MIX_CEED == 10):
            self.middleLeft()
        elif (self.CUBE_MIX_CEED == 11):
            self.leftRight()
        elif (self.CUBE_MIX_CEED == 12):
            self.leftLeft()
        elif (self.CUBE_MIX_CEED == 13):
            self.frontRight()
        elif (self.CUBE_MIX_CEED == 14):
            self.frontLeft()
        elif (self.CUBE_MIX_CEED == 15):
            self.sideRight()
        elif (self.CUBE_MIX_CEED == 16):
            self.sideLeft()
        elif (self.CUBE_MIX_CEED == 17):
            self.backRight()
        elif (self.CUBE_MIX_CEED == 18):
            self.backLeft()

    def saveCube(self):
        """큐브 데이터를 저장하는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        self.defNumber()

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

        self.defColor()

        con.commit()

        cursor.close()
        con.close()

    def loadCube(self):
        """저장했던 큐브 데이터를 불러오는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        NUM = []
        for n in range(54):
            NUM.append(n)
        for n in range(54):
            NUM[n] = n

        elementList = []
        for x in range(54):
            elementList.append(x)

        for x in range(54):
            cursor.execute("SELECT Element FROM pieceAddr WHERE Position = '%d'" % x)
            elementList[x] = cursor.fetchone()

        myCube[0][0][0] = elementList[0][0]
        myCube[0][0][1] = elementList[1][0]
        myCube[0][0][2] = elementList[2][0]
        myCube[0][1][0] = elementList[3][0]
        myCube[0][1][1] = elementList[4][0]
        myCube[0][2][0] = elementList[5][0]
        myCube[0][2][1] = elementList[6][0]
        myCube[0][2][2] = elementList[7][0]
        myCube[0][3][0] = elementList[8][0]
        myCube[0][3][1] = elementList[9][0]
        myCube[0][4][0] = elementList[10][0]
        myCube[0][5][0] = elementList[11][0]
        myCube[0][5][1] = elementList[12][0]
        myCube[0][6][0] = elementList[13][0]
        myCube[0][6][1] = elementList[14][0]
        myCube[0][6][2] = elementList[15][0]
        myCube[0][7][0] = elementList[16][0]
        myCube[0][7][1] = elementList[17][0]
        myCube[0][8][0] = elementList[18][0]
        myCube[0][8][1] = elementList[19][0]
        myCube[0][8][2] = elementList[20][0]
        myCube[1][0][0] = elementList[21][0]
        myCube[1][0][1] = elementList[22][0]
        myCube[1][1][0] = elementList[23][0]
        myCube[1][2][0] = elementList[24][0]
        myCube[1][2][1] = elementList[25][0]
        myCube[1][3][0] = elementList[26][0]
        myCube[1][5][0] = elementList[27][0]
        myCube[1][6][0] = elementList[28][0]
        myCube[1][6][1] = elementList[29][0]
        myCube[1][7][0] = elementList[30][0]
        myCube[1][8][0] = elementList[31][0]
        myCube[1][8][1] = elementList[32][0]
        myCube[2][0][0] = elementList[33][0]
        myCube[2][0][1] = elementList[34][0]
        myCube[2][0][2] = elementList[35][0]
        myCube[2][1][0] = elementList[36][0]
        myCube[2][1][1] = elementList[37][0]
        myCube[2][2][0] = elementList[38][0]
        myCube[2][2][1] = elementList[39][0]
        myCube[2][2][2] = elementList[40][0]
        myCube[2][3][0] = elementList[41][0]
        myCube[2][3][1] = elementList[42][0]
        myCube[2][4][0] = elementList[43][0]
        myCube[2][5][0] = elementList[44][0]
        myCube[2][5][1] = elementList[45][0]
        myCube[2][6][0] = elementList[46][0]
        myCube[2][6][1] = elementList[47][0]
        myCube[2][6][2] = elementList[48][0]
        myCube[2][7][0] = elementList[49][0]
        myCube[2][7][1] = elementList[50][0]
        myCube[2][8][0] = elementList[51][0]
        myCube[2][8][1] = elementList[52][0]
        myCube[2][8][2] = elementList[53][0]

        self.defColor()

        con.commit()

        cursor.close()
        con.close()

    def distColor(self, floor, piece, color):
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

    def defColor(self):
        """각 큐브조각의 값을 색으로 변환하는 함수"""
        for i in range(0, 3, 2):
            self.distColor(i, 4, 0)
            for l in range(1, 5):
                for m in range(2):
                    self.distColor(i, 2 * l - 1, m)
            for n in range(2):
                self.distColor(1, i, n)
                self.distColor(1, i + 6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.distColor(i, j, k)
                    self.distColor(i, j + 6, k)
        for p in range(4):
            self.distColor(1, 2 * p + 1, 0)

    def distNumber(self, floor, piece, color):
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

    def defNumber(self):
        """각 큐브조각의 색을 데이터로 변환하는 함수"""
        for i in range(0, 3, 2):
            self.distNumber(i, 4, 0)
            for l in range(1, 5):
                for m in range(2):
                    self.distNumber(i, 2 * l - 1, m)
            for n in range(2):
                self.distNumber(1, i, n)
                self.distNumber(1, i + 6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.distNumber(i, j, k)
                    self.distNumber(i, j + 6, k)
        for p in range(4):
            self.distNumber(1, 2 * p + 1, 0)

    #
    #    함수
    #    종료
    #


if __name__ == "__main__":
    print()
