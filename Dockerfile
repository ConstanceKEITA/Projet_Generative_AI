FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["chainlit", "run", "src/app_chainlit.py", "--host=0.0.0.0", "--port=80"]