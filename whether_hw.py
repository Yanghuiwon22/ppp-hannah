def read_file(filename):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:



            line_num += 1
            if line_num == 1:
                continue
            # 방법 1
            tokens = line.strip().split(",")
            rainfall = float(tokens[9])
            rainfalls.append(rainfall)


            # 방법 2
            # tokens = line.split(",")
            # rain = float(tokens[9])
            # print(rain)
        #
        # for i,line in enumerate(f):
        #     if 1 == 0:
        #         continue
        #     tokens = line.split(",")
        #     rain = float(tokens[9])
        #     print(rain)

    return rainfalls

def read_file_summer(filename):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            rainfall = float(tokens[9])
            rainfalls.append(rainfall)
        rainy_sum = rainfalls[153:245]
    return rainy_sum

def read_file_daily(filename):
    tem = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            tmax = float(tokens[3])
            tmin = float(tokens[5])
            tem.append(tmax-tmin)
            print(tem)
    return tem


def count_rain_days(rainfalls):
    count = 0
    for num in rainfalls:
         if num >= 0.1:
             count += 1
    return count

def longest_rain_days(rainfalls):
    rainyday_count = 0
    rain_event_days=[]
    for rainfall in rainfalls:
        if rainfall > 0:
            rainyday_count += 1
        if rainfall == 0 and rainyday_count > 0:
            rain_event_days.append(rainyday_count)
            rainyday_count = 0
    if rainyday_count > 0:
        rain_event_days.append(rainyday_count)


    return max(rain_event_days)

def summer_rain_days(rainfalls):
    count = 0
    for num in rainfalls:
         if num >= 0.1:
             count += num
    return count

def largst_rain_days(rainfalls):
    rainyday_count = 0
    rainyday = 0
    rain_event_days = []
    for rainfall in rainfalls:
        if rainfall > 0.0:
            rainyday += rainfall
            rainyday_count += 1
        if rainfall == 0.0 and rainyday_count > 0:
            rain_event_days.append(rainyday)
            rainyday = 0
            rainyday_count = 0

    if rainyday_count > 0:
        rain_event_days.append(rainyday_count)

    return max(rain_event_days)

def maximum_temp_gap(dates, tmax, tmin):
    tem_count = 0
    tem_daily = []
    tem_daily.append(tmax-tmin)


    return [dates, tem_daily]


def main():
    filename = "../homework09/weather(146)_2022-2022 (1).csv"
    rainfall = read_file(filename)
    rain = read_file_summer(filename)

#     1) 총 강수량은?
    print(f"총 강수량{sum(rainfall):.1f}mm입니다.")
#     2) 강우 일수는 ?
    print(f"총 강우일수는 {count_rain_days(rainfall):.1f}일입니다.")
#     3) 여름철(6월-8월) 총 강수량은?
    print(f"여름철(6월-8월) 총 강수량은 {summer_rain_days(rain):.1f}mm입니다.")
#     4) 최장연속강우일수는
    print(f"최장연속강우일수는 {longest_rain_days(rainfall)}일입니다.")
#     5) 강우이벤트 중 최대 강수량은?
    print(f"강우이벤트 중 최대 강수량은 {largst_rain_days(rainfall):.1f}mm입니다.")
#     6) 일교차가 가장 큰 날짜와 해당일자의 일교차
#    print(f"일교차가 가장 큰 날짜는 {maximum_temp_gap[0]}일이고, 해당일자의 일교차는 {maximum_temp_gap[1]}℃입니다.")
#     7)  5월부터 9월까지 적산온도를 구하시오.


if __name__=="__main__":
    main()

