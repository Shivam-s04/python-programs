from tkinter import*
from tkinter.ttk import *
root = Tk()
root.title("Canvas Example")
c= Canvas(root,width = 200,height = 200)
c.pack(fill=BOTH)
c.create_oval(100,100,80,80,outline = 'black',fill='red',width = 2)
c.create_rectangle(10,10,90,90,outline = 'black',fill = 'blue',width = 2)
root.mainloop()
