FROM ubuntu
WORKDIR /app

COPY . /app
RUN apk add build-base
RUN apk add --no-cache --update python3 && \
    pip install --upgrade pip setuptools && \
	pip install --upgrade pip
	
FROM tensorflow/tensorflow
WORKDIR /Arabic_NLP

COPY . /Arabic_NLP  


RUN pip install -r requirements.txt

EXPOSE 4000

ENTRYPOINT  ["python"]

CMD ["app.py"]
