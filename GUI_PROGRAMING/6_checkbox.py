from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

chkvar = IntVar()   # 해당 변수에 int형으로 변수 저장
chkbox = Checkbutton(root,text = "오늘 하루 보지 않기",variable = chkvar)

# 체크 여부 (체크 안할때는 deselect)
chkbox.select()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root,text = "일주일동안 보지 않기",variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: 해제 1: 체크
    print(chkvar2.get())

btn = Button(root,text="클릭",command = btncmd)
btn.pack()
root.mainloop()