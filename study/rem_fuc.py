# sum함수의 필요성
nums = [1,2,3,4,5,6,7]
total=0
for n in nums:
    total += n
print(total)

print(sum(nums))

# ************************************************

# abs함수는 절댓값 계산 함수이다.
print(abs(-20))

# len() 길이세기 함수

# 리스트의 연결은 덧셈으로
list = [4,4,4,4,4]
print(nums+list)
# 리스트 전체에서 뒤에서부터 2개씩
print(nums[::-2])
# 최대최소함수 min() max()
# 가운데함수 center()