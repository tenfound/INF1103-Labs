FROM python:3.11-slim

WORKDIR /app

COPY full_auditor.py .
COPY inventory.json .

CMD ["python", "full_auditor.py"]