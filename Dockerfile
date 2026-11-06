FROM python:3.11-slim

WORKDIR /app

COPY P2_labs/Lab7/phys_dig_auditor.py .
COPY P2_labs/Lab7/class_Can_Be_Shipped.py .
COPY P2_labs/Lab7/class_Product.py .
COPY P2_labs/Lab7/class_Digital_Product.py .
COPY P2_labs/Lab7/class_Physical_Product.py .
COPY P2_labs/Lab7/class_Inventory.py .
COPY inventory2.json .

CMD ["python", "phys_dig_auditor.py"]