import tkinter as tk

class ConvertTemp:
    def conv_c2f(self, temp_c):
        return temp_c * 1.8 + 32

    def conv_f2c(self, temp_f):
        return ( temp_f -32 ) /1.8


    def c2f(self):
        print("clicked!!!!")
        temp_c = float(self.ent_temp_c.get())
        temp_f = self.conv_c2f(temp_c)

        self.lbl_result_c2f.config(text=f"{temp_f:.1f}")

    def f2c(self):
        print("clicked!!!!")
        temp_ff = float(self.ent_temp_f.get())
        temp_cc = self.conv_f2c(temp_ff)

        self.lbl_result_f2c.config(text=f"{temp_cc:.1f}")








    def main(self):
        self.window = tk.Tk()

        self.window.title("온도 변환 프로그램 by 희원")
        # 프레임 잡기
        # c2f
        self.ent_frame = tk.Frame(master=self.window)
        self.ent_temp_c = tk.Entry(master=self.ent_frame, width=10)
        self.lbl_temp_f_1 = tk.Label(master=self.ent_frame, text="\N{DEGREE FAHRENHEIT}")
        self.lbl_temp_c_1 = tk.Label(master=self.ent_frame, text="\N{DEGREE CELSIUS}")
        self.btn_temp_c = tk.Button(
            master=self.ent_frame,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=self.c2f
        )
        self.lbl_result_c2f = tk.Label(master=self.ent_frame, text="")

        # f2c
        self.ent_temp_f = tk.Entry(master=self.ent_frame, width=10)
        self.lbl_temp_f_2 = tk.Label(master=self.ent_frame, text="\N{DEGREE FAHRENHEIT}")
        self.lbl_temp_c_2 = tk.Label(master=self.ent_frame, text="\N{DEGREE CELSIUS}")

        self.btn_temp_f = tk.Button(
            master=self.ent_frame,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=self.f2c
        )
        self.lbl_result_f2c = tk.Label(master=self.ent_frame, text="")

        # 배치하기
        #  c2f
        self.ent_frame.grid(row=0, column=0, sticky="e")
        self.ent_temp_c.grid(row=0, column=0, padx=10, pady=10)
        self.lbl_temp_c_1.grid(row=0, column=1, padx=10, pady=10)
        self.btn_temp_c.grid(row=0, column=2, padx=10, pady=10)
        self.lbl_result_c2f.grid(row=0, column=3, padx=10, pady=10)
        self.lbl_temp_f_1.grid(row=0, column=4, padx=10, pady=10)

        # f2c
        self.ent_temp_f.grid(row=1, column=0, padx=10, pady=10)
        self.lbl_temp_f_2.grid(row=1, column=1, padx=10, pady=10)
        self.btn_temp_f.grid(row=1, column=2, padx=10, pady=10)
        self.lbl_result_f2c.grid(row=1, column=3, padx=10, pady=10)
        self.lbl_temp_c_2.grid(row=1, column=4, padx=10, pady=10)
        self.window.mainloop()


if __name__=="__main__":
    app = ConvertTemp()
    app.main()