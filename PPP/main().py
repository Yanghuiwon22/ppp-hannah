import tkinter as tk

win









window = tk.Tk()

ent_frame = tk.Frame(master=window)

ent_temp = tk.Entry(master=ent_frame, width=10)
lbl_temp_c = tk.Label(master=ent_frame, text="\N{DEGREE CELSIUS}")
btn_temp = tk.Button(master=ent_frame,
                     text="\N{RIGHTWARDS BLACK ARROW}",
                     command=c2f
                     )
lbl_result = tk.Label(master=ent_frame, text="!!!")


def main():

    window.title("온도 변환 프로그램 v.0.1 by 홍길동")
    window.resizable(width=False, height=False)
    window.geometry("500x300")


    ent_temp.grid(row=0, column=0, sticky="e")
    lbl_temp_c.grid(row=0, column=1)
    btn_temp.grid(row=0, column=2)
    lbl_result.grid(row=0, column=3)

    ent_frame.grid(row=0, column=0, padx=10, pady=10)



    window.mainloop()

if __name__=="__main__":
    main()

