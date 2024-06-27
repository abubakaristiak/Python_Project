import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Define a refined color palette
COLOR_PRIMARY = "#3f51b5"  # Indigo
COLOR_SECONDARY = "#fbc02d"  # Yellow
COLOR_BACKGROUND = "#f0f0f0"  # Light gray

def calculate_lifetime():
    try:
        birth_date = datetime.strptime(entry.get(), "%Y-%m-%d")
        current_date = datetime.now()

        # Calculate total seconds, minutes, hours, days, months, and years lived
        delta = current_date - birth_date
        total_seconds = delta.total_seconds()
        total_minutes = total_seconds / 60
        total_hours = total_minutes / 60
        total_days = delta.days
        total_months = total_days / 30.436875  # Average days per month
        total_years = delta.days / 365.2425  # Average days per year

        # Calculate years, months, days, hours, minutes, and seconds
        age = relativedelta(current_date, birth_date)

        result = (
            f"You have been alive for:\n"
            f"{int(total_seconds):,} seconds,\n"
            f"{int(total_minutes):,} minutes,\n"
            f"{int(total_hours):,} hours,\n"
            f"{int(total_days):,} days,\n"
            f"{int(total_months):,} months, and\n"
            f"{int(total_years):,} years!\n\n"
            f"Or exactly {age.years} years, {age.months} months, {age.days} days, "
            f"{age.hours} hours, {age.minutes} minutes, and {age.seconds} seconds."
        )

        messagebox.showinfo("Lifetime Stats", result)
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format")


# Set up the main application window
root = tk.Tk()
root.title("Lifetime Calculator")

# Set window size and add padding
root.geometry("600x500")
root.configure(padx=20, pady=20, bg=COLOR_BACKGROUND)

# Create and place the widgets
label = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):", bg=COLOR_BACKGROUND, font=("Helvetica", 16, "bold"),
                 fg="#333333")
label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 14), width=30, bd=2, relief="solid")
entry.pack(pady=10)

button = tk.Button(root, text="Calculate Lifetime", command=calculate_lifetime, font=("Helvetica", 14, "bold"),
                   bg=COLOR_PRIMARY, fg="white", width=20)
button.pack(pady=20)


# Function to display Lifetime Stats
def show_lifetime_stats():
    # Placeholder for stats display, can be implemented based on requirements
    messagebox.showinfo("Lifetime Stats", "Lifetime Stats Display Placeholder")


stats_button = tk.Button(root, text="Show Lifetime Stats", command=show_lifetime_stats, font=("Helvetica", 14, "bold"),
                         bg=COLOR_SECONDARY, fg="white", width=20)
stats_button.pack(pady=20)

# Run the application
root.mainloop()
