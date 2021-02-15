FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY *.py .

CMD bash -c "FLASK_ENV=development FLASK_APP=main flask run --host=0.0.0.0 --port 8000"
