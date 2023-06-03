import tkinter as tk
import random
from pprint import pprint


class ConvertTemp:
    def get_lotto(self):
        lotto_number = []
        while len(lotto_number) < 6:
            lotto_num = random.randint(1, 45)
            if not lotto_num in lotto_number:
                lotto_number.append(lotto_num)
        return lotto_number

    def final_lotto(self):
        num = self.ent_times.get()
        nums = int(num)
        result = []
        for i in range(nums):
            lotto_number = self.get_lotto()
            result.append(lotto_number)

        self.lbl_result.config(text=f"{result}")

    def main(self):
        self.window = tk.Tk()

        self.window.title("로또 번호 추출 프로그램 by 희원")
        # 프레임 잡기
        self.ent_frame = tk.Frame(master=self.window)
        self.ent_times = tk.Entry(master=self.ent_frame, width=10)
        self.lbl_times = tk.Label(master=self.ent_frame, text="번 추출")
        self.btn_temp_c = tk.Button(
            master=self.ent_frame,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=self.final_lotto
        )
        self.lbl_result = tk.Label(master=self.ent_frame, text="")


        # 배치하기
        self.ent_frame.grid(row=0, column=0, sticky="e")
        self.ent_times.grid(row=0, column=0, padx=10, pady=10)
        self.lbl_times.grid(row=0, column=1, padx=10, pady=10)
        self.btn_temp_c.grid(row=0, column=2, padx=10, pady=10)
        self.lbl_result.grid(row=0, column=3, padx=10, pady=10)

        self.window.mainloop()


if __name__=="__main__":
    app = ConvertTemp()
    app.main()