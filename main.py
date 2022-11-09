from tkinter import *
from tkinter import messagebox
import random
from prompts import prompts

FONT = ("Arial", 20, "normal")
COUNT_SEC = 0
prev_len = 0
timer = None


def start_writing():
    global prev_len

    current_len = len(text_box.get('1.0', END)) - 1
    print(f"Current: {current_len}")
    print(f"Previous: {prev_len}")
    if current_len > prev_len:
        prev_len = current_len
        start_writing()
    else:
        countdown()


def countdown():
    global COUNT_SEC, timer

    COUNT_SEC += 1
    print(COUNT_SEC)
    if COUNT_SEC % 5 != 0:
        timer = window.after(1000, countdown)
    else:
        current_len = len(text_box.get("1.0", END)) - 1
        if current_len == prev_len:
            window.after_cancel(timer)
            messagebox.showinfo(title="Time Out", message="You stopped writing for more than 5 seconds!")
            text_box.delete("1.0", END)
        else:
            start_writing()


def shuffle_prompt():
    new_prompt = random.choice(prompts)
    instruct_label.config(text=new_prompt)


window = Tk()
window.title("Writers Block App")
window.geometry('1100x750')
window.config(padx=50, pady=50)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

instruct_label = Label(text='Click "Generate Prompt" to begin, writing will disappear if there is nothing '
                            'written for 5 seconds.',
                       font=FONT,
                       wraplength=1000
                       )
instruct_label.grid(column=0, row=0, columnspan=2, pady=(0, 40))

start_btn = Button(text="Start Writing", font=FONT, padx=27, command=start_writing)
new_prompt_btn = Button(text="Generate Prompt", font=FONT, command=shuffle_prompt)
start_btn.grid(column=0, row=1)
new_prompt_btn.grid(column=1, row=1)

text_box = Text(width=66, height=14, font=FONT)
text_box.grid(column=0, row=2, columnspan=2, pady=(40, 0))

window.mainloop()
