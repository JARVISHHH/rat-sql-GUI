#! /usr/bin/env python
# -*- python -*-

import sys

py2 = py30 = py31 = False
version = sys.hexversion
if version >= 0x020600F0 and version < 0x03000000 :
    py2 = True    # Python 2.6 or 2.7
    from Tkinter import *
    import ttk
elif version >= 0x03000000 and version < 0x03010000 :
    py30 = True
    from tkinter import *
    import ttk
elif version >= 0x03010000:
    py31 = True
    from tkinter import *
    import tkinter.ttk as ttk
else:
    print ("""
    You do not have a version of python supporting ttk widgets..
    You need a version >= 2.6 to execute PAGE modules.
    """)
    sys.exit()



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()  # tk顶级控件（主窗口）
    root.title('text_to_sql')
    root.geometry('1138x822+861+548')
    w = text_to_sql (root)
    init()
    # 进入消息循环
    root.mainloop()

w = None
def create_text_to_sql (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    # 新建一个对话框
    w = Toplevel (root)
    w.title('text_to_sql')
    w.geometry('1138x822+861+548')
    w_win = text_to_sql (w)
    init()
    return w_win

def destroy_text_to_sql ():
    global w
    w.destroy()
    w = None


def init():
    pass


class text_to_sql:
    def __init__(self, master=None):
        # Set background of toplevel window to match
        # current style
        style = ttk.Style()
        theme = style.theme_use()
        default = style.lookup(theme, 'background')
        master.configure(background=default)

        # text
        self.Text1 = Text (master)
        self.Text1.place(relx=0.37,rely=0.19,relheight=0.08,relwidth=0.25)
        self.Text1.configure(background="white")
        self.Text1.configure(wrap="none")

        # text
        self.Text2 = Text (master)
        self.Text2.place(relx=0.37,rely=0.34,relheight=0.33,relwidth=0.25)
        self.Text2.configure(background="white")
        self.Text2.configure(wrap="none")

        # button
        self.TButton1 = ttk.Button (master, command = self.get_question_give_answer)  # command设置动作
        self.TButton1.place(relx=0.42,rely=0.73,height=41,width=164)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''转换''')

        # label
        self.TLabel1 = ttk.Label (master)
        self.TLabel1.place(relx=0.25,rely=0.21,height=35,width=48)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''text''')

        # label
        self.TLabel2 = ttk.Label (master)
        self.TLabel2.place(relx=0.25,rely=0.35,height=35,width=84)
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''sql语句''')
    
    def get_question_give_answer(self):
        # 清除输出框的内容
        self.Text2.delete('0.0','end')
        # 获得输入框的内容
        question = self.Text1.get('0.0', 'end')[0:-1]

        ### begin code
        # result = 
        result = 'hhh'
        ### end code

        self.Text2.insert('0.0', result)


if __name__ == '__main__':
    vp_start_gui()