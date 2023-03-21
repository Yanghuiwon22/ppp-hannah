def gugudan(num):
    for i in range(9):
       print(f"{num} X {i+1} = {num*(i+1)}")



if __name__ == "__main__":
    gugudan(int(input("몇 단을 출력할까요?")))

