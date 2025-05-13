FROM sanicframework/sanic:3.8-latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "server.py", "-H", "0.0.0.0", "-p", "8080:8080"]
