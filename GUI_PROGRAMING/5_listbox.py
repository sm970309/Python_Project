from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

listbox = Listbox(root,selectmode = "extended",height=0)    # heigth가 0이면 목록 크기만큼
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
# END 사용하면 마지막에 추가
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    # listbox.delete(END)       #삭제
    # print(listbox.size())     #크기
    # print(listbox.get(0,2))   #항목

    # 선택된 항목 확인 -> 인덱스로 반환함
    print("선택된 항목:",listbox.curselection())

btn = Button(root,text="클릭",command = btncmd)
btn.pack()
root.mainloop()