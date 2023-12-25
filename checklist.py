#Phase 1 - UI
    #Create a UI for the checklist, as exe  | 1/2 done
    #-check boxes, entry field, search field, search button, numbers field
    #Create the checklist,entry possebility

#Phase 2 - LTS
    #Save entry for long term use, but make it edable
    #Create a search function

#Phase 3 - Data Scraping
    #Create a link to desired website
    #Pull certain data from website
    #display certain information and picture from website


import tkinter as tk
from tkinter import ttk

checklist = []
current_number = 0

def add_item():
    item = entry.get()
    checklist.insert(tk.END, item)
    entry.delete(0, tk.END)
    update_count()

def remove_item():
    selected = checklist.curselection()
    if selected:
        index = selected[0]
        checklist.delete(index)
        update_count()

#Adds/Subtracts entered Number into the box next to checklist
def add_number():
    global current_number
    entered_value = number_box.get()
    try:
        current_number += int(entered_value)
        check_box.delete(0, tk.END)
        check_box.insert(tk.END, str(current_number))
    except ValueError:
        pass
# ^
def subtract_number():
    global current_number
    entered_value = number_box.get()
    try:
        current_number -= int(entered_value)
        check_box.delete(0, tk.END)
        check_box.insert(tk.END, str(current_number))
    except ValueError:
        pass


def update_count():
    count_label.config(text=f"Total items: {checklist.size()}")

#name of window
window = tk.Tk()
window.title("Checklist")

#size of window
window.geometry("500x500")


#Phase 2
label = tk.Label(window, text="Enter wished Item:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = ttk.Button(window, text="Search", style="Custom.TButton")
button.pack()
#Design of a button
style = ttk.Style()
style.configure("Custom.TButton", foreground="black", font=("Arial", 12))
#_______________________



frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

#number box
number_frame = tk.Frame(window)
number_frame.pack(padx=10, pady=20,side="bottom")

number_label = tk.Label(number_frame, text="Number:")
number_label.pack()

number_box = tk.Entry(number_frame, width=10)
number_box.pack()
number_box.insert(tk.END, str(current_number)) 

#Amount list
check_box = tk.Listbox(frame, width=5)
check_box.pack(side=tk.LEFT, fill=tk.Y)


#checklist
checklist = tk.Listbox(frame, width=20)
checklist.pack(side=tk.LEFT, fill=tk.Y)

#scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=checklist.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
checklist.config(yscrollcommand=scrollbar.set)

#insert field
entry = tk.Entry(window, width=30)
entry.pack()



#buttons
add_button = tk.Button(window, text="Add", command=add_item)
add_button.pack()

remove_button = tk.Button(window, text="Remove", command=remove_item)
remove_button.pack()


add_number_button = tk.Button(number_frame, text="Add", command=add_number)
add_number_button.pack()

subtract_number_button = tk.Button(number_frame, text="Subtract", command=subtract_number)
subtract_number_button.pack()


#counter of total items
count_label = tk.Label(window, text="Total items: 0")
count_label.pack()


window.mainloop()
