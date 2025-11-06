# 1️⃣ Use official Python image as base
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy project files into container
COPY . /app

# 4️⃣ Install dependencies (Flask)
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expose Flask port
EXPOSE 5000

# 6️⃣ Command to run Flask app
CMD ["python3", "app.py"]
