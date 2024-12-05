FROM python:3.10.15-slim-buster

WORKDIR /app

COPY . /app

RUN apt update -y && apt install awscli -y

RUN app-get update && apt-get install ffmpeg libsm6 librext6 unzip -y  && pip install -r requirements.txt

CMD [ "python3" , "app.py" ]


