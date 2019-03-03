
import os
import re
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilenames
from tkinter import ttk
import rawpy
import imageio


def converter(img,targetdirect,i,num):
    t.insert('end', '第' + str(i) + '/' + num + '件' + img + '  Converting \n')
    print(img,targetdirect)
    if os.path.exists(targetdirect)==True:
        pass
    else:
        try:
            raw=rawpy.imread(img)
            raw_post = raw.postprocess()
        except:
            pass
        else:
            imageio.imsave(targetdirect, raw_post)
    t.insert('end', '第' + str(i) + '/' + num + '件' + img + '  Finish \n')


#GUI


# 主程序

# acquire source imgs from source path
def massconvert():
    print(imgs, targetpath, targettype)
    num = str(len(imgs))
    i = 1
    for img in imgs:

        img_name = os.path.basename(img)
        sourcetype=str(re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', img_name)[0])
        print(sourcetype)

        targetdirect = targetpath + '/' +re.sub(sourcetype,'.'+targettype,img_name)
        converter(img, targetdirect,i,num)

        i = i + 1
    t.insert('end', '全部完成')


def gotarget(*args):  # 处理事件，*args表示可变参数
    global targettype
    targettype=targetformatlist.get()
    print(targetformatlist.get())
    # print# 打印选中的值]

def selectsourceimgs():  #获取源文件夹
    global imgs
    imgs=askopenfilenames()
    e1.insert(0,imgs)
    print(sourcepath)


def selecttargetPath():  #设定目标文件夹
    global targetpath
    targetpath = askdirectory()
    e2.insert(0,targetpath)
    print(targetpath)



window = Tk()
window.title('Image Converter')
window.geometry('400x400')
var2 = StringVar()
var3=StringVar()
var2.set(('NEF','jpg','png','tiff','bmp','GIF')) #为变量设置值
var3.set(('NEF','jpg','png','tiff','bmp','GIF')) #为变量设置值
#select path
Label(window,text = "源图片:").grid(row = 0, column = 1)
sourcepath=StringVar()
e1=Entry(window, textvariable = sourcepath)
e1.grid(row = 0, column = 2)
Button(window, text = "选择文件", command = selectsourceimgs).grid(row = 0, column = 3)

Label(window,text = "目标路径:").grid(row = 1, column = 1)
targetpath=StringVar()
e2=Entry(window, textvariable = targetpath)
e2.grid(row = 1, column = 2)

Button(window, text = "选择路径", command = selecttargetPath).grid(row = 1, column = 3)


#targetformatlist
Label(window,text = "目标图片类型:").grid(row = 3, column = 1)
targetformatlist = ttk.Combobox(window, textvariable=var3)  # 初始化
targetformatlist.bind("<<ComboboxSelected>>", gotarget)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
targetformatlist['values'] = ('NEF','jpg','png','tiff','bmp','GIF')    # 设置下拉列表的值
targetformatlist.grid(column=2, row=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
targetformatlist.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值



#显示结果文本库
t=Text(window,height=10,width=30,background = 'grey')
t.grid(row=6,column=2)

#开始转换按钮
Button(window, text = "开始转换", command = massconvert).grid(row = 3, column = 3)



#显示主窗口
window.mainloop()


