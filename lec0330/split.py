
def main():
    input_text = "5,10,3,4,7"
    print(input_text)
    tokens = input_text.split(",")
    numbers = []
    for token in tokens:
        numbers.append(int(token))
    numbers = [int(x) for x in input_text.split(",")]


    return numbers

if __name__=="__main__":
    main()


