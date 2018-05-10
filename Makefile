
main:
	sudo docker build -t my-php-app .
	sudo docker run -d -p 80:80 --name my-running-app my-php-app

clean:
	sudo docker stop my-running-app
	sudo docker rm my-running-app
	sudo docker rmi my-php-app
