
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port on which your Flask app runs
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app_flask.py

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app_flask:app"]

