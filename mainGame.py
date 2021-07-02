from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from random import randint
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
import matplotlib.pyplot as plt
import numpy
import sys
import matplotlib
from numpy.core.fromnumeric import size

matplotlib.use('TkAgg')


# GUI Components
root = Tk()
root.title("Rock, Paper, Scissors")
root.configure(background="#171717")
root.geometry("1000x900")
root.resizable(width=FALSE, height=FALSE)
rock = PhotoImage(file='images/Rock.png')
paper = PhotoImage(file='images/Paper.png')
scissors = PhotoImage(file='images/Scissors.png')


# Declarations
imageList = [rock, paper, scissors]
userChoiceValue = 0
botNumber = randint(0, 2)
global scoreAdd
scoreAdd = 0
global userPoints
userPoints = 0
global botPoints
botPoints = 0


def reset():
    global botPoints
    global userPoints
    userPoints -= userPoints
    botPoints -= botPoints
    bot.config(text="BOT: 0")
    user.config(text="USER: 0")
    label = ("BOT", "USER")
    y = [0, 0]
    fig = plt.figure(figsize=(3, 5), dpi=100)
    plt.bar(label, y, align='center', alpha=1.0)
    # plt.show()
    canvasbar = FigureCanvasTkAgg(fig, master=root)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.82, rely=0.55, anchor=CENTER)


def updateBar():
    label = ("BOT", "USER")
    y = [botPoints, userPoints]
    fig = plt.figure(figsize=(3, 5), dpi=100)
    plt.bar(label, y, align='center', alpha=1.0)
    # plt.show()
    canvasbar = FigureCanvasTkAgg(fig, master=root)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.82, rely=0.55, anchor=CENTER)


def shoot():
    global botPoints
    global userPoints
    global scoreAdd
    userChoiceValue = 0
    botNumber = randint(0, 2)
    # Show Image
    botLabel.config(image=imageList[botNumber])
    # 0 - Rock, 1  - Paper, 2 - Scissors
    # Convert
    if userChoice.get() == "Rock":
        userChoiceValue = 0
    if userChoice.get() == "Paper":
        userChoiceValue = 1
    if userChoice.get() == "Scissors":
        userChoiceValue = 2
    userLabel.config(image=imageList[userChoiceValue])

    # Win Or Lose
    if userChoiceValue == 0:  # Rock
        if botNumber == 0:
            winOrLose.config(text="TIE")
        elif botNumber == 1:
            winOrLose.config(text="BOT WINS!")
            botPoints += 1
            bot.config(text="BOT: " + str(botPoints))
        elif botNumber == 2:
            winOrLose.config(text="PLAYER WINS!")
            userPoints += 1
            user.config(text="USER: " + str(userPoints))

    if userChoiceValue == 1:  # Paper
        if botNumber == 0:
            winOrLose.config(text="PLAYER WINS")
            userPoints += 1
            user.config(text="USER: " + str(userPoints))
        elif botNumber == 1:
            winOrLose.config(text="TIE")
        elif botNumber == 2:
            winOrLose.config(text="BOT WINS!")
            botPoints += 1
            bot.config(text="BOT: " + str(botPoints))

    if userChoiceValue == 2:  # Scissors
        if botNumber == 0:
            winOrLose.config(text="BOT WINS")
            botPoints += 1
            bot.config(text="BOT: " + str(botPoints))
        elif botNumber == 1:
            winOrLose.config(text="PLAYER WINS!")
            userPoints += 1
            user.config(text="USER: " + str(userPoints))
        elif botNumber == 2:
            winOrLose.config(text="TIE!")


# Choose
userChoice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))

# GAME TITLE
gameName = Label(root, text="ROCK, PAPER, SCISSORS!",
                 bg='#171717', fg='white', font=("Montserrat", 22, BOLD))
gameName.place(relx=0.50, rely=0.1, anchor='center')

# BOT'S CHOICE
botName = Label(root, text="BOT", bg='#171717',
                fg='white', font=("Montserrat", 22))
botName.place(relx=0.25, rely=0.3, anchor='center')
botLabel = Label(root, image=imageList[botNumber], bd=0)
botLabel.pack(pady=20)
botLabel.place(relx=0.25, rely=0.4, anchor='center')

# PLAYER'S CHOICE
userName = Label(root, text="USER", bg='#171717',
                 fg='white', font=("Montserrat", 22))
userName.place(relx=0.25, rely=0.6, anchor='center')
userLabel = Label(root, image=imageList[userChoiceValue], bd=0)
userLabel.pack(pady=20, padx=50)
userLabel.place(relx=0.25, rely=0.7, anchor='center')

# PLAYER SCORE
user = Label(root, text="USER: 0", bg='#171717',
             fg='white', font=("Montserrat", 15))
user.place(relx=0.45, rely=0.65, anchor='center')

# BOT SCORE
bot = Label(root, text="BOT: 0", bg='#171717',
            fg='white', font=("Montserrat", 15))
bot.place(relx=0.45, rely=0.7, anchor='center')


# Choose
userChoice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
userChoice.current(0)
userChoice.pack(pady=20)
userChoice.place(relx=0.50, rely=0.25, anchor='center')

# Shoot Button
shootButton = Button(root, text="Shoot!", bg='#171717',
                     border=None, fg="white", font="Montserrat", command=lambda: [shoot(), updateBar()])
shootButton.pack(padx=15)
shootButton.place(rely=0.35, relx=0.45)

# Reset Button
resetButton = Button(root, text="Reset", bg='#171717',
                     border=None, fg="white", font="Montserrat", command=lambda: [reset(), updateBar()])
resetButton.pack(padx=15)
resetButton.place(rely=0.45, relx=0.45)


# IF WON
winOrLose = Label(root, text="SHOOT YOUR SHOT!", bg='#171717',
                  fg='white', font=("Montserrat", 15), bd=0)
winOrLose.pack(pady=50)
winOrLose.place(rely=0.55, relx=0.38)


label = ("BOT", "USER")
y = [botPoints, userPoints]
fig = plt.figure(figsize=(3, 5), dpi=100)
plt.bar(label, y, align='center', alpha=1.0)
# plt.show()
canvasbar = FigureCanvasTkAgg(fig, master=root)
canvasbar.draw()
canvasbar.get_tk_widget().place(relx=0.82, rely=0.55, anchor=CENTER)


# LOOP
root.mainloop()
