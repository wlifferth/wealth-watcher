FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /wealth-watcher
WORKDIR /wealth-watcher

RUN pip install -r requirements.txt 
ENTRYPOINT ["python"]
CMD ["main.py"]

