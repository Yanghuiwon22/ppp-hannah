import tkinter as tk
window = tk.Tk()
window.withdraw()

# 생성할 window창의 크기 및 초기 위치 성정 매더드
window_width = 400
window_height = 200
window_pos_x = 700
window_pos_y = 100

window.geometry(f"{window_width}x{window_height}+{window_pos_x}+{window_pos_y}")


window.resizable(False, False)

window.title("Tkinter: Button test by Rosmary")

# window.iconphoto(False, )


button_1 = tk.Button(window, text="테스트버튼")
button_2 = tk.Button(window, text="창 닫기 버튼")

button_1.pack()
button_2.pack()

window.mainloop()