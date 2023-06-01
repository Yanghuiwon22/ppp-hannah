import tkinter as tk
import random

class Lotto:
    def get_lotto(self):
        lotto_numbers = []
        while len(lotto_numbers) < 6:
            lotto_num = random.randint(1, 45)
            if not lotto_num in lotto_numbers:
                lotto_numbers.append(lotto_num)
        return sorted(lotto_numbers)





    def main(self):
        num = int(input("몇 번 추출할까요?"))
        result = []
        for i in range(num):
            lotto_number = self.get_lotto
            result.append(lotto_number)

        self.window = tk.Tk()

        self.ent_frame = tk.Frame(master=self.window)

        self.ent_temp = tk.Entry(master=self.ent_frame, width=10)
        self.lbl_temp_c = tk.Label(master=self.ent_frame, text="\N{DEGREE CELSIUS}")
        self.btn_temp = tk.Button(master=self.ent_frame,
                                  text="\N{RIGHTWARDS BLACK ARROW}",
                                  command=self.get_lotto
                                  )
        self.lbl_result = tk.Label(master=self.ent_frame, text="!!!")

        self.window.title("로또번호 추출 프로그램 v.0.1 by 홍길동")
        self.window.resizable(width=False, height=False)
        self.window.geometry("500x300")

        self.ent_temp.grid(row=0, column=0, sticky="e")
        self.lbl_temp_c.grid(row=0, column=1)
        self.btn_temp.grid(row=0, column=2)
        self.lbl_result.grid(row=0, column=3)

        self.ent_frame.grid(row=0, column=0, padx=10, pady=10)

        self.window.mainloop()






if __name__=="__main__":
    app = Lotto()
    app.main()