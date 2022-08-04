#from tkinter import *
#from tkinter import messagebox
#
#window=Tk()
#window.title("GUI Python")
#window.resizable(0,0)
#window.geometry('300x500')
#MyVar=StringVar()
#def compute():
#    val=MyVar.get()
#    k=int(val)
#    f=k*(9/5)+32
#    messagebox.showinfo('msg title','Farheinheit Value: '+str(f))
#
#l1=Label(text='Enter celcius value: ',font=100)
#e1=Entry(text='Your input here',textvariable=MyVar,font=100)
#btn=Button(text='Convert',font=100,command=compute)
#l1.grid(column=1,row=0)
#e1.grid(column=2,row=0)
#btn.grid(row=1,column=1)
#window.mainloop()
from tkinter import *
from tkinter import messagebox

from numpy import size

window=Tk()
window.geometry('300x200')
window.title("GUI Programt to convert Celcius to fahreinheit")
MyVar=StringVar()
def compute():
    val=MyVar.get()
    k=int(val)
    f=k*(9/5)+32
    messagebox.showinfo("Result",f"Converted Fahreinheit Value: {f}")

l1=Label(text="Enter your Celcius value: ",font=100)
btn=Button(text="Convert",command=compute,font=100)
e1=Entry(textvariable=MyVar,font=100)
l1.grid(column=1,row=0)
e1.grid(column=2,row=0)
btn.grid(row=1,column=1)
window.mainloop()
