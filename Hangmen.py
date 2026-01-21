import ttkbootstrap as ttk
import tkinter.messagebox as mbox
import random

words = ["educate", "computer", "joking", "table", "exam"]
secret_word = random.choice(words)
guessletters = []
lives = 6
str(map(list, guessletters))
#guessletters.delete(0,"end")


def update_display():
    display = ""
    for letter in secret_word:
        if letter in guessletters:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)
    lives_label.config(text="Lives left: " + str(lives))


def check_win():
    for letter in secret_word:
        if letter not in guessletters:
            return False
    return True

def guessletter2():
    global lives

    letter = entry.get().lower()
    entry.delete(0, "end")

    if len(letter) != 1:
        mbox.showwarning("Invalid", "Buddy one letter at a time")
        return

    if letter in guessletters:
        mbox.showinfo("Already Guessed", "Am pretty sure you guessed that already")
        return

    guessletters.append(letter)

    if letter not in secret_word:
        lives -= 1

    update_display()

    if check_win():
        mbox.showinfo("You Win!", "Congratulations! The word is: " + secret_word)
        guess_button.config(state="disabled")
        return

    if lives == 0:
        mbox.showinfo("Error", "Sorry you lost,The word was: " + secret_word)
        guess_button.config(state="disabled")
        lives_label.delete(0, "end")

        return


window = ttk.Window(themename="darkly")
window.title("Who wants to be a millionaire")
icon = ttk.PhotoImage(file="icon1.jfif")
window.iconphoto(False, icon)
window.geometry("400x300")

frame = ttk.Frame(window)
frame.pack(pady=10,padx=10,fill='x')

title_label = ttk.Label(frame,
                        text="MY SIMPLE HANGMAN"
                        , font=("Serif", 18,"bold"))
title_label.pack(padx=10,pady=10)

word_label = ttk.Label(frame, text="", font=("Courier", 16))
word_label.pack(padx=10,pady=10)

lives_label = ttk.Label(frame, text="")
lives_label.pack(pady=10,padx=10,fill='x')

entry = ttk.Entry(frame, width=10)
entry.pack(padx=10,pady=10,fill='x')

guess_button = ttk.Button(frame, text="Guess", command=guessletter2)
guess_button.pack(padx=10,pady=10,fill='x')

update_display()
window.mainloop()
