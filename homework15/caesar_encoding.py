
def caesar_encode(text:str, shift:int = 3):
    text_list = []
    for i in text:
        char1 = ord(i) - ord("A")
        if 65 <= ord(i) <=90:
            char1 = ord(i) - ord("A")
            encode_word = chr(ord("A") + char1 + 3)


            text_list.append(encode_word)
        elif 97 <= ord(i) <= 112:
            char3 = ord(i) - ord("a")
            char4 = chr(ord("a") + char3 + 3)

            text_list.append(char4)

    return text_list

def caesar_decode(text:str, shift:int = 3):
    text_list = []
    for i in text:
        # print("========================================")
        # print(i)
        # print(ord("z"))
        # print(f"{i}의 야스키코드는 {ord(i)}입니다")
        if 65 <= ord(i) <=90:
            char1 = ord(i) - ord("A")
            char2 = chr(ord("A") + char1 -3)

            # print(f"A와 간격은 {char1}")
            # print(char2)

            text_list.append(char2)
        elif 97 <= ord(i) <= 122:
            char3 = ord(i) - ord("a")
            char4 = chr(ord("a") + char3 -3)

            # print(f"A와 간격은 {char3}")
            # print(char4)

            text_list.append(char4)

    return text_list

def main():
    text = input("입력하세요!(영어로) => ")
    # text = "ABC"
    # text = "AbC"
    # text = "AppLe"

    # print(caesar_encode("ABC"))
    # print(caesar_decode("Def"))
    print(f"암호화 : {text} => {''.join(caesar_encode(text))}")
    print(f"해독 : {''.join(caesar_encode(text))} => {''.join(caesar_decode(caesar_encode(text)))}")
    pass

if __name__=="__main__":
    main()