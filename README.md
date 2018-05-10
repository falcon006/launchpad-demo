
# launchpad-demo

![alt text](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)
[![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com)

## Server setup

1. Configure your rabbgitmq service.
    
    ``sudo docker run -d --hostname my-rabbit -p 5672:5672 --name some-rabbit rabbitmq:3``

2. Update send.py and player.py to point to rabbitmq IP

    ``pika.ConnectionParameters(host='172.20.239.52',port=5672)``

3. Run make to start web service


## Client setup

1. Install packages:
 
    ``sudo apt-get update && sudo apt-get install -y python python-pip``
    
    ``sudo pip install pika==0.11.0``

2. Update player.py sound list with sounds of your choosing.

3. Run service: `python ./player.py`

4. (optional) Install startup script.

   `cp player.service /etc/systemd/system/player.service;`
   
   `systemctl enable player`

