import os.path

import request


def read_file_dates(filename, col_num = 9):
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
            day = int(tokens[2])
            dataset.append([year, month, day])
    return dataset


def read_file(filename):
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

    return rainfalls


def read_file_one_colimn(filename, col_num = 9):
    dataset = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            data = float(tokens[col_num])
            dataset.append(data)

    return dataset


def read_file_one_colimn_int(filename, col_num = 9):
    dataset = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            data = int(tokens[col_num])
            dataset.append(data)

    return dataset


def count_rain_days(rainfalls):
    count = 0
    for num in rainfalls:
        if num >= 0.1:
            count += 1
    return count


def longest_rain_days(rainfalls):
    rain_event_days = []

    rainday_count = 0
    for rainfall in rainfalls:
        if rainfall > 0:
            rainday_count += 1
        if rainfall == 0 and rainday_count > 0:
            rain_event_days.append(rainday_count)
            rainday_count = 0
    if rainday_count > 0:
        rain_event_days.append(rainday_count)

    return max(rain_event_days)


def maximum_rainfall_event(rainfalls):
    rain_event_total = []

    rainday_count = 0
    rainday_total = 0
    for rainfall in rainfalls:
        if rainfall > 0:
            rainday_count += 1
            rainday_total += rainfall
        if rainfall == 0 and rainday_count > 0:
            rain_event_total.append(rainday_total)
            rainday_count = 0
            rainday_total = 0
    if rainday_count > 0:
        rain_event_total.append(rainday_total)

    return max(rain_event_total)


def annual_average(tavgs):
    return sum(tavgs) / len(tavgs)
    # total = 0
    # count = 0
    # for tavg in tavgs:
    #     total = total + tavg
    #     count = count + 1
    # return total / count


def sumifs(rainfall, months, selected=[6, 7, 8]):
    total = 0
    for i in range(len(rainfall)):
        if months[i] in selected:
            total += rainfall[i]
    return total


def maximum_temp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None
    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]
    return max_date, max_gap


def gdd(dates,tavg):
    total_eff_temp = 0
    for i in range(len(dates)):
        eff_temp = max(tavg[i] - 5, 0)
        if dates[i][1] in [5, 6, 7, 8, 9]:
        # month_num = [5, 6, 7, 8, 9]
        # if dates[i][1] in month_num:
            total_eff_temp += eff_temp

    return total_eff_temp


def main():
    filename = "./weather(146)_1960-2022.csv"

    if not os.path.exists(filename):
        URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
        with open(filename, "w", encoding="UTF-8") as f:
            res = requests.get(URL)
            res.encoding = "UTF-8"
            f.write(res.text)

    with open("result.txt", "w",  encoding="UTF-8") as fout:
        rainfall = read_file_one_colimn(filename)

        # 1) 총 강수량은 ?
        fout.write(f"총 강수량은 {sum(rainfall):.1f}mm 입니다.")
        fout.write("\n")

        # 2) 강우 일수는 ?(1mm 이상 온 날의 수)
        fout.write(f"총 강우 일수는 {count_rain_days(rainfall):.1f}일 입니다.")
        fout.write("\n")

        # 4) 최장 연속 강우 일수는 ?
        fout.write(f"최장 연속 강우 일수는 {longest_rain_days(rainfall)}일 입니다.")
        fout.write("\n")

        # 5) 강우 이벤트 중 최대 강수량은? 비가 연속으로 올때, 하나의 강우 이벤트로 가정
        fout.write(f"최대 강수량은 {maximum_rainfall_event(rainfall):.1f}mm 입니다.")
        fout.write("\n")



        # 6) 연평균 기온(tavg의 평균)은?
        tavg = read_file_one_colimn(filename, 4)
        tmax = read_file_one_colimn(filename, 3)
        rainfall = read_file_one_colimn(filename, 9)
        fout.write(f"연평균 기온은 {annual_average(tavg):.1f} 도 입니다.")
        fout.write("\n")

        # 7) 가장 더운날 top 3(tmax의 최대값 3개)는?
        tmax = read_file_one_colimn(filename, 3)
        sorted_tmax = sorted(tmax)
        fout.write(f"가장 높았던 최고기온은 top 3: {list(reversed(sorted(tmax)[-3:]))} 입니다.")
        fout.write("\n")

        # 못다한 3번
        rainfall = read_file_one_colimn(filename)
        months = read_file_one_colimn_int(filename, 1)
        fout.write(f"6, 7, 8월의 강수량 합계는 {sumifs(rainfall, months, selected=[6, 7, 8]):.1f}mm입니다.")
        fout.write("\n")

        # 못다한 6번
        tmin = read_file_one_colimn(filename, 5)
        dates = read_file_dates(filename)
        max_date, max_gap = maximum_temp_gap(dates, tmax, tmin)  # [2021, 1, 20], 23.2
        fout.write(f"일교차가 가장 큰 날짜는 {max_date}이고 해당일자의 일교차는 {max_gap:.1f}도 입니다.")
        fout.write("\n")

        # 못다한 못다할 것 같은 ... 7번
        fout.write(f"5, 6, 7, 8, 9월의 적산 온도의 합은 {gdd(dates, tavg):.1f}도 입니다.")
        fout.write("\n")


if __name__ == "__main__":
    main()