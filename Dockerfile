# Use an official Python image
FROM python:3.12-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose Django's default port
EXPOSE 8000

# Start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
