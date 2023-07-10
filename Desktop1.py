import tkinter as tk

def button_clicked():
    print("Button clicked!")

window = tk.Tk()
window.title("Simple App")

button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack(padx=10, pady=10)

window.mainloop()