from tkinter import * 
from tkinter import messagebox 
Player = 'X'#First player
stop_game = False
def clicked(r,c):
    global Player
    #X's turn
    if Player == "X" and b[r][c]['text'] == '' and stop_game == False:
        b[r][c].configure(text = "X")
        Player='O'      
    #o's turn
    if Player == 'O' and b[r][c]['text'] == '' and stop_game == False:
        b[r][c].configure(text = 'O')
        Player = "X"
#Check if game is over
    check_if_win()
    if stop_game == True:
        root.destroy()    
def check_if_win():
    global stop_game 
    for i in range(3):
        #Horizontal match
        if b[i][0]['text'] == b[i][1]['text'] == b[i][2]['text'] !='':
            stop_game = True
            winner = messagebox.showinfo("Winner", b[i][0]['text'] + " Won")
            break
        #Vertical Match
        elif b[0][i]['text'] == b[1][i]['text'] == b[2][i]['text'] != '':
            stop_game = True
            winner = messagebox.showinfo("Winner", b[0][i]['text']+ " Won!")
            break
        #Left diagonal
        elif b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] !='':
            stop_game = True
            winner = messagebox.showinfo("Winner", b[0][0]['text']+ " Won!")
            break
        #Right diagonal
        elif b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] !='':
            stop_game = True
            winner = messagebox.showinfo("Winner" , b[0][2]['text']+ " Won!")
            break
        #Tie case
        elif b[0][0]['text'] and b[0][1]['text'] and b[0][2]['text'] and b[1][0]['text'] and b[1][1]['text'] and b[1][2]['text'] and b[2][0]['text'] and b[2][1]['text'] and b[2][2]['text'] != '':
            stop_game = True
            winner = messagebox.showinfo("tie", "Tie")
            break
# Design window
root = Tk()            
root.title("Tic Tac Toe")  
root.resizable(0,0)
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(3):
    for j in range(3):                                  
        b[i][j] = Button(height = 2, width = 4, font = ("Helvetica","20"),
                         command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)
mainloop()
