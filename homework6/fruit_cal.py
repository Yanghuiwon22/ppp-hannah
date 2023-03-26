
def fruit_cal(x, y, z):
    calories = {"한라봉": 50, "딸기": 34, "바나나": 77}

    total_calories = 0
    total_calories += x * calories["바나나"] / 100
    total_calories += y * calories["한라봉"] / 100
    total_calories += z * calories["딸기"] / 100

    return total_calories

def main():
    # fruit_banana = int(input("먹은 바나나의 무게(kg):"))
    # fruit_strqwberry = int(input("먹은 딸기의 무게(kg):"))
    # fruit_hanrabong = int(input("먹은 한라봉의 무게(kg):"))

    fruit_banana=100
    fruit_strqwberry=100
    fruit_hanrabong=100
    print(fruit_cal(fruit_banana, fruit_strqwberry, fruit_hanrabong))

if __name__ == "__main__":
    main()
