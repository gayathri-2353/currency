import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to fetch real-time exchange rate
def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()

        if target_currency not in data['rates']:
            raise ValueError(f"{target_currency} not found in API response.")
        
        return data['rates'][target_currency]
    except Exception as e:
        messagebox.showerror("API Error", f"Failed to get exchange rate:\n{e}")
        return None

# Function to handle conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        base_currency = from_currency.get()
        target_currency = to_currency.get()

        if base_currency == "" or target_currency == "":
            messagebox.showwarning("Currency Missing", "Please select both currencies.")
            return

        rate = get_exchange_rate(base_currency, target_currency)
        if rate:
            converted = amount * rate
            result_label.config(text=f"{amount:.2f} {base_currency} = {converted:.2f} {target_currency}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Currency Converter Calculator")
root.geometry("420x350")
root.configure(bg="#f7f7f7")

# Header
tk.Label(root, text="💱 Currency Converter Calculator", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=15)

# Amount
tk.Label(root, text="Enter Amount:", font=("Arial", 12), bg="#f7f7f7").pack()
amount_entry = tk.Entry(root, font=("Arial", 12), justify='center')
amount_entry.pack(pady=8)

# Currency selection frame
frame = tk.Frame(root, bg="#f7f7f7")
frame.pack(pady=10)

currencies = ["USD", "EUR", "INR", "JPY", "GBP", "CAD", "AUD", "CHF", "CNY", "SGD"]

from_currency = ttk.Combobox(frame, values=currencies, font=("Arial", 10), width=10)
from_currency.set("USD")
from_currency.grid(row=0, column=0, padx=10)

to_currency = ttk.Combobox(frame, values=currencies, font=("Arial", 10), width=10)
to_currency.set("INR")
to_currency.grid(row=0, column=1, padx=10)

# Convert Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=convert_currency)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f7f7f7")
result_label.pack(pady=20)

# Footer
tk.Label(root, text="Powered by exchangerate-api.com", font=("Arial", 8), bg="#f7f7f7", fg="gray").pack(side="bottom", pady=5)

# Start the GUI loop
root.mainloop()