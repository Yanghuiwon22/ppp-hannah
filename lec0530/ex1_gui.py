import tkinter as tk

def main():
    # 첫글자가 대문자면 class (주로 함수이름은 소문자로 시작)
    window = tk.Tk()
    # greeting = tk.Label("Hello, Tkinter")
    greeting = tk.Label(text = "Hello, Tkinter", fg="white", bg="black")

    greeting.pack()
    window.mainloop()


if __name__=="__main__":
    main()

