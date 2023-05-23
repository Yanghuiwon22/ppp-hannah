import pandas as pd

def main():
    filename = "./history_jeonju.csv"
    df = pd.read_csv(filename, encoding="euc-kr", skiprows=7)
    print(df)

if __name__=="__main__":
    main()