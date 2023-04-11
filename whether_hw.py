def read_file_one_colum(filename, cul_num):
    dataset = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue
            tokens = line.strip().split(",")
            data = float(tokens[cul_num])
            dataset.append(data)
    return dataset

def read_file_one_colum_int(filename, cul_num):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:

            line_num += 1
            if line_num == 1:
                continue
            tokens = line.strip().split(",")
            rainfall = int(tokens[cul_num])
            rainfalls.append(rainfall)

    return rainfalls

def read_file_dates(filename):
    dataset = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue
            tokens = line.strip().split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            date = int(tokens[2])

            dataset.append([year, month, date])
    return dataset

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

def read_file_taver(filename):
    tem_aver = []
    with open(filename) as f:
        line_num = 0
        for line in f:

            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            t_aver = float(tokens[3])
            tem_aver.append(t_aver)

    return tem_aver

def taver_y(taver):
    aver = sum(taver)
    return aver/len(taver)

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

def sumif(rainfall, month, selected):
    total = 0
    for i in range(len(rainfall)):
        if month[i] in selected:
        # if month[i] == 6 or month[i] == 7 or month[i] == 8:
            total += rainfall[i]
    print(total)
    return total


def maximum_temp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None

    for i in range(len(tmin)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]



    return max_date, max_gap

def gdd(dates , tavg):
    for i in range(len(dates)):
        eff_temp = max(tavg[i] - 5, 0)

def main():
    filename = "../homework09/weather(146)_2022-2022 (1).csv"

    rain = read_file_summer(filename)
    taver = read_file_taver(filename)
#     1) 총 강수량은?
    print(f"총 강수량{sum(read_file_one_colum(filename,9)):.1f}mm입니다.")
#     2) 강우 일수는 ?
    print(f"총 강우일수는 {count_rain_days(read_file_one_colum(filename,9)):.1f}일입니다.")
#     3) 여름철(6월-8월) 총 강수량은?
    print(f"여름철(6월-8월) 총 강수량은 {summer_rain_days(rain):.1f}mm입니다.")
#     4) 최장연속강우일수는
    print(f"최장연속강우일수는 {longest_rain_days(read_file_one_colum(filename,9))}일입니다.")
#     5) 강우이벤트 중 최대 강수량은?
    print(f"강우이벤트 중 최대 강수량은 {largst_rain_days(read_file_one_colum(filename,9)):.1f}mm입니다.")
#     6) 일교차가 가장 큰 날짜와 해당일자의 일교차
    tmax = read_file_one_colum(filename, 3)
    tmin = read_file_one_colum(filename, 5)
    dates = read_file_dates(filename)

    max_date = maximum_temp_gap[0]
    max_gap = maximum_temp_gap[1]

    maximum_temp_gap(dates, tmax, tmin)
    print(f"일교차가 가장 큰 날짜는 {max_date}일이고, 해당일자의 일교차는 {max_gap}℃입니다.")
#     7)  5월부터 9월까지 적산온도를 구하시오.
#     8) 연평균기온
    print(f"연평균기온은 {taver_y(taver):.1f}℃입니다.")
#     9) 가장 높았던 최고기온 top3(tmax의 최댓값 3개)
    tmax = read_file_one_colum(filename, 3)
    sorted_tmax = sorted(tmax)
    print(f"가장 높았던 최고기온 top3 : {sorted_tmax[-3:]}입니다.")

    rainfall = read_file_one_colum(filename, 9)
    month = read_file_one_colum_int(filename, 1)
    print(f"6,7,8월의 강수량 합계는 {sumif(rainfall, month, [6,7,8]):.1f}mm입니다")

#     못다할 거 같은 7번
    gdd(dates, tavg)
if __name__=="__main__":
    main()

