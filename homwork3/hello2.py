import math

x1 = int(input("첫 x의 위치를 입력하세요"))
y1 = int(input("첫 y의 위치를 입력하세요"))
x2 = int(input("두번째 x의 위치를 입력하세요"))
y2 = int(input("두번째 y의 위치를 입력하세요"))

length = (x2-x1)**2 + (y2-y1)**2
llength = round(math.sqrt(length), 2)

print("두 지점 사이의 거리는 {} 입니다.".format(llength))

if x1 > 0 and y1 > 0:
    print("첫번째 좌표는 1사분면입니다.")
elif x1 < 0 and y1 > 0:
    print("첫번째 좌표는 2사분면입니다.")
elif x1 < 0 and y1 < 0:
    print("첫번째 좌표는 3사분면입니다.")
elif x1 > 0 and y1 < 0:
    print("첫번째 좌표는 4사분면입니다.")

if x2 > 0 and y2 > 0:
    print("두번째 좌표는 1사분면입니다.")
elif x2 < 0 and y2 > 0:
    print("두번째 좌표는 2사분면입니다.")
elif x2 < 0 and y2 < 0:
    print("두번째 좌표는 3사분면입니다.")
elif x2 > 0 and y2 < 0:
    print("두번째 좌표는 4사분면입니다.")