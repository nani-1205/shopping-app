FROM registry.access.redhat.com/ubi9/ubi-init:latest

# Install necessary packages
RUN microdnf update -y && \
    microdnf install -y mysql-devel gcc python3-devel && \
    microdnf clean all

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose the port
EXPOSE 5000

# Set the command to run the application
CMD ["python3", "-m", "flask", "run"]