import random
from pprint import pprint

from lec0511.gui_input import gui_input


def get_lotto():
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        lotto_num = random.randint(1, 45)
        if not lotto_num in lotto_numbers:
            lotto_numbers.append(lotto_num)
    return sorted(lotto_numbers)

def main():
    num = int(gui_input("몇 번 추출할까요?"))
    result = []
    for i in range(num):
        lotto_number = get_lotto()
        result.append(lotto_number)


    pprint(result)

if __name__=="__main__":
    main()