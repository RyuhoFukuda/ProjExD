import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)
#    tkm.showinfo(txt, f"[{txt}]のボタンがクリックされました")

def eq_button_click(event):
    get_num = entry.get()
    result = eval(get_num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)


root = tk.Tk()
root.title("電卓")
root.geometry("300x600")

entry = tk.Entry(justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for i in range(9, -3, -1):
    if i >= 0:
        button = tk.Button(root, text=str(i),width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -1:
        button = tk.Button(root, text="+", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -2:
        button = tk.Button(root, text="=", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", eq_button_click)
        button.grid(row=r, column=c)
    

root.mainloop()
