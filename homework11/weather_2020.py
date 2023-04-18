import os.path

import requests
from requests import Response


def read_file(filename):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:

            print(line.split((",")))

            line_num += 1
            if line_num == 1:
                continue
            # 방법 1
            tokens = line.strip().split(",")
            rainfall = float(tokens[9])
            rainfalls.append(rainfall)
            print(rainfall)

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

def count_rain_days(rainfalls):
    count = 0
    for num in rainfalls:
         if num >= 0.1:
             count += 1
    return count

def longest_rain_days(rainfalls):
    longest_days = 0
    days = 0
    for nums in rainfalls:
        if nums > 0.0:
            longest_days += 1
        else:
            if longest_days > days:
                days = longest_days
            else:
                longest_days = 0

    rainyday_count = 0
    rain_event_days=[]
    for rainfall in rainfalls:
        if rainfall > 0:
            rainyday_count += 1
        if rainfall == 0 and rainyday_count > 0:
            rain_event_days.append(rainyday_count)



    return days
def main():
    filename = "./weather_146_2022.csv"

    if not os.path.exists(filename):
        URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
        with open("./weather_146_2022.csv", "w", encoding="UTF-8-sig") as f:
            res: Response = requests.get(URL)
            res.encoding = "UTF-8"
            f.write(res.text)
    with open("result.txt","w", encoding="UTF-8-sig") as fout:
        rainfall = read_file(filename)
    #     1) 총 강수량은?
        print(f"총 강수량{sum(rainfall):.1f}mm입니다.")
        fout.write(f"총 강수량{sum(rainfall):.1f}mm입니다.")
        fout.write("\n")

    #     2) 강우 일수는 ?
        print(f"총 강우일수는 {count_rain_days(rainfall):.1f}일입니다.")
        fout.write(f"총 강우일수는 {count_rain_days(rainfall):.1f}일입니다.")
        fout.write("\n")


    #     3)
    #     4) 최장연속강우일수는
        print(f"최장연속강우일수는 {longest_rain_days(rainfall)}일입니다.")
        fout.write(f"최장연속강우일수는 {longest_rain_days(rainfall)}일입니다.")
        fout.write("\n")


    #     5)


#
if __name__=="__main__":
    main()
