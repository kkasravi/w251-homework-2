login:
	docker login

build:
	docker build -t kkasravi/storage-listener:v3 .

push:
	docker push kkasravi/storage-listener:v3

deploy:
	kubectl apply -f deployment.yaml

undeploy:
	kubectl delete -f deployment.yaml

