
def main():
    max_date = [2005, 8, 3]
    max_year = 2005
    max_month = 8
    max_day = 3


    print(max_date)
    print(f"{max_year}-{max_month:02}-{max_day:02}")
    print(f"{max_date[0]}-{max_date[1]:02}-{max_date[2]:02}")

    print("{}-{:02d}-{:02d}".format(max_year, max_month, max_day))
    print("{}-{:02d}-{:02d}".format(max_date[0], max_date[1], max_date[2]))
    print("{}-{:02d}-{:02d}".format(*max_date))


if __name__=="__main__":
    main()