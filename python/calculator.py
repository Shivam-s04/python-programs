from tkinter import *

expression = ''
def press(num):
    global expression
    expression = expression + str(num)
    exp.configure(text=expression)
    
def equalto():
    global expression
    try:
        result = eval(expression)
        exp.configure(text=result)
    except:
        exp.configure(text='Error')
        expression = ''



def clear():
    global expression
    expression = ''
    exp.configure(text='')



#the main window 
if __name__=='__main__':

    root = Tk()
    root.geometry('300x300')
    root.title('Calculator')

    equation = StringVar()
    exp = Label(root,text = equation,fg='white',bg='gray')
    exp.grid(row=0,column=0,columnspan=4)

    b1=Button(root,text = '1',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(1))
    b1.grid(row=1,column=0)
    b2=Button(root,text = '2',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(2))
    b2.grid(row=1,column=1)
    b3=Button(root,text = '3',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(3))
    b3.grid(row=1,column=2)
    b4=Button(root,text = '4',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(4))
    b4.grid(row=2,column=0)
    b5=Button(root,text = '5',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(5))
    b5.grid(row=2,column=1)
    b6=Button(root,text = '6',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(6))
    b6.grid(row=2,column=2)
    b7=Button(root,text = '7',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(7))
    b7.grid(row=3,column=0)
    b8=Button(root,text = '8',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(8))
    b8.grid(row=3,column=1)
    b9=Button(root,text = '9',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(9))
    b9.grid(row=3,column=2)
    b0=Button(root,text = '0',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press(0))
    b0.grid(row=4,column=0)
    dot=Button(root,text = '.',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press('.'))
    dot.grid(row=4,column=1)
    percent = Button(root,text = '%',fg='black',bg='light blue',padx = 5,pady=5,command = lambda: press('%'))
    percent.grid(row=4,column=2)
    plus=Button(root,text = '+',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press('+'))
    plus.grid(row=1,column=3)
    sub=Button(root,text = '-',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press('-'))
    sub.grid(row=2,column=3)
    mul=Button(root,text = '*',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press('*'))
    mul.grid(row=3,column=3)
    div=Button(root,text = '/',fg='black',bg='light blue',padx = 5,pady=5,command = lambda:press('/'))
    div.grid(row=4,column=3)
    clean= Button(root,text = 'clear',fg='black',bg='light blue',padx = 5,pady=5,command = clear())
    clean.grid(row=5,column = 0)
    enter= Button(root,text = 'enter',fg='black',bg='light blue',padx = 5,pady=5,command = equalto())
    enter.grid(row=5,column = 1)

    root.mainloop()
