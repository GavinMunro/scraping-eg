FROM python:3.6-slim-buster

WORKDIR /home/tweety
RUN adduser tweety --disabled-password

COPY requirements.txt requirements.txt
RUN python -m venv venv
# RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . ./
# COPY migrations migrations  # ToDo: L8r
COPY flask_app.py config.py boot.sh ./
RUN chmod +x ./boot.sh


ENV FLASK_APP flask_app.py

RUN apt update
RUN apt install -y wget
RUN apt install -y unzip

# RUN apt install -y chromium
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

RUN wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
# RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.27/chromedriver_linux64.zip
RUN unzip -a chromedriver_linux64.zip
ENV CHROMEDRIVER_PATH="/home/tweety/chromedriver"


RUN chown -R tweety:tweety ./
USER tweety

# Open port 5000 for Flask app
EXPOSE 5000

# tell the container to execute the start script
ENTRYPOINT ./boot.sh  # Preferred basic exec entry point.
# ENTRYPOINT ["/bin/bash", "/srv/start.sh"]

# Run command: "docker run --name flask_app -d -p 8000:5000 -e FLASK_APP=flask_app flask_app:latest"
# Curl command to access API running in container: curl http://127.0.0.1:8000/tweets
