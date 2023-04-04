def text2list(text):
    numbers = []
    numbers = [int(x) for x in text.split()]
    return numbers

def average(nums):
    total = 0
    for n in nums:
        total += n
    aver = total / len(nums)
    if len(nums) == 0:
        return None
    return aver

def median(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[(len(sorted_nums)//2)]


def main():
    input_text = "5 10 3 4 7 8"
    nums = text2list(input_text)
    print("주어진 리스트는",nums)
    print(f"평균값은 {average(nums):.1f}")
    print(f"중앙값은 {median(nums)}")
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

    return nums

if __name__=="__main__":
    main()
