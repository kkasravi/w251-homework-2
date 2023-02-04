
create-bucket:
	aws s3api create-bucket --bucket kkasravi-w251-homework-2 --region us-east-1 --acl public-read

delete-bucket:
	aws s3 rb s3://kkasravi-w251-homework-2 --force 

install-k3s:
	mkdir $$HOME/.kube/
	curl -sfL https://get.k3s.io | sh -s - --docker --write-kubeconfig-mode 644 --write-kubeconfig $$HOME/.kube/config

port-forward:
	kubectl port-forward service/mosquitto-service 1883:1883

deploy-edge:
	cd broker && make deploy
	cd listener && make deploy
	cd capture && make deploy

deploy-aws:
	cd broker && make deploy
	cd storage && make deploy

undeploy-edge:
	cd broker && make undeploy
	cd listener && make undeploy
	cd capture && make undeploy

undeploy-aws:
	cd broker && make undeploy
	cd storage && make undeploy
