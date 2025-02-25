``` 
kubectl apply -f ingress.yaml 
kubectl port-forward -n kube-system service/traefik 8080:80
curl http://127.0.0.1:8080
kubectl get pods
kubectl logs pod/flask-app-6c74fb9c7c-2dzmw

```


```
kubectl apply -f ingress-host.yaml
curl http://127.0.0.1:8080
curl http://127.0.0.1:8080 --header "Host: flask-app.example.com"
```

https://kubernetes.io/docs/concepts/services-networking/service/