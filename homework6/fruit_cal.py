fruit_banana = int(input("먹은 바나나의 무게(kg):"))
fruit_strqwberry = int(input("먹은 딸기의 무게(kg):"))
fruit_hanrabong = int(input("먹은 한라봉의 무게(kg):"))

calories = {"한라봉":50, "딸기":34, "바나나":77}

total_calories = 0
total_calories += fruit_banana * 77 / 100
total_calories += fruit_hanrabong * 50 / 100
total_calories += fruit_strqwberry * 34 / 100

print(total_calories)
#
total_calories = 0
total_calories += fruit_banana * calories["바나나"] / 100
total_calories += fruit_hanrabong * calories["한라봉"] / 100
total_calories += fruit_strqwberry * calories["딸기"] / 100

print(total_calories)
