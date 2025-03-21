import tkinter as tk
import requests
from tkinter import messagebox

def fetch_weight():
    try:
        response = requests.get("http://localhost:5000/weight")
        weight = response.json().get("weight", "N/A")
        weight_label.config(text=f"Weight: {weight} kg")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weight: {e}")

def fetch_location():
    try:
        response = requests.get("http://localhost:5000/location")
        location = response.json().get("location", "N/A")
        location_label.config(text=f"Location: {location}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch location: {e}")

def send_alert():
    try:
        response = requests.post("http://localhost:5000/alert")
        status = response.json().get("status", "Failed")
        messagebox.showinfo("Alert", f"{status}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send alert: {e}")

# Create GUI window
root = tk.Tk()
root.title("Smart Shoe Dashboard")
root.geometry("400x300")

# Labels
weight_label = tk.Label(root, text="Weight: -- kg", font=("Arial", 14))
weight_label.pack(pady=10)

location_label = tk.Label(root, text="Location: --", font=("Arial", 14))
location_label.pack(pady=10)

# Buttons
tk.Button(root, text="Fetch Weight", command=fetch_weight, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Fetch Location", command=fetch_location, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Send Emergency Alert", command=send_alert, font=("Arial", 12), bg="red", fg="white").pack(pady=20)

# Run the GUI
root.mainloop()
