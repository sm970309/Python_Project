from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
root = Tk()
root.title("IMAGE COMBINE PROGRAM")

def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",filetypes=(("PNG","*.png"),("모든 파일","*.*")),\
                                   initialdir="C:/")
    for file in files:
        list_file.insert(END,file)

def del_file():
    for idx in reversed(list_file.curselection()):  #reversed => 반대로 출력
        list_file.delete(idx)

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(padx = 5,pady=5,fill="x")

btn_add_file = Button(file_frame,padx=5,pady=5,width=12,text="파일추가",command = add_file)
btn_add_file.pack(side="left")
btn_delete_file = Button(file_frame,padx=5,pady=5,width=12,text="선택삭제",command = del_file)
btn_delete_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(padx = 5,pady=5,fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode = "extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(comman=list_file.yview())

# 저장 경로 프레임
path_frame = LabelFrame(root,text="저장경로")
path_frame.pack(padx = 5,pady=5,fill="x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand=True,padx = 5,pady=5,ipady = 4)

btn_dest_path = Button(path_frame,text="찾아보기",width=10)
btn_dest_path.pack(side="right")

# 옵션 프레임
option_frame = LabelFrame(root,text="옵션")
option_frame.pack(padx = 5,pady=5)

# 1. 가로 넓이 옵션
lbl_width = Label(option_frame,text="가로넓이",width=8)
lbl_width.pack(padx = 5,pady=5,side = "left")

opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(option_frame,state="readonly",values=opt_width,width = 10)
cmb_width.current(0)
cmb_width.pack(padx = 5,pady=5,side="left")

# 2. 간격 옵션
lbl_space = Label(option_frame,text="간격",width=8)
lbl_space.pack(padx = 5,pady=5,side = "left")

opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(option_frame,state="readonly",values=opt_space,width = 10)
cmb_space.current(0)
cmb_space.pack(padx = 5,pady=5,side="left")

# 3. 파일 포맷 옵션
lbl_format = Label(option_frame,text="간격",width=8)
lbl_format.pack(padx = 5,pady=5,side = "left")

opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(option_frame,state="readonly",values=opt_space,width = 10)
cmb_format.current(0)
cmb_format.pack(padx = 5,pady=5,side="left")

# 프로그레스바
frame_progress = LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x")

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress,maximum= 100,variable=p_var)
progress_bar.pack(padx = 5,pady=5,fill="x")

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(padx = 5,pady=5,fill="x")

btn_close = Button(frame_run,padx=5,pady=5,text="닫기",width=12,command = root.quit)
btn_close.pack(padx = 5,pady=5,side = "right")

btn_start = Button(frame_run,padx=5,pady=5,text="시작",width=12)
btn_start.pack(padx = 5,pady=5,side = "right")

root.resizable(False,False)
root.mainloop()