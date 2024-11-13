import tkinter as tk
from tkinter import messagebox
import random

# Choices and win conditions
choices = ["Rock", "Paper", "Scissors"]
win_conditions = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

# Score counters
player_score = 0
computer_score = 0

# Functions
def update_scores():
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    update_scores()
    result_label.config(text="Let's play again!")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        result = f"Both chose {player_choice}. It's a tie!"
    elif win_conditions[player_choice] == computer_choice:
        player_score += 1
        result = f"You win! {player_choice} beats {computer_choice}."
    else:
        computer_score += 1
        result = f"Computer wins! {computer_choice} beats {player_choice}."
    
    update_scores()
    result_label.config(text=result)

    if player_score == 5:
        messagebox.showinfo("Game Over", "Congratulations, you won the game!")
        reset_game()
    elif computer_score == 5:
        messagebox.showinfo("Game Over", "Computer won the game. Try again!")
        reset_game()

def player_choice(choice):
    computer_choice = get_computer_choice()
    determine_winner(choice, computer_choice)

# GUI setup
app = tk.Tk()
app.title("Rock, Paper, Scissors")
app.geometry("400x350")
app.config(bg="#f0f4f8")

# Labels
title_label = tk.Label(app, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333333")
title_label.pack(pady=15)

player_score_label = tk.Label(app, text="Player Score: 0", font=("Arial", 12), bg="#f0f4f8", fg="#007acc")
player_score_label.pack()

computer_score_label = tk.Label(app, text="Computer Score: 0", font=("Arial", 12), bg="#f0f4f8", fg="#d9534f")
computer_score_label.pack()

result_label = tk.Label(app, text="Make your choice to start!", font=("Arial", 12), bg="#f0f4f8", fg="#333333")
result_label.pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(app, bg="#f0f4f8")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12, "bold"), width=10, bg="#ffa07a", fg="white", command=lambda: player_choice("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12, "bold"), width=10, bg="#8ab6d6", fg="white", command=lambda: player_choice("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12, "bold"), width=10, bg="#d5a6bd", fg="white", command=lambda: player_choice("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Reset button
reset_button = tk.Button(app, text="Restart Game", font=("Arial", 12), bg="#5cb85c", fg="white", command=reset_game)
reset_button.pack(pady=15)

# Run the app
app.mainloop()
