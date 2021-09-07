from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

# 버튼 추가하기
btn1 = Button(root,text="버튼 1")
btn1.pack()
# padx,pady 로 크기 설정
btn2 = Button(root,padx=5,pady=10,text="버튼 2는 padx,pady를 사용해서 크기가 늘어남")
btn2.pack()
btn3 = Button(root,padx=10,pady=5,text="버튼 3")
btn3.pack()
# width, height 로 크기 설정
btn4 = Button(root,width=10,height=3,text="버튼 4는 width heigth를 사용해서 크기 안늘어남")
btn4.pack()
# fg는 글자 색, bg는 배경 색
btn5 = Button(root,fg='red',bg='blue',text="버튼 5")
btn5.pack()

# 버튼에 이미지 생성
photo = PhotoImage(file="image.png")
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print("버튼 클릭됨")
btn7 = Button(root,text="동작",command=btncmd)
btn7.pack()

root.mainloop()