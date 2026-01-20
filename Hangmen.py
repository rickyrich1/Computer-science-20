import ttkbootstrap as ttk
import tkinter.messagebox as mbox
import random

words = ["Enoch", "computer", "joking", "Babatunde", "Exam"]
secret_word = random.choice(words)
guessed_letters = []
lives = 6


def update_display():
    """Update the word and lives labels"""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)
    lives_label.config(text="Lives left: " + str(lives))

def check_win():
    """Return True if the player guessed the word"""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def guess_letter():
    """Process a letter guess"""
    global lives

    letter = entry.get().lower()
    entry.delete(0, "end")

    if len(letter) != 1:
        mbox.showwarning("Invalid", "Buddy one letter at a time")
        return

    if letter in guessed_letters:
        mbox.showinfo("Already Guessed", "Am pretty sure you guessed that already")
        return

    guessed_letters.append(letter)

    if letter not in secret_word:
        lives -= 1

    update_display()

    if check_win():
        mbox.showinfo("You Win!", "Congratulations! The word is: " + secret_word)
        guess_button.config(state="disabled")
        return

    if lives == 0:
        mbox.showinfo("Game Over!", "The word was: " + secret_word)
        guess_button.config(state="disabled")
        return


window = ttk.Window()
window.title("Who wants to be a millionaire")
window.geometry("400x300")

frame = ttk.Frame(window)
frame.pack(pady=10,padx=10,fill='x')

title_label = ttk.Label(frame, text="Guess the word to win be the next milllionaire", font=("Arial", 18))
title_label.pack(pady=10)

word_label = ttk.Label(frame, text="", font=("Courier", 16))
word_label.pack(pady=10)

lives_label = ttk.Label(frame, text="")
lives_label.pack(pady=5)

entry = ttk.Entry(frame, width=10)
entry.pack(pady=10)

guess_button = ttk.Button(frame, text="Guess", command=guess_letter)
guess_button.pack(padx=10,pady=10,fill='x')

update_display()
window.mainloop()
