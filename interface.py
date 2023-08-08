import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry("410x300")  # Size of the window
my_w.title('www.hybrid_encrypted.com')

# Custom colors
bg_color = '#F8F8F8'
button_color = '#4C8BF5'
label_color = '#333333'

my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='DKV Hybrid Encryption App\nUpload Files & Display', width=30, font=my_font1, bg=bg_color, fg='magenta')
l1.grid(row=1, column=1, columnspan=6)

b1 = tk.Button(my_w, text='Upload Files', width=20, command=lambda: upload_file(), bg=button_color, fg='white')
b1.grid(row=2, column=3, columnspan=1)

b2 = tk.Button(my_w, text='Encrypt', width=10, command=lambda: encrypt_files(), bg=button_color, fg='white')
b2.grid(row=3, column=2)

b3 = tk.Button(my_w, text='Decrypt', width=10, command=lambda: decrypt_files(), bg=button_color, fg='white')
b3.grid(row=3, column=4)

def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]  # type of files to select
    filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
    col = 3  # start from column 1
    row = 6  # start from row 3
    for f in filename:
        img = Image.open(f)  # read the image file
        img = img.resize((100, 100))  # new width & height
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(my_w, bg=bg_color)
        e1.grid(row=row, column=col)
        e1.image = img  # keep a reference! by attaching it to a widget attribute
        e1['image'] = img  # Show Image
        if col == 3:  # start new line after third column
            row = row + 1  # start with next row
            col = 1  # start with first column
        else:  # within the same row
            col = col + 1  # increase to next column

def encrypt_files():
    # Perform encryption logic here
    pass

def decrypt_files():
    # Perform decryption logic here
    pass

my_w.configure(bg=bg_color)  # Set background color for the window
my_w.mainloop()  # Keep the window open
