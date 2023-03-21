mart ={"우유":2800, "계란":300, "빵":1200, "물":1700}
cart=["물","물","계란","빵","빵","빵"]
total_cost=0
for item in cart:
    if item=="물":
        total_cost +=  1700
    if item == "계란":
        total_cost += 300
    if item == "우유":
        total_cost +=2800
    if item == "빵":
        total_cost +=  1200
print(f"총 구매금액은 {total_cost}원입니다.")
