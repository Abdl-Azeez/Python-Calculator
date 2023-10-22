import tkinter as tk

def click_button(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x400")
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

screen = tk.StringVar()
entry = tk.Entry(frame, textvar=screen, font="lucida 20 bold", justify="right")
entry.pack(fill="both", expand=True)

button_frame = tk.Frame(frame)
button_frame.pack(expand=True, fill="both")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 0, 0

for button_text in buttons:
    button = tk.Button(
        button_frame,
        text=button_text,
        font="lucida 15 bold",
        width=4,
        height=2
    )
    button.grid(row=row, column=col, padx=10, pady=10)
    button.bind("<Button-1>", click_button)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
