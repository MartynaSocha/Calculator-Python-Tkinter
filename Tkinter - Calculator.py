from tkinter import *

root = Tk()     #create a window
root.title("Simple Calculator")

e=Entry(root, width=35, borderwidth=5)     #create an input
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)        #position for input

def button_add(number):
    current = e.get()   #var that gets an input value and save as a current
    e.delete(0,END)     #clear var current to not double it
    e.insert(0,str(current) + str(number))  #add a number to input,

def button_to_clear():
    e.delete(0,END)

def button_sum():
    first_number = e.get()  #get the first number from input
    global f_num            #create a global var - we can use it everywhere
    global math
    math="addition"
    f_num = int(first_number)   #assign value from input as a intiger
    e.delete(0,END)

def button_equal():
    second_number =e.get() #get the second number from input
    e.delete(0,END)

    if math =="addition":
        e.insert(0,f_num + int(second_number))    #add this two numbers
    if math == "substract":
        e.insert(0, f_num - int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math="substract"
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiply"
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "divide"
    e.delete(0, END)

#create a buttons with function
#function for button are without argument, but we can use lambda if we want to have parameters
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_add(1))
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_add(2))
button_3 = Button(root,text='3',padx=38,pady=20,command=lambda: button_add(3))
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_add(4))
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_add(5))
button_6 = Button(root,text='6',padx=38,pady=20,command=lambda: button_add(6))
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_add(7))
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_add(8))
button_9 = Button(root,text='9',padx=38,pady=20,command=lambda: button_add(9))
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_add(0))
button_plus= Button(root,text='+',padx=39,pady=20,command=lambda: button_sum())
button_equal = Button(root,text='=',padx=85,pady=20,command= button_equal)
button_clear=Button(root,text='Clear',padx=75,pady=20,command= button_to_clear)
button_subtract= Button(root,text='-',padx=40.5,pady=20,command= button_subtract)
button_multiply= Button(root,text='*',padx=39,pady=20,command= button_multiply)
button_divide= Button(root,text='/',padx=39,pady=20,command=button_divide)

#put the buttons on the screen

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()




