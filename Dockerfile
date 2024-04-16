FROM python:3.8-slim

WORKDIR /app
COPY app /app

RUN apt-get update && apt-get install -y curl \
    && pip install flask

EXPOSE 5000

CMD ["python", "simple_flask_app.py"]
