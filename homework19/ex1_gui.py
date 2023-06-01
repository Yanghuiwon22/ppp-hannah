import tkinter as tk


def main():
    window = tk.Tk()
    greeting = tk.Label(text="Hello, World!",
                        foreground="red",  # Set the text color to white
                        background="black"  # Set the background color to black
                        )
    greeting.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
