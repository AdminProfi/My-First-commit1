'''import cv2
from tkinter import *
from tkinter import Button
from tkinter import filedialog
root = Tk()
root.title('Scaner QR code')
root.geometry("250x250") 
root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text =file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
 
open_button = Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
 
root.mainloop()'''
'''from PIL import image 
from tkinter import Button
from tkinter import filedialog
from tkinter import *
root=TK()
root=title('Saner QR code')
roo.geometry('250:250')
root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
def open_file():
    filepath= filedialog.askopenfilename()
    if filepath!='PNG'or'Jpeg':
        with open(filepath)'''
'''import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")''' 
  