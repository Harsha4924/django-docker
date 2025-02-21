# From python:3.10

# WORKDIR /app

# COPY requirements.txt /app/

# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.10-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


#stage 2

FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .


EXPOSE 8000

# Run the Django application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]