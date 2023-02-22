FROM python:3.8.15-slim-bullseye@sha256:3778adf3c19e35a6cbb7e7ef85c8715e4062f0292e7e8f876a84cc90657d2126 
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
COPY requirements.txt .
# COPY .env .
RUN pip install --no-cache-dir -r /app/requirements.txt
USER 1001
EXPOSE 8080
WORKDIR /app
CMD ["python", "app.py"]