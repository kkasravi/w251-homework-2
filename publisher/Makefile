login:
	docker login

build:
	docker build -t kkasravi/mosquitto-publisher:v1 .

push:
	docker push kkasravi/mosquitto-publisher:v1

deploy:
	kubectl apply -f pod.yaml

undeploy:
	kubectl delete -f pod.yaml

