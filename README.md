# w251-homework-2

## Instructions

Both the edge device (VM on mac pro) and aws use kubernetes.
The aws environment should be deployed by doing:

> make deploy-aws

on the aws instance. In this case I've allocated a t2.medium.
Next on the edge VM, deploy the edge services by doing:

> make deploy-edge


## MQTT 

- topic  kkasravi/face
- QOS - default 0

## S3 bucket

kkasravi-w251-homework-2

## Notes for AWS

- aws ec2 describe-instances | grep PublicDnsName

## ssh into an available instance

- ssh ubuntu@YOUR_PUBLIC_EC2_NAME.compute-1.amazonaws.com
