import random


def main():
    problems = ["apple", "mango", "banana"]
    problem = random.choice(problems)
    print(problem)

    answer = []
    for i in range(len(problem)):
        answer.append("_")

    life = 7
    while life > 0:

        text = input(f"life = {life} 답을 입력하세요 =>")
        for i, x in enumerate(problem):
            if text == x:
                answer[i] = x
                is_correct = True
        if is_correct:
            pass
        else:
            life -= 1
            break

        if ''.join(answer) == problem:
            print("정답입니다!")
            break








if __name__=="__main__":
    main()