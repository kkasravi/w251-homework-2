login:
	docker login

build:
	docker build -t kkasravi/mosquitto:v1 .

push:
	docker push kkasravi/mosquitto:v1

deploy:
	kubectl apply -f deployment.yaml

status:
	kubectl get service mosquitto-service

listener:
	mosquitto_sub -h localhost -p 30926 -t my_topic

publisher:
	mosquitto_pub -h localhost -p 30926 -t my_topic -m "hello mqtt"
