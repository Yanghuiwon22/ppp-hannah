def average(nums):
    total = 0
    count = 0
    for n in nums:
        total += n
        count += 1
        if count == 0:
            return None
    return total / count


def main():
    nums = []
    print("주어진 리스트는",nums)
    print("평균은{:.1f}".format(average(nums)))

if __name__ == "__main__":
    main()


[n for n in range(nums)]