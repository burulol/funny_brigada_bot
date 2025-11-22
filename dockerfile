# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files (including token.txt) into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir discord.py

# Run the bot
CMD ["python3", "main.py"]

