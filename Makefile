
create-bucket:
	aws s3api create-bucket --bucket kkasravi-w251-homework-2 --region us-east-1 --acl public-read

delete-bucket:
	aws s3 rb s3://kkasravi-w251-homework-2 --force 

install-k3s:
	mkdir $$HOME/.kube/
	curl -sfL https://get.k3s.io | sh -s - --docker --write-kubeconfig-mode 644 --write-kubeconfig $$HOME/.kube/config

deploy-edge:
	cd broker-edge && make deploy
	cd listener && make deploy
	cd capture && make deploy

deploy-aws:
	cd broker-aws && make deploy
	cd storage && make deploy

undeploy-edge:
	cd broker-edge && make undeploy
	cd listener && make undeploy
	cd capture && make undeploy

undeploy-aws:
	cd broker-aws && make undeploy
	cd storage && make undeploy

list-objects:
	aws s3api list-objects --bucket kkasravi-w251-homework-2

get-object:
	aws s3api get-object --bucket kkasravi-w251-homework-2 --key face.cv2 face.cv2
