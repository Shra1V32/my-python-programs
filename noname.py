# Write a Python GUI program to create two buttons exit and hello using tkinter module.

from tkinter import *

window = Tk()
btn=Button(window,text="exit")
btn2=Button(window,text="Hello")

btn.place(x=75,y=62)
btn2.place(x=75,y=120)

window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()