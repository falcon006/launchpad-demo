#!/usr/bin/env python
import pika
import sys
soundname = sys.argv[1]
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.64'))
channel = connection.channel()


channel.queue_declare(queue='sounds')

channel.basic_publish(exchange='',
                      routing_key='sounds',
                      body=soundname)
print(" [x] Sent 'Hello World!'")
connection.close()
