FROM python:3.10.6

WORKDIR /app
COPY docker-compose-ci.yaml .
COPY app .
RUN pip install -r requirements.txt



CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]





