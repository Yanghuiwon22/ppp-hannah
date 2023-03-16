num = [10, 20, 30, 40]

numbers = [10,20,30,40,50,60,70,80,90,100]
# print(numbers[3:7])
# print(numbers[1::2])
# # [시작점:끝나기 직전:간격]
#
# # [80,90,100]
# print(numbers[-3:])
# # [100,90,80]
# numbers_rev = numbers[-3:]
# print(numbers_rev)
#
# print(numbers[-1:-4:-1])
#
# [10,20,30,40,50,60,70,80,90,100,200]
numbers.append(200)
# print(numbers)

# [10,20,30,40,50,60,70,80,90,100,200,300,400]


# numbers.append([300,400,500])
# # print(numbers)
# numbers.extend([300,400,500])
# # print(numbers)


# print(numbers)
# numbers.insert(10,[160,170,180])
# print(numbers)

numbers1= [10,20,30,40,50,60,70,80,100]
numbers2 = [200,300,400,500]
i=0
while len(numbers1)<14:
    numbers1.append(150 + 10 * i)
    i = i + 1
else:
    print(numbers1 + numbers2)









