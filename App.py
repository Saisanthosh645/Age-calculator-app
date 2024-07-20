import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        birthYear = int(year_entry.get())
        birthMonth = int(month_entry.get())
        birthDay = int(day_entry.get())
        birthday = date(birthYear, birthMonth, birthDay)

        today = date.today()
        day_check = ((today.month, today.day) < (birthday.month, birthday.day))
        year_diff = today.year - birthday.year
        age_in_years = year_diff - day_check
        remaining_months = abs(today.month - birthday.month)
        remaining_days = abs(today.day - birthday.day)
        
        result_label.config(text=f"Age: {age_in_years} Years, {remaining_months} Months, and {remaining_days} Days")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid date values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Age Calculator by Sai")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Create and place the labels, entries, and button
tk.Label(root, text="Enter Birth Year:", bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=10, sticky='e')
year_entry = tk.Entry(root)
year_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Birth Month:", bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=10, sticky='e')
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Birth Day:", bg='#f0f0f0').grid(row=2, column=0, padx=10, pady=10, sticky='e')
day_entry = tk.Entry(root)
day_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", bg='#f0f0f0', font=('Arial', 12))
result_label.grid(row=4, column=0, columnspan=2)

# Footer
footer = tk.Label(root, text="Created by: linkedin.com/in/raminisaisanthosh/", bg='#f0f0f0', font=('Arial', 10, 'italic'))
footer.grid(row=5, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
