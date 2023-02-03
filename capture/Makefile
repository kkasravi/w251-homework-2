login:
	docker login

build:
	docker build -t kkasravi/camera:v1 .

push:
	docker push kkasravi/camera:v1

deploy:
	kubectl apply -f deployment.yaml

undeploy:
	kubectl delete -f deployment.yaml
