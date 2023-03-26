def n_list(num):
    x = []
    for i in range(1, num + 1):
        x.append(i)
    return x

def main():
    n = int(input('숫자를 입력하세요!:'))
    print(n_list(n))

if __name__ == "__main__":
    main()
