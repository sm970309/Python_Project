from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import filedialog

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

def open_file():
    if txt is not None:
        response = msgbox.askokcancel("파일 열기", "파일을 열면 현재 작성중인 문서가 지워집니다.\n계속 하시겠습니까?")

    if response:
        txt.delete("1.0", END)
        files = filedialog.askopenfile(title="파일을 선택하세요", filetypes=(("txt", "*.txt"), ("모든 파일", "*.*")),\
                                       initialdir=r"C:\Users\sm970\Git_Project\Python_Project\GUI_PROGRAMING")
        lines = files.readlines()
        for line in lines:
            txt.insert(END, line)

def save_file():
    f = open("mynote.txt",'w')
    response = msgbox.askyesnocancel("저장", "저장하시겠습니까?")
    if response:
        f.write(txt.get("1.0",END))
    f.close()

def quit_file():
    response = msgbox.askyesno("종료", "종료하시겠습니까?")
    if response:
        root.quit()

# 메뉴 부분
menu = Menu(root)

# 파일
menu_file = Menu(menu,tearoff = 0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_command(label="종료",command=quit_file)
menu.add_cascade(label="파일",menu = menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)

# 스크롤바 부분
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

# 텍스트 부분
txt = Text(root,yscrollcommand = scrollbar.set)
txt.pack(side="left",fill="both",expand = True)

# 텍스트 부분과 스크롤 바 매핑
scrollbar.config(command=txt.yview)

root.mainloop()