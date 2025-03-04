FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN yum update -y && yum install -y mysql-devel gcc python3-devel

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["flask", "run"]