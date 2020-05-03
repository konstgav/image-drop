FROM       python:3
LABEL      maintainer="Konstantin Gavrilov @konstgav"
ENV        LANG C.UTF-8
WORKDIR    /app
COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y make build-essential libfftw3-dev numdiff
RUN pip3 install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/flatironinstitute/finufft.git
RUN git clone https://github.com/konstgav/image-drop.git image-drop-web
WORKDIR /app/finufft
RUN make test
RUN make lib
RUN make python3
WORKDIR /app/image-drop-web
CMD [ "python3", "./app.py" ]