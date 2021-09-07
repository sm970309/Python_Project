from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

# txt박스 생성
txt = Text(root,width=30,height =1)
txt.pack()

# txt박스 안에 미리 값 집어넣기
txt.insert(END,"글자를 입력하세요")

# 한줄로 받을 때 -> entry 사용
e = Entry(root,width=30)
e.pack()
e.insert(0,"한 줄만 입력")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END))   #1 : 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text= "Click",command=btncmd)
btn.pack()

root.mainloop()