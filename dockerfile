
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app_flask.py .

CMD ["python", "app_flask.py"]



# FROM python:3.11

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app_flask:app"]
