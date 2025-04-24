#Docker file 

# Base image
FROM python:latest

LABEL Creator="Abideen Bello"

# Set the working directory
WORKDIR /app

# Copy game files into the container
COPY . /app

CMD ["python", "main.py"]




