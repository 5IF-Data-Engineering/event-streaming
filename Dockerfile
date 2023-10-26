FROM python:3.8.14

RUN mkdir -p /app
WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
