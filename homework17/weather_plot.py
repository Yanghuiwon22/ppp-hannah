import os
from typing import List

import requests
import matplotlib.pyplot as plt


def download_weather(filename: str) -> None:
    """기상청에서 자료를 다운받아서 저장합니다."""
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19820101&endDt=20211231&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19810101&startYear=1981&endDay=20221231&endYear=2022&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="

    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", newline="") as f:
            f.write(res.text)


def str2float(text: str, default_value: float = -999) -> float:
    try:
        return float(text)
    except ValueError:
        return default_value


def read_data(filename) -> (List[str], List[float], List[float]):
    """기상자료를 읽어서 날짜, 최저기온, 최고기온 리스트를 리턴합니다."""
    date_list = []
    tavg_list = []
    tmin_list = []
    tmax_list = []

    with open(filename) as f:
        lines = f.readlines()
        for line in lines[8:]:
            line = line.strip()
            if line == "":
                continue
            tokens = line.split(",")
            date_list.append(tokens[0].split("-"))
            tavg_list.append(str2float(tokens[2], 999))
            tmin_list.append(str2float(tokens[3], 999))
            tmax_list.append(str2float(tokens[4], -999))

    return date_list, tavg_list, tmin_list, tmax_list



def making_dates_list(dates, input_month, input_day):
    dates_list = []
    for i in range(len(dates)):
        if input_month == dates[i][1] and input_day == dates[i][2]:
            dates_list.append(dates[i])
    return dates_list

def aver_tem(dates,tavg, input_month, input_day):
    tem = 0
    dates_list = []
    for i in range(len(dates)):
        if input_month == dates[i][1] and input_day == dates[i][2]:
            dates_list.append(dates[i])
            tem += tavg[i]

    return tem / 42


def main():
    # 1) 데이터 구해오기 (기상청)
    filename = "./history_jeonju.csv"
    download_weather(filename)
    # 2) 데이터 읽기 (주의: 빈 데이터 처리하기)
    dates, tavg, tmin, tmax = read_data(filename)

    # 3) 특정 날짜 받기
    input_month = input("특정 month를 입력하세요(00월)")
    input_day  = input("특정 day를 입력하세요(00일)")
    print(f"특정 날짜는 {input_month}월 {input_day}일 입니다!")
    print(making_dates_list(dates, input_month, input_day))

    # 4) 특정 날짜의 평균 기온은?
    print(f"해당 날짜의 평균기온은 {aver_tem(dates, tavg, input_month, input_day):.1f}")











if __name__ == "__main__":
    main()
