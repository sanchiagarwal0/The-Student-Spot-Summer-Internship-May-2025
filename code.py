import tkinter as tk
from tkinter import messagebox
import csv
import os

def save_contact():
    try:
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        
        if not name or not phone:
            messagebox.showwarning("Warning", "Name and Phone are required!")
            return
            
        # Create the file if it doesn't exist
        file_exists = os.path.isfile('contacts.csv')
        
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Phone"])  # Write header if new file
            writer.writerow([name, phone])
            
        messagebox.showinfo("Success", "Contact saved!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        
    except PermissionError:
        messagebox.showerror("Error", "Cannot write to file. Check file permissions.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Mini Contact Book")

# Make the window a bit larger
root.geometry("300x150")

# Create and place widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky='e')

name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_entry = tk.Entry(root, width=25)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

save_btn = tk.Button(root, text="Save Contact", command=save_contact)
save_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()