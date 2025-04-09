#Docker file 

# Base image
FROM python:latest

LABEL Creator="Abideen Bello"

RUN apk add curl

# Set the working directory
WORKDIR /app

# Copy game files into the container
COPY . /app

ADD https://file.downloadapk1.com/simcity-buildit_latest%20file%20simcitybuilditapk.com.apk .

# What port to expose to docker
EXPOSE 8000

CMD ["python", "main.py"]




