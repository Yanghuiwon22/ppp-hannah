
def gugudan(n):
    for i in range(9):
        print(f"{n} X {i+1} = {n*(i+1)}")
#     return None


def main():
    # dan = int(input("몇단을 출력할까요? :"))
    dan = 5
    gugudan(dan)

if __name__ == "__main__":
    main()
