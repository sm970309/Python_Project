from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

progressbar = ttk.Progressbar(root,maximum=100,mode = "indeterminate")  # 언제 끝날지 모를때 주로 사용
progressbar.start(10)   # 10ms 마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root,maximum=100,mode = "determinate")  # default
progressbar2.start(10)   # 10ms 마다 움직임
progressbar2.pack()

p_var2 = DoubleVar()
progressbar3 = ttk.Progressbar(root,maximum=100,length = 150, variable=p_var2)  # default
progressbar3.pack()


def btncmd():
    progressbar.destroy()
    progressbar2.destroy()

def btncmd2():
    if p_var2.get() != 100:

        for i in range(101):
            time.sleep(0.01)

            p_var2.set(i)
            progressbar3.update()   # ui 업데이트

btn = Button(root,text="중지",command = btncmd)
btn2 = Button(root,text="시작",command = btncmd2)
btn.pack()
btn2.pack()
root.mainloop()