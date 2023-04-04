def text2list(text):
    numbers = []
    numbers = [int(x) for x in text.split()]
    return numbers

def text2list_csv(text):
    numbers = []
    numbers = [int(x) for x in text.split(",")]
    return numbers


def text2list_csv_multi(text):
    numbers = []
    numbers = [int(x) for x in text.split("\n")]
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

def read_textfile(filename):
    with open(filename) as f:
        text = f.readline()
        return text

def read_textfile_multi(filename):
    with open(filename) as f:
        text = f.read().strip()
        print(f"!{text}")
        return text

def read_textfile_as_list(filename):
    with open(filename) as f:
        nums = []
        for line in f.readlines():
            nums.append(int(line))

        return text

def main():
    input_text = "5 10 3 4 7 8"
    input_text = read_textfile("numbers2.csv")
    input_text = read_textfile_multi("numbers3.csv")
    print(f"!{input_text}")

    nums = text2list(input_text)
    nums = text2list_csv(input_text)



    print("주어진 리스트는",nums)
    print(f"평균값은 {average(nums):.1f}")
    print(f"중앙값은 {median(nums)}")
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

    return nums

if __name__=="__main__":
    main()
