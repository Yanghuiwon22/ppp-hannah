import weather__hw_2
import requests

def read_file(filename, cul_num):
    datas = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if 1 <= line_num <9:
                continue
            tokens = line.strip().split(",")
            try:
                data = float(tokens[cul_num])
            except ValueError:
                data = float(0)
            datas.append(data)
    return datas

def read_file_str(filename, cul_num):
    datas = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if 1 <= line_num < 9:
                continue
            tokens = line.strip().split(",")
            data = str(tokens[cul_num].strip())
            datas.append(data.strip('"')) # 이 부분을 수정해주면 됩니다.

    return datas


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

def max_temp(dates, tmax):
    max_date = None
    max_temp = None
    for i in range(len(dates)):
        temp = tmax[i]
        if max_temp is None or max_temp < temp:
            max_temp = temp
            max_date = dates[i]

    return max_date, max_temp

def maximum_temp_gap(dates, tmax, tmin):
    max_date = None
    max_gap = None
    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if max_gap is None or max_gap < gap:
            max_gap = gap
            max_date = dates[i]
    return max_date, max_gap

def main():
    filename = "ta_20230427153522.csv"
    with open(filename, encoding="euc-kr") as f:

        dates = read_file_str(filename, 0)
        tmax = read_file(filename, 4)
        tmin = read_file(filename, 3)
        print(f"가장 더웠던 날의 온도는 {max_temp(dates, tmax)[1]}")
        print(f"가장 더웠던 날은{max_temp(dates, tmax)[0]}")

        print(f"일교차가 가장 큰 날의 일교차는 {maximum_temp_gap(dates, tmax, tmin)[1]}")
        print(f"일교차가 가장 큰 날은{maximum_temp_gap(dates, tmax, tmin)[0]}")

        # print("양희원", max_temp, max_temp_date, max_temp_gap, max_temp_gap_date)


#       이름, 가장 더웠던 날의 온도, 더웠던 날짜, 일교차가 가장 큰 날의 일교차, 일교차가 가장 큰 날
        weather__hw_2.submit("양희원", max_temp(dates, tmax)[1], max_temp(dates, tmax)[0], maximum_temp_gap(dates, tmax, tmin)[1], maximum_temp_gap(dates, tmax, tmin)[0])


if __name__=="__main__":
    main()
