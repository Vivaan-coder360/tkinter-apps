import tkinter as tk
def change_text():
    user_input = text_box.get("1.0", tk.END)
    label.config(text=f"hello {user_input} not gonna lie it's a pretty cool name")
window = tk.Tk()
window.title("Enter your name")
window.geometry("600x400")
label = tk.Label(window, text="Enter your name", font=("Arial", 14))
label.pack(pady=20)
button = tk.Button(window, text="Click me to enter your name", command=change_text)
button.pack()
text_box = tk.Text(height=5, width=40, font=("Arial", 12 ))
text_box.pack(pady=10)
window.mainloop()