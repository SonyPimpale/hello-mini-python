# hello-mini-python

## Requirements
- python3
- docker
- minikube

Project folder ‘hello-mini-python’ with 4 files

## 1. Requiremet.txt    
flask

Flash dependencies in Python is needed for application, which is installed using below command.

```bash
$pip3 install flask 
```

## 2. Application - Hello MiniKube (Simple Python API)
python file to run a web application using flask
Code:

```bash
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ("Hello MiniKube !")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
```

Run below command to check app.py works without errors.

```bash
$ python3 app.py
```

## 2.1 App Tests - Simple PyTest

```
python3 -m pytest tests/*

.
.
2 passed in...
```

## 3. Dockerfile - Create Dockerfile with below code
```bash
FROM python:3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]
```
Build Docker file 

```bash
$docker build -t sony19/flask-kubernete:v0.3 .
```

Check Image 

```bash
$docker images
```

To push the image to Docker Hub

```bash
$ docker push sony19/flask-kubernete:v0.3
```

##4. deployment.yaml

It is a config file that will be run by kubernetes. 
to change the number of replicas, please change the value on the replicas.

```bash
apiVersion: v1
kind: Service
metadata:
  name: flask-test-service
spec:
  selector:
    app: flask-test-app
  ports:
  - protocol: "TCP"
    port: 6000
    targetPort: 5000
  type: LoadBalancer
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-test-app
spec:
  selector:
    matchLabels:
      app: flask-test-app
  replicas: 5
  template:
    metadata:
      labels:
        app: flask-test-app
    spec:
      containers:
      - name: flask-test-app
        image: sony19/flask-kubernete:v0.2
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000
        command: ["python"]
        args: ["/app/app.py"]
```

To run Kubernetes application, Start minikube

```bash
$ minikube start
```

command to kubernetes to run docker and replicate the service
```bash
$ kubectl apply -f /templates/deployment.yaml
```

To check the service has been replicated and running well
```bash
$ kubectl get deployments,pods,service
```

To see the Kubernetes dashboard of application 

```bash
$ minikube dashboard
```

To access the flask application run below command. This will openup the browser, it calls the api which was inside the flask and we can see “Hello world”
```bash
$minikube service flask-test-service
```

To cleanup the deployment
```bash
kubectl delete deployment flask-test-app
kubectl delete service flask-test-service
```

Stop MiniKube
```bash
minikube stop
```
