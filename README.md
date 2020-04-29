# image-drop
Web app for analyse video files with spreading and evaporating drops.
Finds irregular contour, computes FFT, fractal dimesion, drop area.

### Generate image
docker login
docker image build -t konstgav/image-drop:0.1 .
dicker push konstgav/image-drop:0.1

### Run image
sudo xhost +local:
docker container run -it --rm -v my-vol:/home/ -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix konstgav/image-drop:0.1

## Поля файлов \*.param
    "filename": путь к видеофайлу
    "dirname": название видеофайла
    "frameStep": шаг по кадрам при обработки (1 - каждый кард, 10 - каждый 10-ый кадр)
    "startFrame": начальный кадр для обработки
    "finalFrame": конечный кадр для обработки
    "isSaveFrames": сохранять ли кадры в отдельную папку (true/false)
    "needToShowContour": нужно ли показывать контуры при обработке (true/false)
    "xmin": номер минимального пискеля по горизонтали для области обработки
    "xmax": номер максимального пикселя по горизонтали для области обработки
    "ymin": номер минимального пискеля по вертикали для области обработки
    "ymax": номер максимльного пискеля по вертикали для области обработки
    "needToSaveAreas": нужно ли сохранять площади капли для каждого кадра в файл (true/false)
    "needToShowFFT": нужно ли показывать преобразование при обработке (true/false)
    "MaxFreq": максимальна частота для преобразования Фурье
    "pixelToCm": размер пикселя в сантиметрах
    "startFileNumFFT": номер начального кадра для осреднения преобразования Фурье  
    "NumPicFFT": количество кадров для осреднения преобразования Фурье