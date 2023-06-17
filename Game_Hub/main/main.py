import os
from tkinter import *
from PIL import ImageTk, Image
import SignUp.signup as s
import SignIn.signin as l
import Games.ttt as tic_tac_toe
import Games.pingpong as ping


image_path = "E:\\Scripts\\programes\\MRUH\\App_dev\\Game_Hub\\main\\Images\\"
"""def logo():
    logo_img = Image.open("E:\\Scripts\\programes\\MRUH\\App_dev\\Game_Hub\\main\\Images\\logo1.jpg")
    logo_resize = logo_img.resize((100,200))
    imagelogo = ImageTk.PhotoImage(logo_resize)
    label_logo = Label(root, image=imagelogo, height=100, width=200)
    label_logo.grid(row=5, column=5, padx=10, pady=10)
    #label_logo.pack()"""
def ttt():
    ttt = Toplevel()
    ttt.title("Tic-Tac-Toe")
    ttt.geometry("400x400")
    ttt.config(bg="#1a1a1a")
    img_tic_tac_toe = Image.open(image_path+"tic-tac-toe.jpg")
    tic_tac_toe_resize = img_tic_tac_toe.resize((100,100))
    imgt = ImageTk.PhotoImage(tic_tac_toe_resize)
    labelt = Label(ttt, image=imgt, height=100, width=100)
    labelt.grid(row=0, column=0, padx=10, pady=10)
    text_label = Label(ttt, text="TIC-TAC-TOE", bg="#1a1a1a", fg="White").grid(row=0, column=1, padx=10, pady=10)
    play_button = Button(ttt, text="PLAY", bg="#1a1a1a", fg="White", command=tic_tac_toe.ttt).grid(row=0, column=2, padx=15, pady=15)
    about_ttt="""About TIC-TAC-TOE:\n\n\n Tic-tac-toe is a game in which two players take turns in drawing either an ` O' or an ` X' in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row. ...a game of tic-tac-toe. """
    text_widget = Text(ttt,height= 20, width = 20, bg="#1a1a1a", fg="White")
    text_widget.insert(END, about_ttt)
    text_widget.grid(row=2, column=0, padx=10, pady=10)
    ttt.mainloop()

def pingpong():
    ping_pong = Toplevel()
    ping_pong.title("Ping-Pong")
    ping_pong.geometry("400x400")
    ping_pong.config(bg="#1a1a1a")
    img_ping_pong = Image.open(image_path+"ping-pong.jpg")
    ping_pong_resize = img_ping_pong.resize((100,100))
    imgp = ImageTk.PhotoImage(ping_pong_resize)
    labelp = Label(ping_pong, image=imgp, height=100, width=100)
    labelp.grid(row=0, column=0, padx=10, pady=10)
    text_label = Label(ping_pong, text="PING-PONG", bg="#1a1a1a", fg="White").grid(row=0, column=1, padx=10, pady=10)
    play_button = Button(ping_pong, text="PLAY", bg="#1a1a1a", fg="White", command=ping.pong_game).grid(row=0, column=2, padx=15, pady=15)
    about_ping_pong="""About PING-PONG:\n Pong, groundbreaking electronic game released in 1972 by the American game manufacturer Atari, Inc. One of the earliest video games, Pong became wildly popular and helped launch the video game industry. The original Pong consisted of two paddles that players used to volley a small ball back and forth across a screen. """
    text_widget = Text(ping_pong,height= 20, width = 20, bg="#1a1a1a", fg="White")
    text_widget.insert(END, about_ping_pong)
    text_widget.grid(row=2, column=0, padx=10, pady=10)
    ping_pong.mainloop()


def menu():
    menu = Menu(root)
    root.config(menu=menu)
    root_menu = Menu(menu)
    menu.add_cascade(label="Games")
    menu.add_cascade(label="Sign Up", command=s.signup)
    menu.add_cascade(label="Sign In", command=l.signin)
    #menu.add_cascade(label="Profile")

root = Tk()
root.title("GAME-HUB")
root.geometry("500x500")
root.config(bg='#1a1a1a')
#logo()
menu()



