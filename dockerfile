FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose a port if needed (for web services, etc.)
# EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]