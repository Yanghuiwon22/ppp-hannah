import math


weight = int(input("몸무게를 입력하세요(kg) => "))
height = int(input("키를 입력하세요(cm) => ")) * 0.01
BMI = weight / (math.pow(height, 2))

print(("BMI는 {}".format(round(BMI, 2))))

if 23<=BMI<25.00:
    print("비만 전단계 비만입니다.")
elif BMI<30.00:
    print("1단계 비만입니다.")
elif BMI<35.00:
    print("2단계 비만입니다.")
else:
    print("3단계 비만입니다.")
