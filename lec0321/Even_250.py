# 1부터 250까지 짝수의 합은?
total=0
for i in range(250):
    i=i+1
    if i%2==0:
        total=total+i
print(total)
print(f"1부터 250까지 짝수의 합은 {total}입니다.")
print('='*30)

total=0
for n in range(1,251):
    if n % 2 == 0:
        total = total + n
print(total)
print(f"1부터 250까지 짝수의 합은 {total}입니다.")
print('='*30)

