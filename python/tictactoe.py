from tkinter import*
from tkinter import messagebox
player = 'X'
stop = False

def clicked(r,c):
    global player
    if b[r][c]['text'] == '' and player =='X' and stop ==False:
        b[r][c].configure(text= "X")
        player = 'O'
    if b[r][c]['text'] == '' and player =='O' and stop ==False:
        b[r][c].configure(text= "O")
        player = 'X'
    check_win()
    if stop == True:
        root.destroy
def check_win():
    global stop
    for i in range(3):
        #horizontal
        if b[i][0]['text']==b[i][1]['text']==b[i][2]['text']!='' :
            stop = True
            winner = messagebox.showinfo('Winner',b[i][0]['text']+ 'Won !')
            break
        elif b[0][i]['text']==b[1][i]['text']==b[2][i]['text']!='' :
            stop = True
            winner = messagebox.showinfo('Winner'+b[0][i]['text']+ 'Won !')
            break
        elif b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] !='':
            stop = True
            winner = messagebox.showinfo("Winner" , b[0][2]['text']+ " Won!")
            break
        elif b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] !='':
            stop = True
            winner = messagebox.showinfo("Winner", b[0][0]['text']+ " Won!")
            break
        elif b[0][0]['text'] and b[0][1]['text'] and b[0][2]['text'] and b[1][0]['text'] and b[1][1]['text'] and b[1][2]['text'] and b[2][0]['text'] and b[2][1]['text'] and b[2][2]['text'] != '':
            stop=True
            tie = messagebox.showinfo('TIE','Tie')



root = Tk()
root.resizable(0,0)
root.title('Tic Tac Toe')
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range (0,3):
    for j in range(0,3):
        b[i][j]=Button(root,text='',height= 5,width=10,font=('arial',12),command=lambda r=i,c=j:clicked(r,c))
        b[i][j].grid(row=i,column=j)

mainloop()
