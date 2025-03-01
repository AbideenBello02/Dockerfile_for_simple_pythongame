#Docker file 

# Base image
FROM python:3.10


# Set the working directory
WORKDIR /app


# 3️⃣ Install system dependencies (Xvfb for GUI)
RUN apt-get update && apt-get install -y xvfb


# Copy game files into the container
COPY . /app


# 5️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt



# 6️⃣ Set the default command to run the game using a virtual display (for GUI support)
CMD ["xvfb-run", "python", "main.py"]

							

# What port to expose to 
EXPOSE 8000



