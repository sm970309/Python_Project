from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
# fill y는 y축으로 채운다는 뜻
scrollbar.pack(side="right",fill = "y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame,selectmode = "extended",height = 10,yscrollcommand = scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side = "left")

# 스크롤 바에서 리스트박스 매핑
scrollbar.config(command=listbox.yview)

root.mainloop()