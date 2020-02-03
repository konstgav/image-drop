import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageFilter, ImageTk
import os

class Pic:
    def GetFilename(self):
        filename = fd.askopenfilename(title='open')
        return filename

    def OpenImage(self):
        filename = self.GetFilename()
        self._img = Image.open(filename)
        size = (350, 350)
        self._img.thumbnail(size)
        imgTk = ImageTk.PhotoImage(self._img)
        canvas.create_image(0,0,anchor=tk.NW, image=imgTk)
        canvas.image = imgTk

    def SaveImage(self):
        filename = fd.asksaveasfile(title='save', mode='w', defaultextension=".png")
        if filename:
            self._img.save(os.path.abspath(filename.name))

    def ProcessBLUR(self):
        self._img = self._img.filter(ImageFilter.BLUR)
        imgTk = ImageTk.PhotoImage(self._img)
        canvas.create_image(0,0,anchor=tk.NW, image=imgTk)
        canvas.image = imgTk

    def ProcessCONTOUR(self):
        self._img = self._img.filter(ImageFilter.CONTOUR)
        imgTk = ImageTk.PhotoImage(self._img)
        canvas.create_image(0,0,anchor=tk.NW, image=imgTk)
        canvas.image = imgTk

root = tk.Tk()
root.geometry("400x400")
root.wm_title("Image processor")
img = Pic()

mainMenu = tk.Menu(root) 
root.config(menu=mainMenu) 
 
fileMenu = tk.Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="Open image", command = img.OpenImage)
fileMenu.add_command(label="Save image", command = img.SaveImage)
fileMenu.add_command(label="Open video")
fileMenu.add_command(label="Quit", command=root.quit)
 
helpMenu = tk.Menu(mainMenu, tearoff=0)
helpMenu.add_command(label="BLUR", command = img.ProcessBLUR)
helpMenu.add_command(label="CONTOUR", command = img.ProcessCONTOUR)
 
mainMenu.add_cascade(label="File", menu=fileMenu)
mainMenu.add_cascade(label="Tools", menu=helpMenu)

canvas = tk.Canvas(root,  width=360, height=360)
canvas.pack() 

root.mainloop()