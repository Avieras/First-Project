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
from tkinter import messagebox

checklist = []
checklist2 = []
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

        
# Function to add a number to the selected item in checklist 2
def add_number():
    try:
        selected = checklist2.curselection()  # Get the selected item index
        if selected:
            index = selected[0]
            entered_value = int(entry_number.get())  # Get the number from the entry field
            current_number = int(checklist2.get(index))  # Get the current number from checklist 2
            updated_number = current_number + entered_value  # Calculate the updated number
            checklist2.delete(index)  # Delete the current item from checklist 2
            checklist2.insert(index, updated_number)  # Insert the updated number at the same index
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")  # Show error for invalid input

# Function to subtract a number from the selected item in checklist 2
def subtract_number():
    try:
        selected = checklist2.curselection()  # Get the selected item index
        if selected:
            index = selected[0]
            entered_value = int(entry_number.get())  # Get the number from the entry field
            current_number = int(checklist2.get(index))  # Get the current number from checklist 2
            updated_number = current_number - entered_value  # Calculate the updated number
            if updated_number < 0:
                updated_number = 0  # Ensure the number doesn't go below zero
            checklist2.delete(index)  # Delete the current item from checklist 2
            checklist2.insert(index, updated_number)  # Insert the updated number at the same index
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")  # Show error for invalid input

# Function to add a new number to checklist 2
def add_item_number():
    try:
        entered_value = int(entry_number.get())  # Get the number from the entry field
        checklist2.insert(tk.END, entered_value)  # Insert the entered number at the end of checklist 2
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")  # Show error for invalid input


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
label = tk.Label(window, text="Enter wished Item:")  # Create a label for instructions
label.pack()  # Display the label in the window

entry = tk.Entry(window)  # Create an entry field for user input
entry.pack()  # Display the entry field in the window

#Design of a button
button = ttk.Button(window, text="Search", style="Custom.TButton")  # Create a styled button
button.pack()  # Display the button in the window
style = ttk.Style()
style.configure("Custom.TButton", foreground="black", font=("Arial", 12))  # Configure the style of the button
#_______________________

#Number box
frame = tk.Frame(window)  # Create a frame for layout management
frame.pack(padx=10, pady=10)  # Display the frame with padding

checklist2 = tk.Listbox(frame, width=5)  # Create a listbox for displaying numbers
checklist2.pack(side=tk.LEFT, fill=tk.Y)  # Display the listbox within the frame

number_frame = tk.Frame(window)  # Create a frame for number-related elements
number_frame.pack(padx=10, pady=20, side="bottom")  # Display the frame with padding at the bottom

number_label = tk.Label(number_frame, text="Number:")  # Create a label for number entry
number_label.pack()  # Display the label in the number frame

entry_number = tk.Entry(number_frame, width=10)  # Create an entry field for number input
entry_number.pack()  # Display the entry field in the number frame

#Checklist
checklist = tk.Listbox(frame, width=50)  # Create a listbox for displaying checklist items
checklist.pack(side=tk.LEFT, fill=tk.Y)  # Display the listbox within the frame

#Scrollbar for checklist
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)  # Create a vertical scrollbar for the checklist
scrollbar.config(command=checklist.yview)  # Connect scrollbar to checklist
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Display the scrollbar next to the checklist
checklist.config(yscrollcommand=scrollbar.set)  # Configure the checklist to use the scrollbar

#Insert field
entry = tk.Entry(window, width=30)  # Create an entry field for additional input
entry.pack()  # Display the entry field in the window

#Buttons
add_button = tk.Button(window, text="Add", command=add_item)  # Create an 'Add' button with a command
add_button.pack()  # Display the 'Add' button in the window

remove_button = tk.Button(window, text="Remove", command=remove_item)  # Create a 'Remove' button with a command
remove_button.pack()  # Display the 'Remove' button in the window

add_number_item = tk.Button(number_frame,text="Number",command=add_item_number)
add_number_item.pack()

add_number_button = tk.Button(number_frame, text="Add", command=add_number)  # Create an 'Add' button for numbers
add_number_button.pack()  # Display the 'Add' button in the number frame

subtract_number_button = tk.Button(number_frame, text="Subtract", command=subtract_number)  # Create a 'Subtract' button
subtract_number_button.pack()  # Display the 'Subtract' button in the number frame

#Counter of total items
count_label = tk.Label(window, text="Total items: 0")  # Create a label for total items count
count_label.pack()  # Display the label in the window

window.mainloop()  # Start the GUI event loop