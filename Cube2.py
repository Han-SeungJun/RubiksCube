#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 큐브 모듈화

import wx
import random
import sqlite3 as sq

class Cube:
    def __init__(self, mix_num = 60, time = 0.01):
        self.mix_num = mix_num
        self.time = time

    def Create_Cube(self):
        """큐브의 환경을 조성한다."""
        global Cube, CUBE
        global Resister, resister
        CUBE = [[[1,2,3],[1,3],[1,3,4],[1,2],[1],[1,4],[1,5,2],[1,5],[1,4,5]],
                [[2,3]  ,[3]  ,[4,3]  ,[2]  ,[] ,[4]  ,[2,5]  ,[5]  ,[4,5]  ],
                [[6,3,2],[6,3],[6,4,3],[6,2],[6],[6,4],[6,2,5],[6,5],[6,5,4]]]
        Cube = [[[1,2,3],[1,3],[1,3,4],[1,2],[1],[1,4],[1,5,2],[1,5],[1,4,5]],
                [[2,3]  ,[3]  ,[4,3]  ,[2]  ,[] ,[4]  ,[2,5]  ,[5]  ,[4,5]  ],
                [[6,3,2],[6,3],[6,4,3],[6,2],[6],[6,4],[6,2,5],[6,5],[6,5,4]]]
        Resister = [[[None,None,None],[None,None,None],[None,None,None],[None,None],[None],[None,None],[None,None,None],[None,None],[None,None,None]],
                    [[None,None]      ,[None]     ,[None,None]      ,[None]     ,[None],[None]      ,[None,None]     ,[None]      ,[None,None]  ],
                    [[None,None,None],[None,None],[None,None,None],[None,None],[None],[None,None],[None,None,None],[None,None],[None,None,None]]]
        resister = [None,None,None]

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
        self.Element_Mirror(1,0)
        self.Element_Mirror(1,2)
        self.Element_Mirror(1,6)
        self.Element_Mirror(1,8)

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
        self.Element_Mirror(1,0)
        self.Element_Mirror(1,2)
        self.Element_Mirror(1,6)
        self.Element_Mirror(1,8)

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
        self.Element_Left(0,0)
        self.Element_Right(0,2)
        self.Element_Right(2,0)
        self.Element_Left(2,2)

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
        self.Element_Left(0,0)
        self.Element_Right(0,2)
        self.Element_Right(2,0)
        self.Element_Left(2,2)

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
        self.Element_Mirror(0,3)
        self.Element_Mirror(0,5)
        self.Element_Mirror(2,3)
        self.Element_Mirror(2,5)

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
        self.Element_Mirror(0,3)
        self.Element_Mirror(0,5)
        self.Element_Mirror(2,3)
        self.Element_Mirror(2,5)

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
        self.Element_Right(0,6)
        self.Element_Left(0,8)
        self.Element_Left(2,6)
        self.Element_Right(2,8)

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
        self.Element_Right(0,6)
        self.Element_Left(0,8)
        self.Element_Left(2,6)
        self.Element_Right(2,8)

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
        self.Element_Left(0,6)
        self.Element_Mirror(0,3)
        self.Element_Right(0,0)
        self.Element_Mirror(1,6)
        self.Element_Mirror(1,0)
        self.Element_Right(2,6)
        self.Element_Mirror(2,3)
        self.Element_Left(2,0)

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
        self.Element_Left(0,6)
        self.Element_Mirror(0,3)
        self.Element_Right(0,0)
        self.Element_Mirror(1,6)
        self.Element_Mirror(1,0)
        self.Element_Right(2,6)
        self.Element_Mirror(2,3)
        self.Element_Left(2,0)

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
        self.Element_Mirror(0,7)
        self.Element_Mirror(0,1)
        self.Element_Mirror(2,7)
        self.Element_Mirror(2,1)

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
        self.Element_Mirror(0,7)
        self.Element_Mirror(0,1)
        self.Element_Mirror(2,7)
        self.Element_Mirror(2,1)

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
        self.Element_Left(0,2)
        self.Element_Mirror(0,5)
        self.Element_Right(0,8)
        self.Element_Mirror(1,2)
        self.Element_Mirror(1,8)
        self.Element_Right(2,2)
        self.Element_Mirror(2,5)
        self.Element_Left(2,8)

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
        self.Element_Left(0,2)
        self.Element_Mirror(0,5)
        self.Element_Right(0,8)
        self.Element_Mirror(1,2)
        self.Element_Mirror(1,8)
        self.Element_Right(2,2)
        self.Element_Mirror(2,5)
        self.Element_Left(2,8)

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
            if(CUBE[0][0] == Cube[0][0]):
                if(CUBE[0][1] == Cube[0][1]):
                    if(CUBE[0][2] == Cube[0][2]):
                        if(CUBE[0][3] == Cube[0][3]):
                            if(CUBE[0][4] == Cube[0][4]):
                                if(CUBE[0][5] == Cube[0][5]):
                                    if(CUBE[0][6] == Cube[0][6]):
                                        if(CUBE[0][7] == Cube[0][7]):
                                            if(CUBE[0][8] == Cube[0][8]):
                                                if(CUBE[1][0] == Cube[1][0]):
                                                    if(CUBE[1][1] == Cube[1][1]):
                                                        if(CUBE[1][2] == Cube[1][2]):
                                                            if(CUBE[1][3] == Cube[1][3]):
                                                                if(CUBE[1][5] == Cube[1][5]):
                                                                    if(CUBE[1][6] == Cube[1][6]):
                                                                        if(CUBE[1][7] == Cube[1][7]):
                                                                            if(CUBE[1][8] == Cube[1][8]):
                                                                                if(CUBE[2][0] == Cube[2][0]):
                                                                                    if(CUBE[2][1] == Cube[2][1]):
                                                                                        if(CUBE[2][2] == Cube[2][2]):
                                                                                            if(CUBE[2][3] == Cube[2][3]):
                                                                                                if(CUBE[2][4] == Cube[2][4]):
                                                                                                    if(CUBE[2][5] == Cube[2][5]):
                                                                                                        if(CUBE[2][6] == Cube[2][6]):
                                                                                                            if(CUBE[2][7] == Cube[2][7]):
                                                                                                                if(CUBE[2][8] == Cube[2][8]):
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


        find1 = [[None, None, None, None], [None, None, None, None], [None, None, None, None],[None, None, None, None]]
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
                    find2[zxzx][x] =0
            self.Z_Right()
            self.X_Right()
            if (self.If_Clear() == 1):
                find3[zxzx] = 1
            else:
                find3[zxzx] = 0

        if (find1[0][0] == 1 or find1[0][1] == 1 or find1[0][2] == 1 or find1[0][3] ==  1):
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
        self.Cube_Mix_Ceed = random.randint(1,18)

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
                    self.dist_Color(i, 2*l-1, m)
            for n in range(2):
                self.dist_Color(1, i, n)
                self.dist_Color(1, i+6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.dist_Color(i, j, k)
                    self.dist_Color(i, j+6, k)
        for p in range(4):
            self.dist_Color(1, 2*p+1, 0)

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
                    self.dist_Number(i, 2*l-1, m)
            for n in range(2):
                self.dist_Number(1, i, n)
                self.dist_Number(1, i+6, n)
            for j in range(0, 3, 2):
                for k in range(3):
                    self.dist_Number(i, j, k)
                    self.dist_Number(i, j+6, k)
        for p in range(4):
            self.dist_Number(1, 2*p+1, 0)


    #
    #    함수
    #    종료
    #

