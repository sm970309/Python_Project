from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("IMAGE COMBINE PROGRAM")

def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",filetypes=(("PNG","*.png"),("모든 파일","*.*")),\
                                   initialdir=r"C:\Users\sm970\Git_Project\Python_Project\GUI_PROJECT_IMAGE")
    for file in files:
        list_file.insert(END,file)

def del_file():
    for idx in reversed(list_file.curselection()):  #reversed => 반대로 출력
        list_file.delete(idx)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected =='':
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(END,folder_selected)

def merge_image():
    # PIL에 Image 사용

    """
    # size -> size[0] : width , size[1] : height
    width = max([x.size[0] for x in images])
    height = sum([x.size[1] for x in images])
    """
    try:
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)

        img_space = cmb_space.get()
        if img_space=="좁게":
            img_space = 30
        elif img_space=="보통":
            img_space=60
        elif img_space =="넓게":
            img_space=90
        else:
            img_space=0

        img_format = cmb_format.get().lower()
        images = [Image.open(x) for x in list_file.get(0,END)]

        # 이미지의 사이즈를 튜플 형태로 저장하기 위한 리스트
        image_sizes = []

        if img_width>-1:
            image_sizes = [(img_width,int(img_width*x.size[1]/x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images]

        width,height = zip(*(image_sizes))
        width,height = max(width),sum(height)

        # 합치고자 하는 이미지의 총 크기
        if img_space>0:
            height += img_space*(len(images)-1)

        result_img = Image.new("RGB",(width,height),(255,255,255))
        y_offset = 0     # y의 기준 값
        for idx,img in enumerate(images):
            if img_width>-1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img,(0,y_offset))
            y_offset += img.size[1] + img_space

            progress = (idx+1) / len(images) * 100  # 작업 진행의 퍼센트
            p_var.set(progress)
            progress_bar.update()

        dest_path = os.path.join(txt_dest_path.get(),"merge_photo."+img_format)
        result_img.save(dest_path)
        msgbox.showinfo(None,"작업이 완료되었습니다.")

    except Exception as err:
        msgbox.showerror("에러",err)
def start():
    if list_file.size() == 0:
        msgbox.showwarning(None,"이미지 파일을 추가하세요")
        return
    if len(txt_dest_path.get())==0:
        msgbox.showwarning(None, "저장 경로를 추가하세요")
    else:
        merge_image()

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

btn_dest_path = Button(path_frame,text="찾아보기",width=10,command = browse_dest_path)
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
lbl_format = Label(option_frame,text="포맷",width=8)
lbl_format.pack(padx = 5,pady=5,side = "left")

opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(option_frame,state="readonly",values=opt_format,width = 10)
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

btn_start = Button(frame_run,padx=5,pady=5,text="시작",width=12,command = start)
btn_start.pack(padx = 5,pady=5,side = "right")

root.resizable(False,False)
root.mainloop()