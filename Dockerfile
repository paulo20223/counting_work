FROM python:3.7.4-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt clean && rm -rf /var/lib/apt/lists/* &&  apt update
RUN apt-get install  -y gcc && apt-get install -y make
COPY requirements.txt /code/
RUN pip install -r requirements.txt
