FROM python:3.10.4
LABEL maintainer="anton.lasko1993@gmail.com"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
