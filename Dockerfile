FROM python:3.8.5-slim

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

COPY . /opt/app

EXPOSE 8080
ENTRYPOINT ["python", "main.py"]
