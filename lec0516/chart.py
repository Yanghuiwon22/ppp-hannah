import matplotlib
import matplotlib.pyplot as plt
print(matplotlib.get_cachedir())
import numpy as np



def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    tmax = np.random.rand(30) * 15 + 15
    tmin = tmax - (np.random.rand(30) * 5 + 5)
    highlight = [None, None, None, 17]
    plt.plot(tmax, color="r", label="최고기온")
    plt.plot(tmin, color="b", label="최저기온")
    plt.plot(highlight, color="r", label="마킹", marker="o")
    plt.axhline(y=22, color = "r", linestyle = "--")



    plt.ylabel("기온(℃)")
    plt.legend()
    plt.show()
    # plt.savefig("./line_temp.png")

if __name__=="__main__":
    main()