import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]のボタンがクリックされました")

root = tk.Tk()
root.title("電卓")
root.geometry("300x600")

entry = tk.Entry(justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=str(i),width=4, height=2, font=("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(row=r, column=c)
    c += 1
    if c % 3 == 0:
        c = 0
        r += 1


root.mainloop()
