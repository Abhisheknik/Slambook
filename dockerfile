# Use a pre-built image (Python)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 5000 for the web application
EXPOSE 5000

# Run the app
CMD ["python", "app/app.py"]
