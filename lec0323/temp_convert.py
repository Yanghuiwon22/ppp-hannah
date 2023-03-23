def c2f(c):
    f = c * 1.8 + 32
    return f

def f2c(t):
    result = (t - 32) * 5 / 9
    return result


def main():
    temp_c = 15
    temp_f = c2f(temp_c)
    print(f'섭씨 {temp_c}도는 화씨로{temp_f}입니다.')
    print(f'화씨 {temp_f}도는 섭씨로{f2c(temp_f)}입니다.')



if __name__ == "__main__":
    main()
