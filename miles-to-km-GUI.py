from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50, bg="#e6e6e6")

# Center the window
window_width = 400
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Entry for miles with styling
miles_input = Entry(width=10, font=("Arial", 14), justify="center")
miles_input.grid(column=1, row=0, pady=10)
miles_input.insert(0, "0")

# Labels with styling
miles_label = Label(text="Miles", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333333")
miles_label.grid(column=2, row=0, padx=10)

is_equal_label = Label(text="is equal to", font=("Arial", 12), bg="#e6e6e6", fg="#333333")
is_equal_label.grid(column=0, row=1, pady=10)

result_label = Label(text="0", font=("Arial", 14, "bold"), bg="#ffffff", fg="#007acc", width=10, relief="sunken")
result_label.grid(column=1, row=1, pady=10)

km_label = Label(text="Km", font=("Arial", 12, "bold"), bg="#e6e6e6", fg="#333333")
km_label.grid(column=2, row=1, padx=10)

# Calculate button with styling
calculate_button = Button(
    text="Calculate", 
    command=miles_to_km, 
    font=("Arial", 12, "bold"),
    bg="#007acc",
    fg="white",
    activebackground="#005999",
    relief="raised",
    cursor="hand2",
    width=10,
    height=1
)
calculate_button.grid(column=1, row=2, pady=20)

window.mainloop()