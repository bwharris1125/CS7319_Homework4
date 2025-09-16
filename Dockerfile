# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /src

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080 for the API
EXPOSE 8080

# Start the API
CMD ["python3", "src/quote_api.py"]