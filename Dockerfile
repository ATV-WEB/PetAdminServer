# Base image
FROM python:3.10-slim

# Setup environment variable
ENV DockerHOME=/home/app/petadmin

# Create home directory for app user
RUN mkdir -p $DockerHOME

# Create DB directory
RUN mkdir -p $DockerHOME/db

# Create the volume
VOLUME [ $DockerHOME/db ]

# Where your code lives
WORKDIR $DockerHOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip

# Copy whole project to your docker home directory. 
COPY . $DockerHOME

# Run this command to install all dependencies
RUN pip install -r requirements.txt

# Run django migrations
RUN python manage.py migrate

# Port where the Django app runs
EXPOSE 8000/tcp

# Start server
CMD ["python" "manage.py" "runserver" "0.0.0.0:8000"]