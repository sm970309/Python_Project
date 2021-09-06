from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

# 창 크기 변경 불가(가로,세로)
root.resizable(False,False)
root.mainloop()