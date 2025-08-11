import qr 
import tkinter as tk
from PIL import Image, ImageTk


def generate_qr():
    qr.createQr("white", "black", inp.get())

    img = Image.open("qr.png")
    img = img.resize((200, 150))
    photo = ImageTk.PhotoImage(img)

    label3.config(image=photo)
    label3.image = photo 
    
    label4 = tk.Label(root, text="Qr Saved Successfully", font=("Arial", 14), fg="#333333", bg="white")
    label4.place(x=100, y=460)


root = tk.Tk()
root.title("QR Generator")
root.geometry("400x500")
root.configure(bg="white")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Qr Generator",
    font=("Arial", 20, "bold"),
    fg="#333333",
    bg="white",
    padx=20,
)
label.pack(pady=20)

label2 = tk.Label(
    root, text="Enter the link", font=("Arial", 14), fg="#333333", bg="white"
)
label2.place(x=40, y=120)

inp = tk.Entry(root, font=("Arial", 14), width=30, border=2, bg="white")
inp.place(x=40, y=150)

btn = tk.Button(
    root,
    text="Generate",
    font=("Arial", 14),
    command=generate_qr,
    fg="white",
    bg="#F18F01",
    cursor="hand2",
    highlightbackground="#24613b",
    relief="raised",
)
btn.place(x=40, y=200, width=334)

img = Image.open("qr.png")
img = img.resize((200, 150))
photo = ImageTk.PhotoImage(img)

label3 = tk.Label(root, image=photo)
label3.place(x=100, y=300)

root.mainloop()
