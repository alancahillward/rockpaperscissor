import random
import tkinter as tk
from tkinter import *



choices = ['rock', 'paper','scissors']
CPUChoice = random.choice(choices)
PlayerChoice = ""
#Create Window
window = tk.Tk()
window.title("RockPaperScissors by alancahillward")
window.geometry("900x400")
window.resizable(False, False)

#Commands for Button
def Rock():
    PlayerChoice='rock'
    WinCheck(PlayerChoice, CPUChoice)
    f = Label(window, text =f'CPU:{CPUChoice}, P1:{PlayerChoice}', font=('consolas', 40))
    f.pack()
    
    
def Paper():
    PlayerChoice='paper'
    WinCheck(PlayerChoice, CPUChoice)
    f = Label(window, text =f'CPU:{CPUChoice}, P1:{PlayerChoice}', font=('consolas', 40))
    f.pack()
    
    
def Scissors():
    PlayerChoice='scissors'
    WinCheck(PlayerChoice, CPUChoice)
    f = Label(window, text =f'CPU:{CPUChoice}, P1:{PlayerChoice}', font=('consolas', 40))
    f.pack()
    
#Check For Win   
def WinCheck(PlayerChoice, CPUChoice):
        if PlayerChoice == 'rock':
            if CPUChoice == 'scissors':
                Won()
                
            elif CPUChoice == 'paper':
                Lost()
            elif CPUChoice == 'rock':
                Tie()
                
        elif PlayerChoice == 'paper':
            if CPUChoice == 'rock':
                Won()
                
            elif CPUChoice == 'scissors':
                Lost()
            elif CPUChoice == 'paper':
                Tie()
                
        elif PlayerChoice == 'scissors':
            if CPUChoice == 'paper':
                Won()
                print('won')
            elif CPUChoice == 'rock':
                Lost()
            elif CPUChoice == 'scissors':
                Tie()
                
        elif PlayerChoice == CPUChoice:
            Tie()
#Win Conditions
def Won():
    g = Label(window, text='Player Won!', font=('consolas', 40))
    g.pack() 
def Tie():
    g = Label(window, text ='Tie!', font=('consolas', 40))
    g.pack()
def Lost():
    g = Label(window, text='Computer Won!', font=('consolas', 40))
    g.pack()
def EndGame():
    window.destroy()

#Game Header
Header = Label(window, text="Rock Paper Scissors", font=('consolas', 40))
Header.pack()
#Player vs CPU
PvC = Label(window, text="Player vs CPU", font=('consolas', 40))
PvC.pack()
#Rock, paper and scissors buttons
RockButton = tk.Button(window, bg="white", text="Rock", width=50, command=Rock)
RockButton.pack()
PaperButton = tk.Button(window, bg="white", text="Paper", width=50, command=Paper)
PaperButton.pack()
ScissorsButton = tk.Button(window, bg="white", text="Scissors", width=50, command=Scissors)
ScissorsButton.pack()
ResetButton = tk.Button(window, bg="white", text="End Game", width=50, command=EndGame)
ResetButton.pack()




window.mainloop()





