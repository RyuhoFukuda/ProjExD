import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)


def eq_button_click(event):
    get_num = entry.get()
    try:
        result = eval(get_num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except SyntaxError:
        entry.delete(0, tk.END)

def delete_button_click(event):
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("電卓")
root.geometry("600x650")

entry = tk.Entry(justify="right", width=10,  font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0
for i in range(9, -7, -1):
    if i > 0:
        button = tk.Button(root, text=str(i),width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == 0:
        button = tk.Button(root, text="0",width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r, column=c+1)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -1:
        button = tk.Button(root, text="+", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r-2, column=c+2)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -2:
        button = tk.Button(root, text="=", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", eq_button_click)
        button.grid(row=r, column=c+1)
    elif i == -3:
        button = tk.Button(root, text="-", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r-1, column=c+1)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -4:
        button = tk.Button(root, text="*", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r-4, column=c+3)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -5:
        button = tk.Button(root, text="/", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=r-5, column=c+2)
        c += 1
        if c % 3 == 0:
            c = 0
            r += 1
    elif i == -6:
        button = tk.Button(root, text="CE", width=4, height=2, font=("Times New Roman", 30))
        button.bind("<1>", delete_button_click)
        button.grid(row=r-5, column=c+2)

root.mainloop()
