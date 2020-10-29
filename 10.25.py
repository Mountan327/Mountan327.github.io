
from tkinter import *
 
def cross(value):
    text.insert(INSERT,'x')
window =Tk()
frame =Frame(window)
frame.pack()
 
text =Text(frame,height =3,width =10)
text.pack()
 
button=Button(frame,text="add",command = lambda:cross(text))
button.pack()
 
window.mainloop()