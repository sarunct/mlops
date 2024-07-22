FROM python:3.12.4-alpine3.20

LABEL Maintainer="Arun"

WORKDIR /usr/app/src

RUN pip3 install flask

COPY ./ml.py ./

EXPOSE 5000

CMD ["python3", "./ml.py"]

