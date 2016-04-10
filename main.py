#v1.1 Tic Tac Toe
#future plans: implement score board

import tkinter
from tkinter import *
import tkinter.messagebox

player_check = True
answer = None
    
rootWindow = Tk()
rootWindow.title("v1.1")
    
label_greeting = Label(master=rootWindow, text="Tic Tac Toe!", font=("Symbol 20 bold italic"), fg="#800020")
label_greeting.grid(column=1, sticky='wesn')

buttons = StringVar()

button_1 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_1))
button_1.grid(row=1, column=0, padx= 0, pady= 0, sticky='wesn')
        
button_2 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_2))
button_2.grid(row=1, column=1, padx=0, pady=0, sticky='wesn')
        
button_3 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_3))
button_3.grid(row=1, column=2, padx=0, pady=0, sticky='wesn')
        
button_4 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_4))
button_4.grid(row=2, column=0, padx=0, pady=0, sticky='wesn')
        
button_5 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_5))
button_5.grid(row=2, column=1, padx=0, pady=0, sticky='wesn')

button_6 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_6))
button_6.grid(row=2, column=2, padx=0, pady=0, sticky='wesn')

button_7 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_7))
button_7.grid(row=3, column=0, padx=0, pady=0, sticky='wesn')

button_8 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_8))
button_8.grid(row=3, column=1, padx=0, pady=0, sticky='wesn')

button_9 = Button(rootWindow, text=" ", height=6, width=6, font=("Arial 20 bold"), fg="blue", command=lambda:checker(button_9))
button_9.grid(row=3, column=2, padx=0, pady=0, sticky='wesn')      

def reset_board():
    button_1["text"] = " "
    button_2["text"] = " "
    button_3["text"] = " "
    button_4["text"] = " "
    button_5["text"] = " "
    button_6["text"] = " "
    button_7["text"] = " "
    button_8["text"] = " "
    button_9["text"] = " "

def checker(buttons): #function will check to see which player's turn it is, as well as check if there's a winner
    global player_check
    global answer
    
    if buttons["text"] == " " and player_check == True:
        buttons["text"] = "X"
        player_check = False
    
    elif buttons["text"] == " " and player_check == False:
        buttons["text"] = "O"
        player_check = True
    
    #Winning Conditions...
    
    elif (button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" or 
    button_4["text"] == "X" and button_5["text"] == "X" and button_6["text"] == "X" or 
    button_7["text"] == "X" and button_8["text"] == "X" and button_9["text"] == "X" or 
    button_3["text"] == "X" and button_5["text"] == "X" and button_7["text"] == "X" or 
    button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" or 
    button_1["text"] == "X" and button_4["text"] == "X" and button_7["text"] == "X" or 
    button_2["text"] == "X" and button_5["text"] == "X" and button_8["text"] == "X" or 
    button_3["text"] == "X" and button_6["text"] == "X" and button_9["text"] == "X"):
        answer = tkinter.messagebox.askyesno("Winner!", "Player X wins! Play again?")
        if answer == False:
            rootWindow.destroy() 
        else:
            reset_board()
            
    
    elif (button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O" or 
    button_4["text"] == "O" and button_5["text"] == "O" and button_6["text"] == "O" or 
    button_7["text"] == "O" and button_8["text"] == "O" and button_9["text"] == "O" or 
    button_3["text"] == "O" and button_5["text"] == "O" and button_7["text"] == "O" or 
    button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O" or 
    button_1["text"] == "O" and button_4["text"] == "O" and button_7["text"] == "O" or 
    button_2["text"] == "O" and button_5["text"] == "O" and button_8["text"] == "O" or 
    button_3["text"] == "O" and button_6["text"] == "O" and button_9["text"] == "O"):
        answer = tkinter.messagebox.askyesno("Winner!", "Player O wins! Play again?")
        if answer == False:
            rootWindow.destroy()
        else: 
            reset_board()
    
    #In the event of a Draw...
    
    else:
        answer = tkinter.messagebox.askyesno("Draw!", "It's a tie! Play again?")
        if answer == False:
            rootWindow.destroy() 
        else:
            reset_board()

rootWindow.mainloop() 