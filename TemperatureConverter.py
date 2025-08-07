import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get().strip())  # Strip spaces and convert
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_result.config(text=f"Result: {round(celsius, 2)}\N{DEGREE CELSIUS}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create frame for entry and label
frm_entry = tk.Frame(master=window)

# Create entry widget for Fahrenheit input
ent_temperature = tk.Entry(master=frm_entry, width=10, font=("Arial", 12))
ent_temperature.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# Create label for Fahrenheit degree symbol
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}", font=("Arial", 12))
lbl_temp.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Create convert button
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
btn_convert.grid(row=0, column=1, padx=10, pady=10)

# Create label for Celsius result
lbl_result = tk.Label(master=window, text="Result: \N{DEGREE CELSIUS}", font=("Arial", 12))
lbl_result.grid(row=0, column=2, padx=10, pady=10)

# Arrange the entry frame
frm_entry.grid(row=0, column=0, padx=10, pady=10)

# Focus the input field when app starts
ent_temperature.focus()

# Bind the Enter key to trigger conversion
window.bind("<Return>", lambda event: fahrenheit_to_celsius())

# Start the main loop
window.mainloop()
