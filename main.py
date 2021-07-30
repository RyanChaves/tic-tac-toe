from tkinter import *
YELLOW = "#DAF7A6"
FONT_NAME = "Bree Serif"
GREEN ="#58C14F"
BLUE= "#4FA7C1"
DARK_BLUE= "#295E6E"


#x starts the game
x_turn = True
is_winner = False
winner_symbol = ""
#if count = 9 and no winner we have a tie
count=0
x_tally=0
y_tally=0


def btn_clicked(btn):
    global x_turn, count
    #every time a button is clicked, we need to check
    #has that btn been clicked? !=''

    if btn['text']!='':
        print("Already Chosen")
    else:
        count+=1
        if x_turn:
            btn.config(text='X')
            x_turn=False
            o_player_turn_label.grid(row=2, column=4)
            x_player_turn_label.grid_forget()
        else:
            btn.config(text='O')
            x_player_turn_label.grid(row=2, column=0)
            o_player_turn_label.grid_forget()
            x_turn = True
        #now check for win
        check_winner()


def check_winner():
    global is_winner, winner_symbol

    #check all possible win scenarios
    if btn1['text'] == btn2['text'] and btn1['text'] == btn3['text'] and btn1['text'] != '':
        winner_symbol=btn1['text']
        is_winner=True
        btn1.config(bg=GREEN)
        btn2.config(bg=GREEN)
        btn3.config(bg=GREEN)
        end_game()
    elif btn4['text'] == btn5['text'] and btn4['text'] == btn6['text'] and btn4['text'] != '':
        winner_symbol=btn4['text']
        is_winner=True
        btn4.config(bg=GREEN)
        btn5.config(bg=GREEN)
        btn6.config(bg=GREEN)
        end_game()
    elif btn7['text'] == btn8['text'] and btn7['text'] == btn9['text'] and btn7['text'] != '':
        winner_symbol = btn7['text']
        is_winner = True
        btn7.config(bg=GREEN)
        btn8.config(bg=GREEN)
        btn9.config(bg=GREEN)
        end_game()
    elif btn1['text'] == btn4['text'] and btn1['text'] == btn7['text'] and btn1['text'] != '':
        winner_symbol = btn1['text']
        is_winner = True
        btn1.config(bg=GREEN)
        btn4.config(bg=GREEN)
        btn7.config(bg=GREEN)
        end_game()
    elif btn2['text'] == btn5['text'] and btn2['text'] == btn8['text'] and btn2['text'] != '':
        winner_symbol = btn2['text']
        is_winner = True
        btn2.config(bg=GREEN)
        btn5.config(bg=GREEN)
        btn8.config(bg=GREEN)
        end_game()
    elif btn3['text'] == btn6['text'] and btn3['text'] == btn9['text'] and btn3['text'] != '':
        winner_symbol = btn3['text']
        is_winner = True
        btn3.config(bg=GREEN)
        btn6.config(bg=GREEN)
        btn9.config(bg=GREEN)
        end_game()
    elif btn1['text'] == btn5['text'] and btn1['text'] == btn9['text'] and btn1['text'] != '':
        winner_symbol = btn1['text']
        is_winner = True
        btn1.config(bg=GREEN)
        btn5.config(bg=GREEN)
        btn9.config(bg=GREEN)
        end_game()
    elif btn7['text'] == btn5['text'] and btn7['text'] == btn3['text'] and btn7['text'] != '':
        winner_symbol = btn7['text']
        is_winner = True
        btn7.config(bg=GREEN)
        btn5.config(bg=GREEN)
        btn3.config(bg=GREEN)
        end_game()
    elif count == 9:
        winner_symbol = 'T'
        end_game()

def end_game():
    global x_tally, y_tally
    x_player_turn_label.grid_forget()
    o_player_turn_label.grid_forget()
    if winner_symbol == 'X':
        x_winner_label.grid(row=2, column=0)
        x_tally+=1
        x_tally_label.config(text=f"Wins\n {x_tally}")
    elif winner_symbol== 'O':
        y_tally+=1
        y_winner_label.grid(row=2, column=4)
        y_tally_label.config(text=f"Wins\n {y_tally}")

    else:
        tie_label.grid(row=4, column=2, columnspan=2)

    reset_btn.grid(row=4, column=2)
    disable_btns()
    print(f"{winner_symbol} is winner")

#called when game is over
def disable_btns():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

#resets the state to beginning of game
def reset_game():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, count
    reset_btn.grid_forget()
    x_winner_label.grid_forget()
    y_winner_label.grid_forget()
    tie_label.grid_forget()
    btn1 = Button(root, text="", command=lambda: btn_clicked(btn1), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn2 = Button(root, text="", command=lambda: btn_clicked(btn2), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn3 = Button(root, text="", command=lambda: btn_clicked(btn3), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn4 = Button(root, text="", command=lambda: btn_clicked(btn4), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn5 = Button(root, text="", command=lambda: btn_clicked(btn5), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn6 = Button(root, text="", command=lambda: btn_clicked(btn6), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn7 = Button(root, text="", command=lambda: btn_clicked(btn7), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn8 = Button(root, text="", command=lambda: btn_clicked(btn8), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)
    btn9 = Button(root, text="", command=lambda: btn_clicked(btn9), font=(FONT_NAME, 20, "bold"), height=2, width=5,
                  bg=BLUE, activebackground=DARK_BLUE)

    btn1.grid(row=1, column=1)
    btn2.grid(row=1, column=2)
    btn3.grid(row=1, column=3)
    btn4.grid(row=2, column=1)
    btn5.grid(row=2, column=2)
    btn6.grid(row=2, column=3)
    btn7.grid(row=3, column=1)
    btn8.grid(row=3, column=2)
    btn9.grid(row=3, column=3)

    count=0

root = Tk()
root.title("Tic-Tac-Toe")
root.config(padx=50,pady=50, bg=YELLOW)
cross_logo_label = Label(text='X', bg=YELLOW, font=(FONT_NAME, 50, "bold"), padx=40)
cross_logo_label.grid(row=0,column=0)

circle_logo_label = Label(text='O', bg=YELLOW, font=(FONT_NAME, 50, "bold"), padx=40)
circle_logo_label.grid(row=0,column=4)

x_player_turn_label = Label(text='Your turn', bg=YELLOW, font=(FONT_NAME, 15, "bold"))
x_player_turn_label.grid(row=2, column=0)
o_player_turn_label = Label(text='Your turn', bg=YELLOW, font=(FONT_NAME, 15, "bold"), )
o_player_turn_label.grid(row=2, column=4)
o_player_turn_label.grid_forget()

top_label = Label(text='Tic-Tac-Toe', bg=YELLOW, font=(FONT_NAME, 20, "bold"))
top_label.grid(row=0,column=1, columnspan=3)

x_winner_label = Label(text='Winner!', bg=YELLOW, font=(FONT_NAME, 20, "bold"))
y_winner_label = Label(text='Winner', bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tie_label = Label(text='Tie!', bg=YELLOW, font=(FONT_NAME, 20, "bold"))

reset_btn = Button(root,text='Restart?',font=(FONT_NAME, 13, "bold"),bg=BLUE, command=reset_game)

x_tally_label = Label(text="Wins\n ", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
x_tally_label.grid(row=4, column=0)
y_tally_label = Label(text="Wins\n ", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
y_tally_label.grid(row=4, column=4)

reset_game()

# while game_is_on:
#      pass


root.mainloop()