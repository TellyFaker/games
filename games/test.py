import tkinter as tk
import random

root = tk.Tk()
root.title("Test Game")
root.geometry("300x200")

zahl = random.randint(1, 10)

label = tk.Label(root, text=f"Zahl ist: {zahl}", font=("Arial", 20))
label.pack(expand=True)

root.mainloop()
