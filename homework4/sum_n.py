def sum_n(num):
    total = 0
    for i in range(num):
        i = i + 1
        total = total + i
        print(total)
    print(f"1부터 {num}까지 합은 {total}입니다.")

if __name__ == "__main__":
    sum_n(int(input("몇까지 더할까요?:")))





