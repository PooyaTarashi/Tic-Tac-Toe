from tkinter import *
from tkinter import messagebox

board = Tk()
board.title("Tic-Tac_Toe")
board.geometry("360x360")
board.config(bg="#eee")
board.resizable(True, True)
#=============================
def start_game():
    pass

#=============================
x_entry = Entry(board,fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
x_entry.place(x=5, y=6)           
x_entry.insert(0, "Enter name of X player:")
Frame(board, width=162, height=2,bg="navy").place(x=5, y=26)

o_entry = Entry(board,fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
o_entry.place(x=193, y=6)           
o_entry.insert(0, "Enter name of O player:")
Frame(board, width=162, height=2,bg="#b90e0a").place(x=193, y=26)

Button(board, width=49, text="Start Game!", fg="#fff", bg="navy", border=0, command=start_game).place(x=5, y=40)

board.mainloop()