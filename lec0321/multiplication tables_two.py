# 구구단 2단을 출력하시오.
for i in range(9):
    i=i+1
    print('2 X ',i,'=',2*i)
print("="*30)

for i in range(9):
    print("{} X {} = {}".format(2,i+1,2*(i+1)))
print("="*30)

for i in range(9):
    print(f"2 X {i+1} = {2*(i+1)}")
print("="*30)
