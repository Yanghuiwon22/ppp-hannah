def largest(numbers):
    max_number=-1000
    for n in numbers:
        if max_number < n:
            max_number = n
    return max_number

def main():
    nums = [5,7,2,10]
    print("가장 큰 수는 {}입니다".format(largest(nums)))

if __name__ == "__main__":
    main()
