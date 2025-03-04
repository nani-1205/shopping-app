WORKDIR /app

RUN apk update &&     apk add --no-cache mysql-client gcc musl-dev python3-dev libffi-dev openssl-dev pkgconfig

ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/mysql"

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["python3", "-m", "flask", "run"]
```