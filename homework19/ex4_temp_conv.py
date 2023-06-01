import tkinter as tk

from hw15.danuni29.caesar_ciphere_hw15 import caesar_encode, caesar_decode


def conv_c2f(temp_c):
    return temp_c * 1.8 + 32


def encode():
    print("clicked!!")
    # 섭씨를 화씨로...
    # 섭씨는...? 입력값은 어디??
    # giu_input() 비슷
    raw_text = ent_temp.get()
    encoded_text = "".join(caesar_encode(raw_text))
    print(encoded_text)
    # 결과는 어디다가 표시??
    lbl_result.config(text=encoded_text)


def decode():
    raw_text = ent_temp.get()
    decoded_text = "".join(caesar_decode(raw_text))
    print(decoded_text)
    # 결과는 어디다가 표시??
    lbl_result.config(text=decoded_text)


window = tk.Tk()

ent_frame = tk.Frame(master=window)

ent_temp = tk.Entry(master=ent_frame, width=10)
lbl_temp_c = tk.Label(master=ent_frame, text="\N{DEGREE CELSIUS}")
btn_temp = tk.Button(master=ent_frame,
                     text="암호화",
                     command=encode
                     )
btn_decode = tk.Button(master=ent_frame,
                     text="복호화",
                     command=decode
                     )
lbl_result = tk.Label(master=ent_frame, text="!!!")


def main():

    window.title("온도 변환 프로그램 v.0.1 by 홍길동")
    window.resizable(width=False, height=False)
    window.geometry("500x300")


    ent_temp.grid(row=0, column=0, sticky="e")
    lbl_temp_c.grid(row=0, column=1)
    btn_temp.grid(row=0, column=2)
    btn_decode.grid(row=1, column=2)

    lbl_result.grid(row=0, column=3)

    ent_frame.grid(row=0, column=0, padx=10, pady=10)



    window.mainloop()


if __name__ == "__main__":
    main()
