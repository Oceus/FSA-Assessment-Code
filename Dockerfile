FROM python:3.10.6
MAINTAINER sapruitt
WORKDIR /home/sapruitt/Desktop/Enterprise/Docker
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "main.py", "RestAPI.py"]
