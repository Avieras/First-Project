import tkinter as tk
from tkinter import ttk

def add_item(entry, checklist):
    item = entry.get()
    checklist.insert(tk.END, item)
    entry.delete(0, tk.END)
    update_count()

def remove_item(checklist):
    selected = checklist.curselection()
    if selected:
        index = selected[0]
        checklist.delete(index)
        update_count()

def update_count(count_label, checklist):
    count_label.config(text=f"Total items: {checklist.size()}")




#doesn't work proberly