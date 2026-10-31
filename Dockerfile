FROM python:3.11-slim

WORKDIR /app

COPY P2_labs/oo_auditor.py .
COPY inventory2.json .

CMD ["python", "oo_auditor.py"]