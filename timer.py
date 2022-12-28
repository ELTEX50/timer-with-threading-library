import time
from tkinter import *
from threading import *

root=Tk()
def start1():
    number= e1.get()
    number = int(number)
    t=Thread(target=counter1,args=(number,))
    t.start()

def start2():
    number = e2.get()
    number = int(number)
    t = Thread(target=counter2, args=(number,))
    t.start()

def counter1(number):
    for x in range(number,-1,-1):
        lbl2.set(x)
        root.update()
        time.sleep(1)

def counter2(number):
    for x in range(number,-1,-1):
        lbl1.set(x)
        root.update()
        time.sleep(1)

lbl1=StringVar()
lbl2=StringVar()
l1=Label(root,textvariable=lbl1,bg="yellow")
l1.grid(row=0,column=1)

l2=Label(root,textvariable=lbl2,bg="yellow")
l2.grid(row=0,column=0)

e1=Entry(root)
e1.grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

b1=Button(root,text="start",bg="light blue",command=start1)
b1.grid(row=2,column=0,columnspan=1,sticky="nsew")

b2=Button(root,text="start",bg="light blue",command=start2)
b2.grid(row=2,column=1,columnspan=2,sticky="nsew")

b3=Button(root,text="cancel",bg="red",command=quit)
b3.grid(row=3,column=0,columnspan=2, sticky="nswe")

root.config(bg="light blue")

root=mainloop()