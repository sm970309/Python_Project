from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

# 레이블 추가
label1 = Label(root,text = "HI")
label1.pack()
# 레이블 사진 추가
photo = PhotoImage(file="image.png")
label2 = Label(root,image=photo)
label2.pack()

# 버튼 동작 바꾸기
def change():
    label1.config(text="Bye")

btn = Button(root,text="클릭",command = change)
btn.pack()

root.mainloop()