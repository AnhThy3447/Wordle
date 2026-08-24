from tkinter import *
from tkinter import messagebox
from wordle import Wordle
import pandas as pd
import random

# --- DEFINE PARAMETERS ---
bg_color = "black"
current_guess = 0
end_game = False


# --- LOAD WORDS ---
data = pd.read_csv("data/wordle.csv")
word_list = data['word']


# --- CHECK ANSWER ---
def check_answer(user_ans, row):
    global wordle
    guess_label = wordle.check_letter(user_ans)

    for i in range (5):
        letter = user_ans[i]
        color = guess_label[i]
        mfield[row * 5 + i].config(text=letter.upper(), fg="white", bg=color)

    if len(set(guess_label)) == 1 and guess_label[0] == "green":
        return True
    return False

def handle_user_answer(event=None):
    global current_guess, end_game, correct_ans

    if end_game:
        return

    user_ans = entry.get().lower()
    if len(user_ans) == 5:
        if user_ans in set(word_list):
            if check_answer(user_ans, current_guess):
                lab_ans.config(text=f"Correct Answer: {correct_ans.upper()}. YOU WIN !!!",
                                bg=bg_color, fg="yellow", font=("Helvetica", 14, "bold"))
                entry.config(state="disabled")
                end_game = True
            elif current_guess == 5:
                lab_ans.config(text=f"Correct Answer: {correct_ans.upper()}. YOU LOSE!",
                                bg=bg_color, fg="yellow", font=("Helvetica", 14, "bold"))
                entry.config(state="disabled")
                end_game = True
            else:
                current_guess += 1
                entry.delete(0, 'end')
        else:
            messagebox.showwarning("Warning", "It's not in word list")
    else:
        messagebox.showwarning("Warning", "It's a 5-letter word")

def new_game():
    global wordle, correct_ans, mfield, current_guess, end_game
    # reload UI
    lab_ans.config(text="")
    for row in range (6):
        for col in range(5):
            mfield[row * 5 + col].config(text="", relief="groove", bg=bg_color,highlightbackground="white", 
                                         highlightcolor="white", height=1, width=4, font=("Helvetica", 20, "bold"))
    current_guess = 0
    end_game = False
    entry.config(state="normal")
    entry.delete(0, 'end')

    # choose new word
    correct_ans = str(random.choice(word_list))
    wordle = Wordle(correct_ans)
    root.bind('<Return>', handle_user_answer)


# --- GAME INTERFACE ---
root = Tk()
root.title("Wordle")
root.config(bg=bg_color)
root.geometry("450x620")

# Reset button
Button(
    root,
    text="Reset",
    font=("Arial", 8),
    bg="white",
    width=10,
    command=new_game
).pack(side=TOP, anchor=NE, padx=8, pady=5)

# Title
Label(
    root,
    text="WORDLE", 
    font=("Helvetica", 40, "bold"),
    fg="yellow",
    bg=bg_color
).pack(pady=(20, 5))

# Answer box
fr_ans = Frame(root, pady=5, bg=bg_color)
fr_ans.pack(anchor='center', expand=True)

lbl = Label(fr_ans, text="Your Answer", width=10, anchor='w',
            font=("Helvetica", 14, "bold"), bg=bg_color, fg="white")
lbl.pack(side=LEFT, padx=5)           

entry = Entry(fr_ans)
entry.pack(side=LEFT, padx=5)
entry.focus()

# Answer
body = Frame(root, bg=bg_color)
body.pack(fill=BOTH, expand=True)

mfield = []
for row in range (6):
    blocksContainer = Frame(body, bg=bg_color)
    blocksContainer.pack()
    for col in range(5):
        mfield.append(Button(blocksContainer, relief="groove", bg=bg_color,highlightbackground="white", highlightcolor="white",
                     height=1, width=4, font=("Helvetica", 20, "bold")))
        mfield[row * 5 + col].grid(row=0, column=col, padx=2, pady=5, sticky="ew")

# Correct Answer
lab_ans = Label(root, bg=bg_color)
lab_ans.pack(pady=(0, 10))


# --- MAIN ---
new_game()
root.mainloop()