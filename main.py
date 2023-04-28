from tkinter import *
from tkinter import messagebox

board = Tk()
board.title("Tic-Tac_Toe")
board.geometry("360x340")
board.config(bg="#eee")
board.resizable(False, False)
#=============================
turn = "X"

def btn_click(btn:Button):
    global turn
    btn['text'] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print(turn)

def start_game(start_btn:Button):
    global turn
    start_btn['text'] = "Reset Game"
    start_btn['bg'] = "#1338be"
    start_btn['command'] = game

    button1 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button1))
    button1.place(x=4, y=80)

    button2 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button2))
    button2.place(x=4, y=165)

    button3 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button3))
    button3.place(x=4, y=250)

    button4 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button4))
    button4.place(x=92, y=80)

    button5 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button5))
    button5.place(x=92, y=165)

    button6 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button6))
    button6.place(x=92, y=250)

    button7 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button7))
    button7.place(x=180, y=80)

    button8 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button8))
    button8.place(x=180, y=165)

    button9 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button9))
    button9.place(x=180, y=250)

#=============================
def game():    
    for widget in board.winfo_children():
        widget.destroy()
    
    x_entry = Entry(board,fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
    x_entry.place(x=5, y=6)           
    x_entry.insert(0, "Enter name of X player:")
    Frame(board, width=162, height=2,bg="navy").place(x=5, y=26)

    o_entry = Entry(board,fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
    o_entry.place(x=193, y=6)           
    o_entry.insert(0, "Enter name of O player:")
    Frame(board, width=162, height=2,bg="#b90e0a").place(x=193, y=26)

    start_btn = Button(board, width=49, height=2, text="Start Game!", fg="#fff", bg="navy", font=("Helvetica", 9), border=0, command=lambda: start_game(start_btn))
    start_btn.place(x=5, y=36)

    board.mainloop()

game()