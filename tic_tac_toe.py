import customtkinter as ctk
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # theme blue hi rehne do

root = ctk.CTk()
root.eval('tk::PlaceWindow . center')
def blink_status():
    current = status.cget("text_color")
    new = "white" if current != "white" else "#d81b60"
    status.configure(text_color=new)
    root.after(300, blink_status)
root.geometry("350x450")
root.title("Tic Tac Toe 💖")

# 👉 BACKGROUND COLOR (baby pink)
root.configure(fg_color="#ffc0cb")

buttons = []
game_over = False


def check_winner():
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in combos:
        if buttons[a].cget("text") == buttons[b].cget("text") == buttons[c].cget("text") != "":
            return buttons[a].cget("text"), (a,b,c)
    return None, None


def highlight(combo):
    for i in combo:
        buttons[i].configure(fg_color="#90ee90")  # light green


def player_click(i):
    global game_over

    if game_over:
        return

    if buttons[i].cget("text") == "":
        buttons[i].configure(text="X", text_color="#ff4da6")  # pink X

        winner, combo = check_winner()
        if winner == "X":
            highlight(combo)
            status.configure(text="🎉 YOU WIN 💖")
            blink_status()
            game_over = True
            return

        if all(btn.cget("text") != "" for btn in buttons):
            status.configure(text="😅 It's a Draw!")
            game_over = True
            return

        computer_move()


def computer_move():
    global game_over

    empty = [i for i in range(9) if buttons[i].cget("text") == ""]
    move = random.choice(empty)

    buttons[move].configure(text="O", text_color="#3399ff")  # blue O

    winner, combo = check_winner()
    if winner == "O":
        highlight(combo)
        status.configure(text="😭 You're out 💔")
        game_over = True
        return

    if all(btn.cget("text") != "" for btn in buttons):
        status.configure(text="😅 It's a Draw!")
        game_over = True


def reset_game():
    global game_over
    for btn in buttons:
        btn.configure(text="", fg_color="#ffe6f0")  # soft pink boxes
    status.configure(text="Your Turn 💖")
    game_over = False


# Title
title = ctk.CTkLabel(root, text="Tic Tac Toe 💖",
                     font=("Arial", 22, "bold"),
                     text_color="#d81b60")
title.pack(pady=10)

# Frame
frame = ctk.CTkFrame(root, fg_color="#ffc0cb")  # same pink bg
frame.pack(pady=10)

# Buttons
for i in range(9):
    btn = ctk.CTkButton(
        frame,
        text="",
        width=80,
        height=60,
        fg_color="#ffe6f0",       # light pink boxes
        hover_color="#ffb6c1",    # hover pink
        text_color="black",
        command=lambda i=i: player_click(i)
    )
    btn.grid(row=i//3, column=i%3, padx=6, pady=6)
    buttons.append(btn)

# Status
status = ctk.CTkLabel(root, text="Your Turn 💖",
                      font=("Arial", 14),
                      text_color="black")
status.pack(pady=10)

# Restart button
reset_btn = ctk.CTkButton(
    root,
    text="🔄 Restart",
    fg_color="#ff69b4",
    hover_color="#ff1493",
    command=reset_game
)
reset_btn.pack(pady=10)

root.mainloop()