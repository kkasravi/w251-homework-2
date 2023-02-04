# w251-homework-2

## Overview

Both the edge device (VM on mac pro) and aws use kubernetes.
The aws environment should be brought up first by doing:

> pushd broker && make deploy && popd
> pushd storage && make deploy && popd

Then the public ip of aws needs to be added as an environment variable to listener/deployment.yaml
Prior to deploying capture and listener, you need to run port-forward on the aws machine

> make port-forward

Now bring up the broker, listener and capture deployments on the edge device:

> pushd broker && make deploy && popd
> pushd listener && make deploy && popd
> pushd capture && make deploy && popd


## MQTT 

- topic  kkasravi/face
- QOS - default 0

## S3 bucket

kkasravi-w251-homework-2

## Notes for AWS

- aws ec2 describe-instances | grep PublicDnsName

## ssh into an available instance

- ssh ubuntu@YOUR_PUBLIC_EC2_NAME.compute-1.amazonaws.com