#ping-pong
img_ping_pong = Image.open(image_path+"ping-pong.jpg")
ping_pong_resize = img_ping_pong.resize((100,100)) #, Image.ANTIALIAS
imgp = ImageTk.PhotoImage(ping_pong_resize)
labelp = Label(root ,image=imgp, height=100, width=100)
labelp.grid(row=0, column=1, padx=10, pady=10)
ping_pong = Button(root, text="Ping-Pong", bg="#1a1a1a", fg="White", command=pingpong).grid(row=1, column=1, padx=15, pady=15)

#tic_tac_toe
img_tic_tac_toe = Image.open(image_path+"tic-tac-toe.jpg")
tic_tac_toe_resize = img_tic_tac_toe.resize((100,100))
imgt = ImageTk.PhotoImage(tic_tac_toe_resize)
labelt = Label(root, image=imgt, height=100, width=100)
labelt.grid(row=0, column=0, padx=10, pady=10)
hangman = Button(root, text="Tic-Tac-Toe", bg="#1a1a1a", fg="White", command=ttt).grid(row=1, column=0, padx=15, pady=15)

#sudoku
img_sudoku = Image.open(image_path+"sudoku.jpg")
sudoku_resize = img_sudoku.resize((100,100))
imgs = ImageTk.PhotoImage(sudoku_resize)
labels = Label(root, image=imgs, height=100, width=100)
labels.grid(row=0, column=2, padx=10, pady=10)
sudoku = Button(root, text="Sudoku", bg="#1a1a1a", fg="White").grid(row=1, column=2, padx=15, pady=15)

#hangman
img_hangman = Image.open(image_path+"hangman.jpg")
hangman_resize = img_hangman.resize((100,100))
imgh = ImageTk.PhotoImage(hangman_resize)
labelh = Label(root, image=imgh, height=100, width=100)
labelh.grid(row=0, column=3, padx=10, pady=10)
hangman = Button(root, text="Hangman", bg="#1a1a1a", fg="White").grid(row=1, column=3, padx=15, pady=15)

#othello
img_othello = Image.open(image_path+"othello.jpg")
othello_resize = img_othello.resize((100,100))
imgo = ImageTk.PhotoImage(othello_resize)
labelo = Label(root, image=imgo, height=100, width=100)
labelo.grid(row=2, column=0, padx=10, pady=10)
hangman = Button(root, text="Othello", bg="#1a1a1a", fg="White").grid(row=3, column=0, padx=15, pady=15)

#minesweeper
img_minesweeper= Image.open(image_path+"minesweeper.jpg")
minesweeper_resize = img_minesweeper.resize((100,100))
imgm = ImageTk.PhotoImage(minesweeper_resize)
labelm = Label(root, image=imgm, height=100, width=100)
labelm.grid(row=2, column=1, padx=10, pady=10)
minesweeper = Button(root, text="Minesweeper", bg="#1a1a1a", fg="White").grid(row=3, column=1, padx=15, pady=15)

#memory-game
img_memory_game= Image.open(image_path+"memory-game.jpg")
memory_game_resize = img_memory_game.resize((100,100))
imgmg = ImageTk.PhotoImage(memory_game_resize)
labelmg = Label(root, image=imgmg, height=100, width=100)
labelmg.grid(row=2, column=2, padx=10, pady=10)
memory_game = Button(root, text="Memory Game", bg="#1a1a1a", fg="White").grid(row=3, column=2, padx=15, pady=15)

#snake-game
img_snake_game= Image.open(image_path+"Snake-Game.jpg")
snake_game_resize = img_snake_game.resize((100,100))
imgsk = ImageTk.PhotoImage(snake_game_resize)
labelsk = Label(root, image=imgsk, height=100, width=100)
labelsk.grid(row=2, column=3, padx=10, pady=10)
snake_game = Button(root, text="Snake Game", bg="#1a1a1a", fg="White").grid(row=3, column=3, padx=15, pady=15)

root.mainloop()
