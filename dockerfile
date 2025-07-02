FROM python:3.8-slim-buster

# Set working directory#
WORKDIR /app

# Install awscli and clean up cache to reduce image size
RUN apt update -y && apt install -y awscli && apt clean && rm -rf /var/lib/apt/lists/*

# Copy application code and offline packages
COPY . /app
COPY ./packages /packages

# Install Python dependencies from local wheels
RUN pip install --find-links=/packages -r requirements.txt


# Command to run the app
CMD ["python3", "app.py"]
