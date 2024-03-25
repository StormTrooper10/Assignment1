FROM python:3.8-alpine
WORKDIR /app
Copy . /app
RUN pip install -r requirements.txt
Expose 5000
CMD ["python", "app.py"]

