# Use a pre-built image (Python)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 5000 for the web application
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_ENV=production  # Change to production for deployment

# Run the app
CMD ["python", "app/app.py"]
