FROM python:3.7.4-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt clean && rm -rf /var/lib/apt/lists/* &&  apt update
RUN apt-get install -y build-essential unzip vim git curl locales orca
RUN apt install -y python3-cffi libcairo2 libcairo2-dev libpango-1.0-0 libpango1.0-dev libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
                   libgdk-pixbuf2.0-dev libffi-dev shared-mime-info libffi-dev fonts-font-awesome
RUN apt-get install  -y gcc && apt-get install -y make
COPY requirements.txt /code/
RUN pip install -r requirements.txt
