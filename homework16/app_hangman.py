import random

from lec0511.gui_input import gui_input


def main():
    global is_correct
    problems = ["apple", "mango", "banana"]
    problem = random.choice(problems)
    print(problem)

    answer = []
    for i in range(len(problem)):
        answer.append("_")

    life = 7
    while life > 0:
        print(''.join(answer))
        text = gui_input(f"life = {life} 답을 입력하세요 =>")
        is_correct = False

        for i, x in enumerate(problem):
            print(i)
            if x==text:
                answer[i] = x
                is_correct = True
        if is_correct:
            pass
        else:
            life -= 1



        if ''.join(answer) == problem:
            print("정답입니다!")
            break



if __name__=="__main__":
    main()