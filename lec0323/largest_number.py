def largest(a, b, c):
    if a > b:
        if a > c:
            num = a
        else:
            num = c
    else:
        if b > c:
            num = b
        else:
            num = c
        return num


def main():
    x1 = 5
    x2 = 7
    x3 = 2
    print("가장 큰 수는 {}입니다".format(largest(x1,x2,x3)))

if __name__ == "__main__":
    main()
