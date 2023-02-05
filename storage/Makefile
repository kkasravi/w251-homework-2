login:
	docker login

build:
	docker build -t kkasravi/storage-listener:v4 .

push:
	docker push kkasravi/storage-listener:v4

deploy:
	kubectl apply -f deployment.yaml

undeploy:
	kubectl delete -f deployment.yaml

