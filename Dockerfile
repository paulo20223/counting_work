FROM python:3.7.4-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt clean && rm -rf /var/lib/apt/lists/* &&  apt-get update
RUN apt-get update && apt-get install -y python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 libpango1.0-dev

RUN apt-get install  -y gcc && apt-get install -y make
COPY requirements.txt /code/
RUN pip install -r requirements.txt
