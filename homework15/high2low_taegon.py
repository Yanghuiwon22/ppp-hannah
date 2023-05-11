# 대문자를 소문자로 소문자를 대문자로
def toggle_text(text:str):
    text_list = []
    for i in text:
        try:
            if 65 <= ord(i) <=90:
                char1 = ord(i) - ord("A")
                char2 = chr(ord("a") + char1)
                # print(char2)
                # print(char1)
                text_list.append(char2)
            elif 97 <= ord(i) <= 112:
                char3 = ord(i) - ord("a")
                char4 = chr(ord("A") + char3)
                # print(char4)

                # print(char2)
                text_list.append(char4)
                # print(ord("a"))
            # if 65 <= ord(i) <=90 or 97 <= ord(i) <= 112:
            #     print(f"{text} => {''.join(toggle_text(text))}")



        except:
            pass
    return text_list

# def only_en(text):
#     for i in text:
#         if 65 <= ord(i) <=90 or 97 <= ord(i) <= 112:
#
#


def main():
    text = input("영어를 입력하세요!")
    # text = "ABCdef"
    print(f"{text} => {''.join(toggle_text(text))}")


if __name__=="__main__":
    main()