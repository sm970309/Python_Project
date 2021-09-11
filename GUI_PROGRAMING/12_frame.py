from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

Label(root,text="메뉴를 선택해 주세요").pack(side="top")
Button(root,text="주문하기").pack(side="bottom")

frame1 = Frame(root, relief ="solid", bd = 1)
frame1.pack(side="left",fill="both",expand=True)

Button(frame1, text="1번").pack()
Button(frame1, text="2번").pack()
Button(frame1, text="3번").pack()

frame2 = LabelFrame(root,text = "음료",relief="solid",bd = 1)
frame2.pack(side="right",fill="both",expand=True)

Button(frame2,text="4번").pack()
Button(frame2,text="5번").pack()

root.mainloop()