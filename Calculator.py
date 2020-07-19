from tkinter import *

gui = Tk()
gui.title("Calculator")
gui.configure(bg='#9D9A9A')

e=Entry(gui,width=50,bd=5)
e.grid(row=0,column=0,columnspan=25,padx=10,pady=50)

def button_click(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num,operator
    operator="addition"
    f_num=int(first_number)
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_num,operator
    operator="subtraction"
    f_num=int(first_number)
    e.delete(0,END)
    
def button_mul():
    first_number=e.get()
    global f_num,operator
    operator="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num,operator
    operator="Division"
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if operator=="addition":
        e.insert(0,f_num + int(second_number))
    if operator=="subtraction":
        e.insert(0,f_num - int(second_number))
    if operator=="division":
        e.insert(0,f_num / int(second_number))
    if operator=="multiplication":
        e.insert(0,f_num * int(second_number))      



def entered(event):
    button_0.config(
        bg='#595454',
        fg='#ffffff'
    )

    button_1.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_2.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_3.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_4.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_5.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_6.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_7.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_8.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_9.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_plus.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_sub.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_divi.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_multi.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_dot.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_equal.config(
        bg='#595454',
        fg='#ffffff'
    )
def entered(event):
    button_clear.config(
        bg='#595454',
        fg='#ffffff'
    )
def left(event):
    button_0.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_1.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_2.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_3.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_4.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_5.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_6.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_7.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_8.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_9.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_plus.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_sub.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_divi.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_multi.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_dot.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_equal.config(
        bg='#000000',
        fg='#ffffff'
    )
def left(event):
    button_clear.config(
        bg='#000000',
        fg='#ffffff'
    )


#Button

button_1 = Button(gui, text='1', padx=38,pady=20, command=lambda : button_click(1),bg='#000000',fg='#ffffff' , activeforeground='#5e5e56')
button_2 = Button(gui, text='2', padx=40,pady=20, command=lambda: button_click(2),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_3 = Button(gui, text='3', padx=40,pady=20, command=lambda: button_click(3),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_plus = Button(gui, text='+', padx=40,pady=20, command=button_add,bg='#000000', fg='#ffffff', activeforeground='#5e5e56')

button_4 = Button(gui, text='4', padx=38,pady=20, command=lambda: button_click(4),bg='#000000', fg='#ffffff', activeforeground='#5e5e56')
button_5 = Button(gui, text='5', padx=40,pady=20, command=lambda: button_click(5),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_6 = Button(gui, text='6', padx=40,pady=20, command=lambda: button_click(6),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_sub = Button(gui, text='-', padx=40,pady=20, command=button_sub,bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')

button_7 = Button(gui, text='7', padx=38,pady=20, command=lambda: button_click(7),bg='#000000', fg='#ffffff', activeforeground='#5e5e56')
button_8 = Button(gui, text='8', padx=40,pady=20, command=lambda: button_click(8),bg='#000000', fg='#ffffff', activeforeground='#5e5e56')
button_9 = Button(gui, text='9', padx=40,pady=20, command=lambda: button_click(9),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_multi = Button(gui, text='*', padx=40,pady=20, command=button_mul,bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')

button_divi = Button(gui, text='/', padx=40,pady=20, command= button_div,bg='#000000', fg='#ffffff', activeforeground='#5e5e56')
button_0 = Button(gui, text='0', padx=40,pady=20, command=lambda: button_click(0),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_dot = Button(gui, text='.', padx=40,pady=20, command=lambda: button_click(),bg='#000000', fg='#ffffff',  activeforeground='#5e5e56')
button_equal = Button(gui, text='=', padx=40,pady=20, command=button_equal,bg='#000000', fg='#ffffff', activeforeground='#5e5e56')
button_clear = Button(gui, text='Clear', padx=175,pady=20, command=button_clear,bg='#000000', fg='#ffffff',activeforeground='#5e5e56')

button_0.bind('<Enter>',entered)
button_0.bind('<Leave>',left)
button_1.bind('<Enter>',entered)
button_1.bind('<Leave>',left)
button_2.bind('<Enter>',entered)
button_2.bind('<Leave>',left)
button_3.bind('<Enter>',entered)
button_3.bind('<Leave>',left)
button_4.bind('<Enter>',entered)
button_4.bind('<Leave>',left)
button_5.bind('<Enter>',entered)
button_5.bind('<Leave>',left)
button_6.bind('<Enter>',entered)
button_6.bind('<Leave>',left)
button_7.bind('<Enter>',entered)
button_7.bind('<Leave>',left)
button_8.bind('<Enter>',entered)
button_8.bind('<Leave>',left)
button_9.bind('<Enter>',entered)
button_9.bind('<Leave>',left)
button_plus.bind('<Enter>',entered)
button_plus.bind('<Leave>',left)
button_sub.bind('<Enter>',entered)
button_sub.bind('<Leave>',left)
button_multi.bind('<Enter>',entered)
button_multi.bind('<Leave>',left)
button_divi.bind('<Enter>',entered)
button_divi.bind('<Leave>',left)
button_dot.bind('<Enter>',entered)
button_dot.bind('<Leave>',left)
button_equal.bind('<Enter>',entered)
button_equal.bind('<Leave>',left)
button_clear.bind('<Enter>',entered)
button_clear.bind('<Leave>',left)

#On screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_plus.grid(row=3,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_multi.grid(row=1,column=3)

button_divi.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_dot.grid(row=4,column=2)
button_equal.grid(row=4,column=3)
button_clear.grid(row=5,column=0, columnspan=4)

gui.mainloop() 


#---------------------------------------------------------------------------------------------------------------------
#This work is Done by Nitin Mishra with  refrence of some website and is designed by me itself
# Thank you
# -------------------------------------------------------------------------------------------------------------------- 
