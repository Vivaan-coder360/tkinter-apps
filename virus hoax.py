import tkinter as tk
def change_text():
    label.config(text = "haha got your password idiot", font = ("Arial, 14"))
window =  tk.Tk()
window.geometry("600x400")
window.title("virus_hoax")
label = tk.Label(window, text="Enter your password immeadetly!!!! you have been hacked I can fix it", font =("Arial", 14))
label.pack(pady = 20)
text = tk.Text(window, width=40, height = 1, font=("Arial", 12))
text.pack(pady = 20)
button = tk.Button(window, text="Submit_password", command=change_text)
button.pack(pady = 20)
window.mainloop()