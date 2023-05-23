class Cake:
    coat = "생크림"

    def __init__(self, topping, price, candle=0):
        self.topping = topping
        self.price = price
        self.candle = candle

    def desc(self):
        print(f"토핑: {self.topping}")
        print(f"가격: {self.price}")
        print(f"초갯수: {self.candle}")

def main():
    cake1 = Cake("딸기", 3000)
    cake2 = Cake("포도", 7000)
    cake3 = Cake("치즈", 6000)

    cakes = [cake1, cake2, cake3]

    for cake in cakes:
        print("케이크 정보를 출력합니다")
        cake.desc()

    pass

if __name__=="__main__":
    main()

