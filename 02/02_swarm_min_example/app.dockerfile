FROM python:3.7

ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install Flask==1.1.2
RUN pip install requests

COPY ./main.py /app/main.py

CMD bash -c "FLASK_ENV=development FLASK_APP=main flask run --host=0.0.0.0 --port 8000"
