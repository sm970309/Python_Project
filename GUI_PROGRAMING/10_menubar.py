from tkinter import *

root = Tk()
root.title("GUI 프로그래밍")
root.geometry("640x480+300+100")       # 가로x세로 가로간격+세로간격

def create_new_file():
    print("새 파일 만들기")

menu = Menu(root)

menu_file = Menu(menu,tearoff = 0)
# 메뉴 값 추가
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window")
# 구분자
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
# 선택 불가능
menu_file.add_command(label="Save All",state = "disable")
# 종료 명령
menu_file.add_command(label="Exit",command=root.quit)

# 위의 menu_file의 값을 menu에 추가
menu.add_cascade(label="File",menu = menu_file)

# Edit 메뉴(빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가(radio)
menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

# View 메뉴 추가(chkbox)
menu_view = Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View",menu=menu_view)

root.config(menu = menu)
root.mainloop()