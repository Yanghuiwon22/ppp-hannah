import math

a1 = int(input("첫 x의 위치를 입력하세요"))
a2 = int(input("첫 y의 위치를 입력하세요"))

b1 = int(input("두번째 x의 위치를 입력하세요"))
b2 = int(input("두번째 y의 위치를 입력하세요"))

length = (b1-a1)**2 + (b2-a2)**2
llength = round(math.sqrt(length), 2)

print("두 지점 사이의 거리는 {} 입니다.".format(llength))

# 수업 내용
if llength <= 1:
    print("두 점이 너무 가깝습니다.")
else:
    print("두 점의 거리가 적당합니다.")

