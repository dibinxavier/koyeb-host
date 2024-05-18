# Use a base image with Python
FROM python:3.9-slim

# Copy your Python script into the container
COPY alert.py /app/

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Start your Python script
CMD ["python", "alert.py"]
