import tkinter as tk
from tkinter import messagebox
import random as rnd


def start_game():
    global word, category, guesses_left, guessed_letters, word_display
   

# Start the game
start_game()


import tkinter as tk
from tkinter import messagebox
import random as rnd
from tkinter import *

# Word lists 
frutas = ['maça', 'pera', 'laranja', 'uva', 'banana', 'manga', 'melancia', 'morango']
animal = ['cachorro', 'gato', 'papagaio', 'cavalo', 'camelo', 'girafa', 'rato', 'tigre']
objeto = ['cadeira', 'mesa', 'bolsa', 'fone', 'celular', 'notebook', 'lapis', 'tênis']

def start_game():
    global word, category, guesses_left, guessed_letters, word_display
    guesses_left = 10
    guessed_letters = []
    word_display = []

    # Choose a random word and category
    npalavra = rnd.randint(0, 7)
    nlista = rnd.randint(0, 2)
    if nlista == 0:
        word = frutas[npalavra]
        category = "FRUTAS"
    elif nlista == 1:
        word = animal[npalavra]
        category = "ANIMAIS"
    else:
        word = objeto[npalavra]
        category = "OBJETOS"

    # Initialize the word display with underscores
    for letter in word:
        word_display.append("_")

    # Update the display
    update_display()

def handle_guess():
    global guesses_left, guessed_letters, word_display
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)  # Clear the entry field

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Entrada inválida", "Entre com algo válido!")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Essa letra já foi usada")
        return

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
        update_display()
        if "".join(word_display) == word:
            messagebox.showinfo("Você acertou!", f"Parabéns, a palavra era {word.upper()} !")
            reset_game()
    else:
        guesses_left -= 1
        if guesses_left == 9:
            img["file"] = "erro=0.png"
            update_display()
        if guesses_left == 8:
            img["file"] = "erro=1.png"
            update_display()
        if guesses_left == 7:
            img["file"] = "erro=2.png"
            update_display()
        if guesses_left == 6:
            img["file"] = "erro=3.png"
            update_display()
        if guesses_left == 5:
            img["file"] = "erro=4.png"
            update_display()
        if guesses_left == 4:
            img["file"] = "erro=5.png"
            update_display()
        if guesses_left == 3:
            img["file"] = "erro=6.png"
            update_display()
        if guesses_left == 2:
            img["file"] = "erro=7.png"
            update_display()
        if guesses_left == 1:
            img["file"] = "erro=8.png"
            update_display()
        
        if guesses_left == 0:
            img["file"] = "erro=9.png"
            update_display()
            messagebox.showinfo("Você não acertou", f"Infelizmente suas tentativas acabaram, a palavra era {word.upper()}.")
            reset_game()

def update_display():
    # Update the word display label
    word_label.config(text=" ".join(word_display))
    # Update the category label
    category_label.config(text=f"Categoria: {category}")
    # Update the guesses left label
    guesses_label.config(text=f"Tentativas Restantes: {guesses_left}")
    # Update the guessed letters label
    guessed_label.config(text=f"Letras Já Tentadas: {' '.join(guessed_letters)}")

def reset_game():
    global guesses_left, guessed_letters, word_display
    guesses_left = 10
    guessed_letters = []
    word_display = []
    start_game()

# Create the main window
window = tk.Tk()
window.title("Jogo da Forca")

# Create labels
category_label = tk.Label(window, text="Categoria: ", font=("Arial", 14))
category_label.grid(row=0, column=0, pady=10)

word_label = tk.Label(window, text=" ", font=("Arial", 24))
word_label.grid(row=1, column=0, pady=10)

guesses_label = tk.Label(window, text="Tentativas Restantes: ", font=("Arial", 14))
guesses_label.grid(row=2, column=0, pady=5)

guessed_label = tk.Label(window, text="Letras Já Tentadas: ", font=("Arial", 14))
guessed_label.grid(row=3, column=0, pady=5)

# Create entry field for guess
guess_entry = tk.Entry(window, font=("Arial", 14), width=2)
guess_entry.grid(row=4, column=0, pady=10)

# Create submit button
submit_button = tk.Button(window, text="Enviar", font=("Arial", 14), command=handle_guess)
submit_button.grid(row=5, column=0)

img = PhotoImage(file="")
label_img = Label(window, image=img)
label_img.grid(column=0, row=6, pady=10)

# Start the game
start_game()

window.mainloop()





