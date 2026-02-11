# Use official Python runtime as base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional, remove if not needed)
#RUN apt-get update && apt-get install -y --no-install-recommends \
 ##  && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)


# Install Python dependencies
RUN pip install --upgrade pip 
   

# Copy project
COPY . .

# Expose port (change if your app uses a different one)
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
