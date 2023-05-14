import time
import winsound

from lec0511.gui_input import gui_input


def main():
    timer_set = int(gui_input("카운트다운 할 시간을 쓰시오"))
    # timer_set = 3

    print("start")
    i=0
    while True:
        time.sleep(1)
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 300  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print (timer_set - i)
        i += 1

        if i == timer_set:
            frequency = 2150  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            break

    print("hello")
    frequency = 2150  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

if __name__=="__main__":
    main()