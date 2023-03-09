Hanrabong = int(input("한라봉을 몇 그램(g) 섭취하셨습니까?"))
strawberry = int(input("딸기(설향)을 몇 그램(g) 섭취하셨습니까?"))
banana = int(input("바나나을 몇 그램(g) 섭취하셨습니까?"))

HanrabongK = Hanrabong * (50/100)
strawberryk = strawberry * (34/100)
bananaK = banana * (77/100)

print((HanrabongK + strawberryk + bananaK), "Kcal를 섭취하셨습니다.")
