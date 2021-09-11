from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "매진 되었습니다.")

def error():
    msgbox.showerror("에러", "에러가 발생되었습니다.")
def okcancel():
    msgbox.askokcancel("확인/취소", "계속 하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("일시적인 오류", "에러가 발생되었습니다. 계속 하시겠습니까?")
def yesnocancel():
    response = msgbox.askyesnocancel(NONE, "저장하시겠습니까?")
    print(response)

Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()
Button(root,command=okcancel,text="확인/취소").pack()
Button(root,command=retrycancel,text="계속/취소").pack()
Button(root,command=yesnocancel,text="예/아니오/취소").pack()

root.mainloop()