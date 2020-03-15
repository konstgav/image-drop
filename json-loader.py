import json 
import os

def SaveVideoParamsToJson():
    videoParams = {}
    videoParams['filename'] = './images/fractal1.MOV'
    videoParams['dirname'] = os.path.splitext(os.path.basename(videoParams['filename']))[0]
    videoParams['frameStep'] = 1
    videoParams['startFrame'] = 600
    videoParams['finalFrame'] = 900
    videoParams['isSaveFrames'] = False
    videoParams['needToShowCountour'] = True
    videoParams['xmin'] = 1400
    videoParams['xmax'] = 2160
    videoParams['ymin'] = 640
    videoParams['ymax'] = 1500
    videoParams['needToSaveAreas'] = True
    videoParams['needToShowFFT'] = False
    videoParams['MaxFreq'] = 300
    videoParams['pixelToCm'] = 6./263
    
    with open(videoParams['dirname']+'.param', 'w') as outfile:
        json.dump(videoParams, outfile, indent = 4)
    return 1

def ReadVideoParamsFromFile():
    with open('fractal1.param', 'r')  as json_file:
        videoParams = json.load(json_file)
    print(videoParams)
    return 1

ReadVideoParamsFromFile()