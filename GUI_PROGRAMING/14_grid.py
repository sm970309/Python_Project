from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

btn1 = Button(root,text="%",padx=10,pady=10)
btn2 = Button(root,text="CE",padx=10,pady=10)
btn3 = Button(root,text="C",padx=10,pady=10)

# N E W S 는 상하좌우로 늘리기
btn1.grid(row=0,column=0,sticky = N+E+W+S)
btn2.grid(row=0,column=1,sticky = N+E+W+S)
btn3.grid(row=0,column=2,sticky = N+E+W+S)

btn4 = Button(root,text="4",padx=10,pady=10)
btn5 = Button(root,text="5",padx=10,pady=10)
btn6 = Button(root,text="6",padx=10,pady=10)

btn4.grid(row=1,column=0,sticky = N+E+W+S)
btn5.grid(row=1,column=1,sticky = N+E+W+S)
btn6.grid(row=1,column=2,sticky = N+E+W+S)

root.mainloop()