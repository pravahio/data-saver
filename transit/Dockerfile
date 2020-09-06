FROM python:3.7

RUN pip install pravah protobuf

WORKDIR /usr/src/pravah

COPY transit.py .
COPY ../db.py .

CMD ["python3"]