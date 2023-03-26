def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            print("윤년이 아닙니다.")

        else:
            print("윤년입니다")
    else:
        print("윤년이 아닙니다.")

def main():
    n=int(input("년도를 입력하세요 : "))
    return is_leap_year(n)

if __name__=="__main__":
    main()
    