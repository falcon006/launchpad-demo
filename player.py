#!/usr/bin/env python
import pika
from subprocess import call

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='sounds')

def callback(ch, method, properties, body):
    # directory mapping of sounds you want to run locally on
    # your player
    choices = {
               'sound1': '/home/ntillman/sounds/chanchan.swf.mp3',
               'sound2': '/home/ntillman/sounds/metalgearsolid.swf.mp3',
               'sound3': '/home/ntillman/sounds/sadtrombone.swf.mp3',
               'sound4': '/home/ntillman/sounds/doh.swf.mp3',
               'sound5': '/home/ntillman/sounds/preview_4.mp3',
               'sound6': '/home/ntillman/sounds/shoryuken.mp3',
               'sound7': '/home/ntillman/sounds/it-is-wednesday-my-dudes-vine.mp3',
               'sound8': '/home/ntillman/sounds/r2d2.swf.mp3',
               'sound9': '/home/ntillman/sounds/trollolol.swf.mp3' }
    result = choices.get(body, 'none')
    print(" [x] Received %r" % result)
    if result != 'none':
        call(['mpv', result])


channel.basic_consume(callback,
                      queue='sounds',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
