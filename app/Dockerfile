FROM python:3.6.4

RUN mkdir /app
WORKDIR /app


# INSTALL DEPENDENCIES
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8080
