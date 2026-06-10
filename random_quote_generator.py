import tkinter as tk
import random

quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Success is not final, failure is not fatal.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Never give up because great things take time.", "Anonymous"),
    ("Your only limit is your mind.", "Anonymous"),
    ("Push yourself, because no one else is going to do it for you.", "Anonymous"),
    ("Hard work beats talent when talent doesn't work hard.", "Tim Notke"),
    ("Every accomplishment starts with the decision to try.", "John F. Kennedy"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Success is the sum of small efforts repeated daily.", "Robert Collier"),
    ("Opportunities don't happen. You create them.", "Chris Grosser"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Great things never come from comfort zones.", "Anonymous"),
    ("Work hard in silence, let success make the noise.", "Frank Ocean")
]

def generate_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("700x400")
root.configure(bg="#f4f4f4")

title = tk.Label(
    root,
    text="Random Quote Generator",
    font=("Arial", 20, "bold"),
    bg="#f4f4f4"
)
title.pack(pady=20)

quote_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
quote_frame.pack(padx=30, pady=20, fill="both", expand=True)

quote_label = tk.Label(
    quote_frame,
    text="Click 'New Quote' to generate a quote",
    font=("Arial", 16),
    wraplength=550,
    bg="white",
    justify="center"
)
quote_label.pack(pady=40)

author_label = tk.Label(
    quote_frame,
    text="",
    font=("Arial", 12, "italic"),
    bg="white"
)
author_label.pack()

generate_btn = tk.Button(
    root,
    text="New Quote",
    font=("Arial", 12, "bold"),
    command=generate_quote,
    padx=20,
    pady=10
)
generate_btn.pack(pady=20)

generate_quote()

root.mainloop()