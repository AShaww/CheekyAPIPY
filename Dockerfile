# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy requirements from host, to docker container in /app
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8000 within the container
EXPOSE 8000

# Run your FastAPI application
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload", "app.app:app"]
