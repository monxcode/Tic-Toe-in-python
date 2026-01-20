import tkinter as tk
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("TIC TAC TOE - By Mohan Singh Parmar")
root.geometry("230x320")  # Reduced height for a smaller window
root.configure(bg="#282c34")

current_player = "X"
x_wins = 0
o_wins = 0

# UI elements with new design
title_label = tk.Label(root, text="TIC TAC TOE", font=('Verdana', 18, 'bold'), fg="#ff6347", bg="#282c34")
title_label.pack(pady=(20, 10))

# Name in normal style
name_label = tk.Label(root, text="By Mohan Singh Parmar", font=('Arial', 12, 'bold'), fg="white", bg="#282c34")
name_label.pack(pady=(5, 10))  # Display your name under the title

# Frame moved lower
frame = tk.Frame(root, bg="#282c34")
frame.place(relx=0.5, rely=0.55, anchor="center")  # Game box is moved down further

turn_label = tk.Label(root, text="Player X's Turn", font=('Arial', 10, 'bold'), fg="white", bg="#282c34")
turn_label.pack(pady=(10, 5))

# Win count display
win_count_label = tk.Label(root, text=f"X: {x_wins} | O: {o_wins}", font=('Arial', 12, 'bold'), fg="white", bg="#282c34")
win_count_label.pack(pady=(5, 10))

buttons = [[None, None, None] for _ in range(3)]

# Check if a player has won
def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

# Check if the game is a draw
def is_draw():
    for row in buttons:
        for btn in row:
            if btn['text'] == "":
                return False
    return True

# Function to handle button click
def on_click(row, col):
    global current_player, x_wins, o_wins
    if buttons[row][col]['text'] == "":
        buttons[row][col]['text'] = current_player
        buttons[row][col].config(font=('Arial', 16, 'bold'), relief="sunken", fg="#FFFFFF", bg="#4682B4")
        if check_winner():
            if current_player == "X":
                x_wins += 1
            else:
                o_wins += 1
            win_count_label.config(text=f"X: {x_wins} | O: {o_wins}")
            messagebox.showinfo("Game Over", f"Player {current_player} जीत गया!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "मैच ड्रा हो गया!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Player {current_player}'s Turn")

# Reset the board after game ends
def reset_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""
            buttons[i][j].config(bg="#f4f4f4", fg="black", relief="raised")

# Create buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", width=6, height=3,
                        font=('Arial', 16, 'bold'),
                        relief="raised", bd=4, fg="black", bg="#f4f4f4",
                        command=lambda row=i, col=j: on_click(row, col))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# Studio name between game and bottom
studio_label = tk.Label(root, text="Creator: MONXCODE", font=('Arial', 8), fg="gray", bg="#282c34")
studio_label.pack(pady=(10, 10))  # Positioned between the game and the bottom

# Reset button positioned at the bottom
reset_button = tk.Button(root, text="Reset Game", font=('Arial', 10), command=reset_board, fg="black", bg="#98C8E8")
reset_button.pack(side="bottom", pady=10)  # Placed at the very bottom

root.mainloop()