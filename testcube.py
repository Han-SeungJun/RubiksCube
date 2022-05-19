import cube

cubic_object = cube.CubeBody

cubic_object.createCube()

Round_Count = 0

while(1):

    cubic_object.yRight()

    Round_Count += 1
    if (cubic_object.clearCube() == 0):
        print("큐브가 맞춰졌습니다!!")
        break
    else:
        continue

print('돌린 수 : ', Round_Count, '\n')