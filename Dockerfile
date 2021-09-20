FROM python:3.9-slim
ADD . /app
WORKDIR /app
ENTRYPOINT ["python", "main.py"]