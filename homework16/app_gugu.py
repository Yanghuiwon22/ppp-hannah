import random
import tkinter as tk
from tkinter import simpledialog
from lec0321 import color_text
window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    score = 0
    num_of_problom = int(gui_input("몇 문제를 푸시겠습니까?"))
    for i in range(num_of_problom):
        x = random.randint(2,9)
        y = random.randint(1,9)
        answer = int(gui_input(f"{x} X {y} =                    ({score}/{num_of_problom})"))
        if x*y == answer:
            print(color_text.text_blue("정답입니다!"))
            score += 1

        else:
            print(color_text.text_red("오답입니다 -.-"))
    total_score = score * 100/num_of_problom
    print((f"{total_score:.1f}점 입니다!"))






if __name__=="__main__":
    main()