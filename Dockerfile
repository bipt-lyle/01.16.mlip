# Dockerfile to build a flask app
# Use Python 3.8.10 as the base image
FROM python:3.8.10

# Set the working directory to /app
WORKDIR /app

# Copy all files from the current directory to the working directory
COPY . /app

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the application, assuming the entry file is app.py
CMD ["python", "app.py"]
