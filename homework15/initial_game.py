import random

animal_name_list = {
    "다람쥐" : "ㄷㄹㅈ",
    "하마" : "ㅎㅁ",
    "호랑이" : "ㅎㄹㅇ",
    "두더지" : "ㄷㄷㅈ"
            }

random_word = random.choice(list(animal_name_list))
quiz = animal_name_list[random_word]


def colpol():
    print(f"초성보고 단어 맞추기 게임 (동물이름)")
    print(f"===============================")
    while True:

        answer = input(f"{quiz} => ")

        try:
            if answer != random_word:
                print("다시 생각해보세요")
            else:
                print("정답입니다")
                break

        except :
            pass



def main():
    colpol()











    pass

if __name__=="__main__":
    main()