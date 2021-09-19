FROM python:3.6-slim
ADD . /app
WORKDIR /app
ENTRYPOINT ["python", "main.py"]