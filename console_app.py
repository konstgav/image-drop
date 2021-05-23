from video import Video
import json
from filepath import filepath
import matplotlib.pyplot as plt

UPLOAD_FOLDER = "."
USER = 'konst'

def start_computations():
    filename = "IMG_0483.MOV"
    fpath = filepath(UPLOAD_FOLDER, USER)
    fpath.set_videofilename(filename)
    json_file = open(fpath.to_param_file(), 'r')
    videoParams = json.load(json_file)
    video = Video(videoParams, fpath)
    #video.Run()
    #video.AverageNUFFT()
    video.compute_fractal_dimension()
    json_file.close()

if __name__ == '__main__':
    start_computations()