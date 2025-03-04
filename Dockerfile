FROM registry.access.redhat.com/ubi9/ubi-minimal:latest  #This line MUST be first, no spaces before

RUN microdnf update -y && \
    microdnf install -y mysql-devel gcc python3-devel && \
    microdnf clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["python3", "-m", "flask", "run"]