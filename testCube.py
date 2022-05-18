import Cube2

Cube2.Create_Cube()

Round_Count = 0

while(1):

    Cube2.Y_Right()

    Round_Count += 1
    if (Cube2.Clear_Cube() == 0):
        print("큐브가 맞춰졌습니다!!")
        break
    else:
        continue

print('돌린 수 : ', Round_Count, '\n')