from tkinter import *
from tkinter import messagebox

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
    print(button3['text'])
    for cell in btn_ls:
        if cell['text'] == "     ":
            end_game = False
        
    if end_game:
        messagebox.showinfo("Draw!", "It's a tie, This game has no winner.")

def start_game(start_btn:Button):
    global turn
    start_btn['text'] = "Reset Game"
    start_btn['bg'] = "#1338be"
    start_btn['command'] = game

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