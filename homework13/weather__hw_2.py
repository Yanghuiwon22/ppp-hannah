import os.path

import requests

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


def read_file(filename, cul_num):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue

            tokens = line.strip().split(",")
            rainfall = float(tokens[cul_num])
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


def maximum_temp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None
    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]
    return max_date, max_gap



def maximum_temp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None
    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]
    return max_date, max_gap


def maximun_rainfallss_gap(dates, rainfall):
    max_date = None
    max_rainfalls = None
    for i in range(len(dates)):
        rainfalll = rainfall[i]
        if max_rainfalls is None or max_rainfalls < rainfalll:
            max_rainfalls = rainfalll
            max_date = dates[i]
    return max_date, max_rainfalls

def maximum_tempp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None
    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]
    return max_date, max_gap

def submit(name: str, rain_max: float, rain_max_date: str, gap_max: float, gap_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbyNex1PwGoPeR9Be--QlYrD90C8CR6FU_CC82K2EaGrc2-uVHtbHOw7ZwjfNTESHA5Eiw/exec"
    PARAMS = {
        '제출자': name,
        '최대강수량': rain_max,
        '최대강수량날짜': rain_max_date,
        '최대일교차': gap_max,
        '최대일교차날짜': gap_max_date,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")

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

        #비가 가장 많이 온 날짜와 강수량(9)
        dates = read_file_dates(filename)
        max_date, max_rainfalls = maximun_rainfallss_gap(dates,rainfall)  # [2021, 1, 20], 23.2
        tmin = read_file_one_colimn(filename, 5)
        tmax = read_file_one_colimn(filename, 3)

#       가장 큰 일교차와 해당 일자
        max_dates, max_gap = maximum_tempp_gap(dates, tmax,tmin)
        print(f"일교차가 가장 큰 날짜는 {max_dates}이고 해당일자의 일교차는 {max_gap:.1f}도 입니다.")
        submit("양희원", max_date, max_rainfalls, max_dates, max_gap)
        print("양희원", max_date, max_rainfalls, max_dates, max_gap)



if __name__ == "__main__":
    main()

