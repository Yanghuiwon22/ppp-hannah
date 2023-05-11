import random
import tkinter as tk
from tkinter import simpledialog
window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    score = 0
    num_of_problom = 5
    for i in range(num_of_problom):
        x = random.randint(2,9)
        y = random.randint(1,9)
        answer = int(gui_input(f"{x} X {y} = "))
        if x*y == answer:
            print("정답입니다!")
            score += 1

        else:
            print("오답")
    total_score = score * 100/num_of_problom
    print((f"{total_score:01f}점 입니다!"))






if __name__=="__main__":
    main()