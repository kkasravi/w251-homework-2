login:
	docker login

build:
	docker build -t kkasravi/mosquitto-listener:v1 .

push:
	docker push kkasravi/mosquitto-listener:v1

deploy:
	kubectl apply -f deployment.yaml

undeploy:
	kubectl delete -f deployment.yaml

