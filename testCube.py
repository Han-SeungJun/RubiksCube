import Cube2

myCube = Cube2

myCube.createCube()

Round_Count = 0

while(1):

    myCube.yRight()

    Round_Count += 1
    if (myCube.clearCube() == 0):
        print("큐브가 맞춰졌습니다!!")
        break
    else:
        continue

print('돌린 수 : ', Round_Count, '\n')