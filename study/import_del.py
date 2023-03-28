
# 리스트를 키보드로 입력받아서 하는 프로그램을 짜봤습니다.

from lec0321 import color_text
# 이건 같은 파일이 아니라도 불러오는 명령어

def average(nums):
    total = 0
    for n in nums:
        total = total + n
    print(f"리스트의 합은 {total}입니다.")
    return total


def main():
    pass
    x = []
    print(color_text.text_pink("리스트 추가를 끝내고 싶으면 '0'을 입력하세요!"))
    while True:
        n=int(input("정수를 입력하세요:"))

        # 정수에 0을 입력하면 리스트 추가가 끝나게 했습니다.
        if n==0:
            print("리스트 추가가 끝났습니다.")
            print("="*50)
            print(f"리스트는 {x}입니다.")
            break
        x.append(n)

    print(f"리스트의 평균은 {average(x)/len(x)}입니다.")


if __name__ == "__main__":
    main()

# color_text가 화면에 안보였으면 좋겠어요!

# 그렇다면 if __name__=="__main__": 안으로 넣으면 된다!