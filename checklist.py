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
    #Display certain information and picture from website


import tkinter as tk
from tkinter import ttk

checklist = []
current_number = 0

# Function to add an item to the checklist
def add_item():
    item = entry.get()  # Get the text from the entry field
    checklist.insert(tk.END, item)  # Insert the item to the checklist
    entry.delete(0, tk.END)  # Clear the entry field
    update_count()  # Update the count of items

# Function to remove an item from the checklist
def remove_item():
    selected = checklist.curselection()  # Get the selected item(s)
    if selected:
        index = selected[0]
        checklist.delete(index)  # Remove the selected item from the checklist
        update_count()  # Update the count of items

# Function to add a number to the total count
def add_number():
    global current_number
    entered_value = number_box.get()
    try:
        current_number += int(entered_value)  # Add the entered value to the total count
        check_box.delete(0, tk.END)  # Clear the box
        check_box.insert(tk.END, str(current_number))  # Display the updated total count
    except ValueError:
        pass

# Function to subtract a number from the total count
def subtract_number():
    global current_number
    entered_value = number_box.get()
    try:
        current_number -= int(entered_value)  # Subtract the entered value from the total count
        check_box.delete(0, tk.END)  # Clear the box
        check_box.insert(tk.END, str(current_number))  # Display the updated total count
    except ValueError:
        pass

# Function to update the count label with the total number of items
def update_count():
    count_label.config(text=f"Total items: {checklist.size()}")

    

#Creates the main window
window = tk.Tk()
window.title("Checklist")

#Window size
window.geometry("500x500")


#Phase 2

# Label and entry for adding items
label = tk.Label(window, text="Enter wished Item:")
label.pack()

entry = tk.Entry(window)
entry.pack()

#Design of a button
button = ttk.Button(window, text="Search", style="Custom.TButton")
button.pack()
style = ttk.Style()
style.configure("Custom.TButton", foreground="black", font=("Arial", 12))
#_______________________



#Number box
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

number_frame = tk.Frame(window)
number_frame.pack(padx=10, pady=20,side="bottom")

number_label = tk.Label(number_frame, text="Number:")
number_label.pack()

number_box = tk.Entry(number_frame, width=10)
number_box.pack()

check_box = tk.Listbox(frame, width=5)
check_box.pack(side=tk.LEFT, fill=tk.Y)


#Checklist
checklist = tk.Listbox(frame, width=20)
checklist.pack(side=tk.LEFT, fill=tk.Y)

#Scrollbar for checklist
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=checklist.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
checklist.config(yscrollcommand=scrollbar.set)

#Insert field
entry = tk.Entry(window, width=30)
entry.pack()



#Buttons
add_button = tk.Button(window, text="Add", command=add_item)
add_button.pack()

remove_button = tk.Button(window, text="Remove", command=remove_item)
remove_button.pack()


add_number_button = tk.Button(number_frame, text="Add", command=add_number)
add_number_button.pack()

subtract_number_button = tk.Button(number_frame, text="Subtract", command=subtract_number)
subtract_number_button.pack()


#Counter of total items
count_label = tk.Label(window, text="Total items: 0")
count_label.pack()


window.mainloop()
