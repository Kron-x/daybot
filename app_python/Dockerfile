FROM python:3.7-alpine

WORKDIR /app

COPY main.py requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
