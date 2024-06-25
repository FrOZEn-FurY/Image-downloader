FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    zlib1g-dev \
    build-essential \
    libjpeg-dev && \ 
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver-linux64/chromedriver

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV POSTGRES_DB images
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD root1234
ENV POSTGRES_HOST db
ENV POSTGRES_PORT 5432

EXPOSE 80

ENV NAME World

CMD ["python", "runner.py"]