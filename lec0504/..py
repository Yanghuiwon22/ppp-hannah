import math
def str2float(text):
    try:
        result_value = float(text)
    except:
        result_value = None

    return result_value

def main():
    text = "2.5!"

    result_value = str2float(text)
    if result_value is not None:
        result_value *= 5




    print(f"{result_value:.1f}")


if __name__=="__main__":
    main()