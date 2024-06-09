# Dockerfile for auto_selecto (backend)
FROM python:3.11-alpine

# Select working directory
WORKDIR /code

# Update
RUN apk update
RUN apk add libpq-dev
RUN apk add build-base

# Copy requirements.txt to working directory
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# RUN python manage.py makemigrations

# RUN python manage.py migrate

# Copy all files to working directory
COPY . .

# Expose the container port
EXPOSE 8001

# Execute the app
CMD ["python","manage.py","runserver","0.0.0.0:8001"]
# ENTRYPOINT [ "/bin/bash", "/code/entrypoint.sh" ]