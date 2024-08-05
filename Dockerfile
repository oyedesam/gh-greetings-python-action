FROM python:3

# COPY requirement.txt /requirement.txt

# RUN pip install -r /requirement.txt

COPY index.py /index.py

CMD ["python", "/index.py"] 