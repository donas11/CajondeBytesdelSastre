``` kubectl create -f pod.yaml ```


``` kubectl get pods ```


```
   kubectl port-forward flask-app 5000:5000
   curl http://127.0.0.1:5000 ;echo
```
result: Hello world

```
kubectl logs pod/flask-app
```
result: INFO:waitress:/ invoked


```
kubectl get pod/flask-app --output go-template="{{.metadata.name}} {{ .status.podIP }}" ; echo;

```
result: flask-app 10.244.0.11

```
kubectl delete -f pod.yaml
kubectl get pod/flask-app --output go-template="{{.metadata.name}} {{ .status.podIP }}" ; echo;
kubectl apply -f service.yaml
kubectl port-forward service/flask-svc 5000:5000

curl http://127.0.0.1:5000 ;echo

```


```
kubectl apply -f pod-b.yaml
kubectl port-forward service/flask-svc 5000:5000
curl http://127.0.0.1:5000 ;echo
```

```
kubectl delete -f pod.yaml,pod-b.yaml
kubectl create -f deployment.yaml
kubectl port-forward service/flask-svc 5000:5000

curl http://127.0.0.1:5000 ;echo
curl http://127.0.0.1:5000 ;echo
curl http://127.0.0.1:5000 ;echo

kubectl logs deploy/flask-app

kubectl get pods
```
NAME                        READY  STATUS   RESTARTS  AGE
flask-app-6c74fb9c7c-hr4s7  1/1    Running  0         54s
flask-app-6c74fb9c7c-kzt9c  1/1    Running  0         54s
flask-app-6c74fb9c7c-sb5f6  1/1    Running  0         54s

Now get the logs of each pod:
```
kubectl logs pod/flask-app-6c74fb9c7c-hr4s7
kubectl logs pod/flask-app-6c74fb9c7c-kzt9c
kubectl logs pod/flask-app-6c74fb9c7c-sb5f6
```