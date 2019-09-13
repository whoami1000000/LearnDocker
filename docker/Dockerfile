FROM python:3.7-buster

WORKDIR app

COPY . /app

RUN ls

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]