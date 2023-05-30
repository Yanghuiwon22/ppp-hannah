import tkinter as tk





class ConvertTemp:
    def conv_c2f(self, temp_c):
        return temp_c * 1.8 + 32

    def c2f(self):
        print("clicked!!!!")
    #     섭씨를 화씨로
    # 입력값은?
        temp_c = float(self.ent_temp.get())
        temp_f = self.conv_c2f(temp_c)
        print(temp_f)
    #     결과는 어디에?
        self.lbl_result.config(text=f"{temp_f:.1f}")

    window = tk.Tk()

    ent_frame = tk.Frame(master=self.window)
    ent_temp = tk.Entry(master=ent_frame, width=10)
    lbl_temp_c = tk.Label(text="\N{DEGREE FAHRENHEIT}")
    btn_temp = tk.Button(
        master=ent_frame,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=c2f
    )
    lbl_result = tk.Label(master=ent_frame, text="!!!")


    def main(self):

        self.window.title("온도 변환 프로그램 by 희원")
        self.window.resizable(width=False, height=False)
        self.window.geometry("500x300")



        self.ent_temp.grid(row=0, column=0, sticky="e")
        self.lbl_temp_c.grid(row=0, column=1)
        self.btn_temp.grid(row=0, column=2)
        self.lbl_result.grid(row=0, column=3)


        self.ent_frame.grid(row=0, column=0, padx=10, pady=10)

        self.window.mainloop()


if __name__=="__main__":
    app = ConvertTemp()
    app.main()