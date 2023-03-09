import math


weight = int(input("몸무게를 입력하세요(kg) => "))
height = int(input("키를 입력하세요(cm) => ")) * 0.01
BMI = weight / (math.pow(height, 2))

print(("BMI는 {}".format(round(BMI, 2))))