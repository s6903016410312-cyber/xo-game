import tkinter as tk
from tkinter import messagebox

# ===================== WINDOW =====================
root = tk.Tk()
root.title("XO Game")
root.geometry("400x500")
root.resizable(False, False)

# ใส่ไอคอน (ถ้ามีไฟล์)
try:
    root.iconbitmap("assets/icon.ico")
except:
    pass

root.configure(bg="#2c3e50")

# ===================== VARIABLES =====================
current_player = "X"
buttons = []

score_x = 0
score_o = 0

# ===================== SCORE LABEL =====================
score_label = tk.Label(
    root,
    text="X: 0 | O: 0",
    font=("Arial", 14, "bold"),
    bg="#2c3e50",
    fg="white"
)
score_label.pack(pady=10)

# ===================== FUNCTIONS =====================
def update_score(winner):
    global score_x, score_o

    if winner == "X":
        score_x += 1
    else:
        score_o += 1

    score_label.config(text=f"X: {score_x} | O: {score_o}")


def check_winner():
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for a, b, c in win_patterns:
        if buttons[a]["text"] != "" and \
           buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"]:

            winner = buttons[a]["text"]
            messagebox.showinfo("Game Over", f"ผู้เล่น {winner} ชนะ!")
            update_score(winner)
            reset_game()
            return

    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Game Over", "เสมอ!")
        reset_game()


def click(btn):
    global current_player

    if btn["text"] == "":
        btn["text"] = current_player
        btn.config(fg="white")

        check_winner()

        current_player = "O" if current_player == "X" else "X"


def reset_game():
    global current_player
    current_player = "X"

    for btn in buttons:
        btn.config(text="", bg="#34495e")


# ===================== TITLE =====================
title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 20, "bold"),
    bg="#2c3e50",
    fg="white"
)
title.pack()

# ===================== BOARD =====================
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=4,
        height=2,
        bg="#34495e",
        fg="white",
        activebackground="#1abc9c",
        command=lambda b=i: click(buttons[b])
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# ===================== RESET BUTTON =====================
reset_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14, "bold"),
    bg="#e67e22",
    fg="white",
    command=reset_game
)
reset_btn.pack(pady=10)

# ===================== RUN =====================
root.mainloop()