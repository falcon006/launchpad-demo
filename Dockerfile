FROM php:7.0-apache
COPY src/ /var/www/html/
COPY send.py /usr/local/bin

RUN apt-get update && apt-get install -y \
		python \
		python-pip
RUN pip install pika==0.11.0
