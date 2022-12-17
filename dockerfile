FROM ubuntu
WORKDIR /app

COPY . /app
RUN apk add build-base
RUN apk add --no-cache --update python3 && \
    pip install --upgrade pip setuptools && \
	pip install --upgrade pip
	
FROM tensorflow/tensorflow
WORKDIR /app

COPY . /app  


RUN pip install -r requirements.txt

EXPOSE 4000

ENTRYPOINT  ["python"]

CMD ["app.py"]
