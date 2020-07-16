from tkinter import *

gui = Tk()
gui.title("Calculator")

#gui.geometry("600x400")
#gui.configure(bg='blue')

e=Entry(gui,width=40,borderwidth=2)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

def button_click(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))
    
def button_sub():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))

def button_mul():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))

def button_div():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num + int(second_number))





#Button

button_1 = Button(gui, text='1', padx=40,pady=20, command=lambda : button_click(1),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_2 = Button(gui, text='2', padx=40,pady=20, command=lambda: button_click(2),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_3 = Button(gui, text='3', padx=40,pady=20, command=lambda: button_click(3),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_plus = Button(gui, text='+', padx=40,pady=20, command=button_add,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')

button_4 = Button(gui, text='4', padx=40,pady=20, command=lambda: button_click(4),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_5 = Button(gui, text='5', padx=40,pady=20, command=lambda: button_click(5),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_6 = Button(gui, text='6', padx=40,pady=20, command=lambda: button_click(6),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_sub = Button(gui, text='-', padx=40,pady=20, command=button_sub,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')

button_7 = Button(gui, text='7', padx=40,pady=20, command=lambda: button_click(7),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_8 = Button(gui, text='8', padx=40,pady=20, command=lambda: button_click(8),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_9 = Button(gui, text='9', padx=40,pady=20, command=lambda: button_click(9),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_multi = Button(gui, text='*', padx=40,pady=20, command=button_multi,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')

button_divi = Button(gui, text='/', padx=40,pady=20, command= button_div,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_0 = Button(gui, text='0', padx=40,pady=20, command=lambda: button_click(0),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_dot = Button(gui, text='.', padx=40,pady=20, command=lambda: button_click(),bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_equal = Button(gui, text='=', padx=40,pady=20, command=button_equal,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')
button_clear = Button(gui, text='Clear', padx=175,pady=20, command=button_clear,bg='#000000', fg='#ffffff', activebackground='#595454', activeforeground='#5e5e56')


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