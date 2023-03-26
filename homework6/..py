def n_list(num):
    n = int(input('숫자를 입력하세요!:'))
    x = []
    for i in range(1, n_list(n)):
        x.append(i)
    return x

def main():
    print(n_list())

if __name__ == "__main__":
    main()
