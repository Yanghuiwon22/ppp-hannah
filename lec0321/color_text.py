def colored(r,g,b, text):
    return"\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b,
text)

def text_red(text):
    return colored(255, 0, 0, text)

print(colored(255,0,0, "hello"))
print(text_red("hello World"))