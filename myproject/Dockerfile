# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies inside a temporary directory
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Use Distroless Image for a Minimal Final Container
FROM gcr.io/distroless/python3-debian11

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Set environment variable to ensure Python finds installed packages
ENV PYTHONPATH="/usr/local/lib/python3.11/site-packages"

# Expose the port Django runs on
EXPOSE 8000

# Run Django server
CMD ["/usr/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]








# # From python:3.10

# # WORKDIR /app

# # COPY requirements.txt /app/

# # RUN pip install -r requirements.txt

# # COPY . .

# # EXPOSE 8000

# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:3.10-slim as builder

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# #stage 2

# FROM gcr.io/distroless/python3

# WORKDIR /app

# COPY --from=builder /install /usr/local

# COPY . .


# EXPOSE 8000

# # Run the Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]