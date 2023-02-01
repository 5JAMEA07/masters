import tkinter as tk


def calculate_caloric_need():
    # Get the values from the input fields
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = float(age_entry.get())
    gender = gender_var.get()
    activity_level = activity_var.get()

    # Calculate the BMR (Basal Metabolic Rate)
    if gender == "Male":
        bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    else:
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

    # Multiply the BMR by the appropriate activity factor
    if activity_level == "Sedentary":
        caloric_need = bmr * 1.2
    elif activity_level == "Lightly Active":
        caloric_need = bmr * 1.375
    elif activity_level == "Moderately Active":
        caloric_need = bmr * 1.55
    elif activity_level == "Very Active":
        caloric_need = bmr * 1.725
    else:
        caloric_need = bmr * 1.9

    # Display the result
    result_label.config(text=f"Your daily caloric need is {caloric_need:.2f} calories.", font=("Helvetica", 14))


# Create the main window
root = tk.Tk()
root.title("Caloric Need Calculator")

# Create the input fields
weight_label = tk.Label(root, text="Weight (kg):", font=("Helvetica", 14))
weight_entry = tk.Entry(root, font=("Helvetica", 14))
height_label = tk.Label(root, text="Height (cm):", font=("Helvetica", 14))
height_entry = tk.Entry(root, font=("Helvetica", 14))
age_label = tk.Label(root, text="Age (years):", font=("Helvetica", 14))
age_entry = tk.Entry(root, font=("Helvetica", 14))

# Create the gender options
gender_label = tk.Label(root, text="Gender:", font=("Helvetica", 14))
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", font=("Helvetica", 14))
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", font=("Helvetica", 14))

# Create the activity level options
activity_label = tk.Label(root, text="Activity Level:", font=("Helvetica", 14))
activity_var = tk.StringVar()
activity_var.set("Sedentary")
activity_menu = tk.OptionMenu(root, activity_var, "Sedentary", "Lightly Active", "Moderately Active", "Very Active",
                              "Extremely Active")
activity_menu.config(font=("Helvetica", 14), width=20, bg="white", activebackground="white")

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_caloric_need, font=("Helvetica", 14),
                             bg="#00BFFF", fg="white", activebackground="#00BFFF", activeforeground="white",
                             relief="flat", bd=0)
calculate_button.config(height=2, width=20)

# Create the result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#E0FFFF")
result_label.config(width=40, height=3, relief="solid", bd=1)

# Position the widgets using grid
weight_label.grid(row=0, column=0, sticky="W")
weight_entry.grid(row=0, column=1, sticky="W")
height_label.grid(row=1, column=0, sticky="W")
height_entry.grid(row=1, column=1, sticky="W")
age_label.grid(row=2, column=0, sticky="W")
age_entry.grid(row=2, column=1, sticky="W")
gender_label.grid(row=3, column=0, sticky="W")
male_radio.grid(row=3, column=1, sticky="W")
female_radio.grid(row=3, column=2, sticky="W")
activity_label.grid(row=4, column=0, sticky="W")
activity_menu.grid(row=4, column=1, sticky="W")
calculate_button.grid(row=5, column=0, columnspan=3, pady=10)
result_label.grid(row=6, column=0, columnspan=3, pady=10)

root.config(bg="#E0FFFF")

# Add padding to all widgets
for i in range(7):
    root.columnconfigure(i, pad=10)
for i in range(7):
    root.rowconfigure(i, pad=10)

# Update font and color for labels
weight_label.config(font=("Helvetica", 16), fg="black", bg="#E0FFFF")
height_label.config(font=("Helvetica", 16), fg="black", bg="#E0FFFF")
age_label.config(font=("Helvetica", 16), fg="black", bg="#E0FFFF")
gender_label.config(font=("Helvetica", 16), fg="black", bg="#E0FFFF")
activity_label.config(font=("Helvetica", 16), fg="black", bg="#E0FFFF")

# Update font and color for entries
weight_entry.config(font=("Helvetica", 16), bg="white", fg="black")
height_entry.config(font=("Helvetica", 16), bg="white", fg="black")
age_entry.config(font=("Helvetica", 16), bg="white", fg="black")

# Update font and color for radio buttons
male_radio.config(font=("Helvetica", 16), bg="#E0FFFF", fg="black", selectcolor="#E0FFFF", activebackground="#E0FFFF")
female_radio.config(font=("Helvetica", 16), bg="#E0FFFF", fg="black", selectcolor="#E0FFFF", activebackground="#E0FFFF")

# Update font and color for option menu
activity_menu.config(font=("Helvetica", 16), width=20, bg="white", fg="black", activebackground="white")

# Update font and color for calculate button
calculate_button.config(font=("Helvetica", 16), bg="#00BFFF", fg="white", activebackground="#00BFFF",
                        activeforeground="white", relief="flat", bd=0)

# Update font and color for result label
result_label.config(font=("Helvetica", 16), bg="#E0FFFF", fg="black", width=40, height=3, relief="solid", bd=1)

# Start the main event loop
root.mainloop()