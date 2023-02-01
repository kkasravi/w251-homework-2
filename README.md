# w251-homework-2

## MQTT 

- topic  kkasravi/face
- QOS - default 0


## Directoryies

The iot directory contains

```
iot
├── deployment.yaml (has the service and deployment yaml)
├── Dockerfile (to create the alpine mosquitto broker)
└── Makefile
```

The listener directory contains:

```
listener/
├── deployment.yaml
├── Dockerfile
├── listener.py
└── Makefile
```

## Starting the edge vm broker and service

> cd iot && make deploy

## Starting the aws vm broker and listener

> cd listener && make deploy


## Misc development notes for AWS

- aws ec2 describe-instances | grep PublicDnsName

## ssh into an available instance

- ssh ubuntu@YOUR_PUBLIC_EC2_NAME.compute-1.amazonaws.com
