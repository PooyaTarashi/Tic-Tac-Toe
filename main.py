from tkinter import *
from tkinter import messagebox

"""
This is a classic two-player Tic Tac Toe game. The game board consists of a 3x3 button grid, and each player takes turns marking their symbol on the board. The first player to get three symbols in a row (horizontally, vertically, or diagonally) wins the game. If all spaces are filled and no player has won, then the game ends in a tie.
To start the game, run the `game()` function.
Here are some additional features:
- every player has a different color
- button colors are changed by every click
- the turn is placed and determined on the screen
- there is a reset button
- This game is coded by a genius, stylish, good-natured coder and graphic designer.
"""

board = Tk()
board.title("Tic-Tac_Toe")
board.geometry("360x340")
board.config(bg="#eee")
board.resizable(False, False)
#=============================
turn = "X"



def btn_click(btn:Button, btn_ls:list):
    button1, button2, button3, button4, button5, button6, button7, button8, button9 = btn_ls
    global turn
    global x_name
    global o_name
    btn['text'] = turn
    btn['disabledforeground'] = '#fff'
    if turn == 'X':
        btn['bg'] = '#597883'
        turn = 'O'
    else:
        btn['bg'] = '#bc544b'
        turn = 'X'
    btn['state'] = DISABLED
    end_game = True
    x_wins = False
    o_wins = False

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        x_wins = True
    
    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
        button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        o_wins = True

    
    for cell in btn_ls:
        if cell['text'] == "     ":
            end_game = False
        
    if x_wins:
        messagebox.showinfo("X wins!", "{} is winner!".format(x_name))
        for cell in btn_ls:
            cell['state'] = DISABLED

    if o_wins:
        messagebox.showinfo("O wins!", "{} is winner!".format(o_name))
        for cell in btn_ls:
            cell['state'] = DISABLED

    if end_game and not x_wins and not o_wins:
        messagebox.showinfo("Draw!", "It's a tie, This game has no winner.")

def start_game(start_btn:Button, x_n, o_n):
    global turn
    global x_name
    global o_name
    x_name = x_n
    o_name = o_n
    start_btn['text'] = "Reset Game"
    start_btn['bg'] = "#1338be"
    start_btn['command'] = game

    lbl = Label(board, text="turn:", fg='black')
    lbl.place(x=300, y=160)
    color = ''
    if turn == 'X':
        color = "navy"
    else:
        color = "#b90e0a"
    trn_lbl = Label(board, text=turn, fg=color, font=('CircularStd-Bold', 25))
    trn_lbl.place(x=300, y=180)


    button1 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button1, btns_ls))
    button1.place(x=4, y=80)

    button2 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button2, btns_ls))
    button2.place(x=4, y=165)

    button3 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button3, btns_ls))
    button3.place(x=4, y=250)

    button4 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button4, btns_ls))
    button4.place(x=92, y=80)

    button5 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button5, btns_ls))
    button5.place(x=92, y=165)

    button6 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button6, btns_ls))
    button6.place(x=92, y=250)

    button7 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button7, btns_ls))
    button7.place(x=180, y=80)

    button8 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button8, btns_ls))
    button8.place(x=180, y=165)

    button9 = Button(board, text="     ", font='CircularStd-Bold 20', bg='#fff', fg='black', height=2, width=5, command=lambda: btn_click(button9, btns_ls))
    button9.place(x=180, y=250)

    btns_ls = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

#=============================
x_name = ''
o_name = ''

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

    start_btn = Button(board, width=49, height=2, text="Start Game!", fg="#fff", bg="navy", font=("Helvetica", 9), border=0, command=lambda: start_game(start_btn, x_entry.get(), o_entry.get()))
    start_btn.place(x=5, y=36)

    board.mainloop()

game()