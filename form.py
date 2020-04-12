import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import video
import json

class ControllerVideo:

    def OpenVideo(self):
        filename = fd.askopenfilename(title='Open video')
        dirname = os.path.splitext(os.path.basename(filename))[0]
        json_filename = dirname + '.param'
        # Reading video parameters from json file
        try:
            with open(json_filename, 'r')  as json_file:
                videoParams = json.load(json_file)
                canvas.delete("all")
                canvas.create_text(200,200,text=json.dumps(videoParams, indent = 4))
                self._video = video.Video(videoParams)
        except OSError:
            print ('Error: cannot read videoparams from json-file')
            messagebox.showwarning("Error", "Сannot open file %s with videoparams" % json_filename)

    def SaveImage(self):
        filename = fd.asksaveasfile(title='save', mode='w', defaultextension=".png")
   
    def ProcessVideo(self):
        self._video.Run()
    
    def AverageFFT(self):
        self._video.AverageNUFFT()

root = tk.Tk()
root.geometry("400x400")
root.wm_title("Image drop processor")
controllerVideo = ControllerVideo()

mainMenu = tk.Menu(root) 
root.config(menu=mainMenu) 
 
fileMenu = tk.Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="Open video", command = controllerVideo.OpenVideo)
fileMenu.add_command(label="Quit", command = root.quit)
 
toolsMenu = tk.Menu(mainMenu, tearoff=0)
toolsMenu.add_command(label="Process video", command = controllerVideo.ProcessVideo)
toolsMenu.add_command(label="Average FFT", command = controllerVideo.AverageFFT)

mainMenu.add_cascade(label = "File", menu = fileMenu)
mainMenu.add_cascade(label = "Tools", menu = toolsMenu)

canvas = tk.Canvas(root,  width=400, height=400)
canvas.pack() 

root.mainloop()