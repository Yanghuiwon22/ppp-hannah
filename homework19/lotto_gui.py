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

    def how_times(self):
        num = self.times
        result = []
        for i in range(num):
            lotto_number = self.get_lotto
            result.append(lotto_number)

    def main(self):

        self.window = tk.Tk()

        self.window.title("로또번호 추출 프로그램 v.0.1 by 홍길동")
        self.window.resizable(width=False, height=False)
        self.window.geometry("500x300")

        self.ent_frame_1 = tk.Frame(master=self.window)

        self.ent_times = tk.Entry(master=self.ent_frame_1, width=10)
        self.text_times = tk.Label(master=self.ent_frame_1, text="번")
        self.btn_times = tk.Button(master=self.ent_frame_1,
                                   text="\N{RIGHTWARDS BLACK ARROW}",
                                   command=self.get_lotto
                                   )

        self.ent_frame_1.grid(row=0, column=0, sticky="e")
        self.ent_times.grid(row=0, column=0, sticky="e")






        self.window.mainloop()





if __name__=="__main__":
    app = Lotto()
    app.main()