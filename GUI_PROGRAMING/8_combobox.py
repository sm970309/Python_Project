from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

values = [str(i) +"일" for i in range(1,32)]

combobox = ttk.Combobox(root,height = 5,values = values,state="readonly")
combobox.pack()

# 메세지 직접 넣기
combobox.set("카드 결제일")
# 0번째 값 넣기
combobox.current(0)


def btncmd():
    print(combobox.get())
btn = Button(root,text="선택",command = btncmd)
btn.pack()
root.mainloop()