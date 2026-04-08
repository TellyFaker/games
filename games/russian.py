import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Russisch")
root.geometry("300x300")

chamber = random.randint(1, 6)
current = 1

label = tk.Label(root, text="Drück ab 😈")
label.pack(pady=20)

def shutdown():
    os.system("shutdown /s /t 1")

def shoot():
    global current

    if current == chamber:
        label.config(text="💥 BUMM")
        root.after(1000, shutdown)
    else:
        label.config(text="😅 Klick")
        current += 1

tk.Button(root, text="🔫", command=shoot).pack()

root.mainloop()