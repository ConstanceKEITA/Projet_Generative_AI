FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["chainlit", "run", "src/app_chainlit.py", "--server.address=0.0.0.0", "--server.port=8000"]
