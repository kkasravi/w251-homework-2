# w251-homework-2

## Instructions

Both the edge device (VM on mac pro) and AWS use kubernetes.
Prior to deploying the AWS services, you need to update storage/deployment.yaml
to add your ACCESS_KEY and SECRET_KEY variables. The AWS environment can be deployed 
after ssh'ing into an AWS instance by doing:

> make deploy-aws

The AWS instance I've allocated is a t2.medium with an extended volume.

The edge environment can be deployed on the edge VM by doing:

> make deploy-edge

## Questions

- topic  kkasravi/face
- QOS - default 0

## S3 bucket and object location

-bucket: kkasravi-w251-homework-2
-object: face.cv2

Calling the following will download face.cv2 from the S3 bucket

> make get-object

## Notes for AWS

- aws ec2 describe-instances | grep PublicDnsName

## ssh into an available instance

- ssh ubuntu@YOUR_PUBLIC_EC2_NAME.compute-1.amazonaws.com
