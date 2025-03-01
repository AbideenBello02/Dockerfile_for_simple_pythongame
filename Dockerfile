#Docker file 

# Base image
FROM python:3.10


# Set the working directory
WORKDIR /app


# Copy game files into the container
COPY . /app
		

# What port to expose to 
EXPOSE 8000



