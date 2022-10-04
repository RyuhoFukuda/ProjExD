import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタン押されました")

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

r, c = 0, 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=str(i),width=4, height=2, font=("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(row=r, column=c)
    c += 1
    if c % 3 == 0:
        c = 0
        r += 1

root.mainloop()
