import os

class filepath:
    def __init__(self, workdir, user, videofilename):
        self.__workdir = workdir
        self.__user = user
        self.__case = os.path.splitext(videofilename)[0]
        self.__case_dir = os.path.join(self.__workdir, self.__user, self.__case)
        self.__videofilename = videofilename
    
    def set_videofilename(self, videofilename):
        self.__case = os.path.splitext(videofilename)[0]
        self.__case_dir = os.path.join(self.__workdir, self.__user, self.__case)
        self.__videofilename = videofilename

    def to_video_file(self, filename):
        path = os.path.join(self.__case_dir, 'video')
        os.makedirs(path, exist_ok=True)
        return os.path.join(path, filename)

    def to_images_dir(self):
        path = os.path.join(self.__case_dir, 'images')
        os.makedirs(path, exist_ok=True)
        return path

    def to_contours_dir(self):
        path = os.path.join(self.__case_dir, 'contours')
        os.makedirs(path, exist_ok=True)
        return path

    def to_ffts_dir(self):
        path = os.path.join(self.__case_dir, 'ffts')
        os.makedirs(path, exist_ok=True)
        return path

    def to_results_dir(self):
        path = os.path.join(self.__case_dir, 'results')
        os.makedirs(path, exist_ok=True)
        return path

    def to_case(self):
        return self.__case
    
    def to_param_file(self):
        return os.path.join(self.__case_dir, 'video', self.__case + '.param')
    
    def to_videofile(self):
        return os.path.join(self.__case_dir, 'video', self.__videofilename)