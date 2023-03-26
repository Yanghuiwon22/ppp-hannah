def average(nums):
    total = 0
    for n in nums:
        total = total + n
    print(total)
    return total



def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    print(len(x))
    print(average(x)/len(x))


if __name__ == "__main__":
    main()