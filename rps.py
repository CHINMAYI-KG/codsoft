import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    global user_score, computer_score

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Initializing scores
user_score = 0
computer_score = 0

# Tkinter GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

# Labels for choices and results
result_label = tk.Label(root, text="Make your choice!", font=("Helvetica", 14))
result_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your choice: ", font=("Helvetica", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 12))
computer_choice_label.pack()

score_label = tk.Label(root, text=f"Score - You: {user_score}, Computer: {computer_score}", font=("Helvetica", 12))
score_label.pack(pady=10)

# Buttons for user choices
tk.Button(root, text="Rock", command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("scissors")).pack(pady=5)

# Run the Tkinter application
root.mainloop()
