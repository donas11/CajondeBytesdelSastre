# Instalation
```curl -sfL https://get.k3s.io | sh -```

he kubeconfig is stored at ```/etc/rancher/k3s/k3s.yaml```

# K3s Agent Instalation 
NODE_TOKEN comes from ```/var/lib/rancher/k3s/server/node-token```

## on your slave server 
```sudo k3s agent --server https://myserver:6443 --token ${NODE_TOKEN}```

logs de K3s :
```sudo journalctl -u k3s -f``` 

sudo k3s kubectl get nodes:
```sudo k3s kubectl get nodes```

Comprobar puerto esta abierto:
```nc -zv 192.168.1.183 6443 ```

Certificados:
```/var/lib/rancher/k3s/server/tls```



# Tools
[K3sup](https://github.com/alexellis/k3sup)

```
k3sup install --host $AGENT1
k3sup join --host $AGENT1 --server-host $SERVER
k3sup join --host $AGENT2 --server-host $SERVER
```
After the install command, k3sup fetches the kubeconfig file so that you can access your cluster via kubectl.
```
export KUBECONFIG=pwd/kubeconfig
kubectl get node

```
k3sup can also update the configuration file for kubectl by creating and merging different clusters into your KUBECONFIG file.


In the following example, we install two single-node Raspberry Pi clusters and merge them into our kubeconfig file, so we can switch to either one by name:

k3sup install --user pi \
  --ip 192.168.0.101 \
  --context pi-cluster1 \
  --kubeconfig $HOME/.kube/config \
  --merge

k3sup install --user pi \
  --ip 192.168.0.102 \
  --context pi-cluster2 \
  --kubeconfig $HOME/.kube/config \
  --merge

You can then use kubectl config use-context pi-cluster1 or kubectl config use-context pi-cluster2 to access either of the two single node Raspberry Pi clusters

[K3d](https://k3d.io/stable/)

```k3d cluster create ```

``` 
k3d cluster create \
  --servers 1 \
  --agents 1 
```
After the tooling has downloaded a container image for K3s, it will start K3s and save the kubeconfig file into your local Kubernetes context.

```
 k3d cluster delete 

```


```kubectl config get-clusters ```

``` kubectl config current-context ```

``` kubectl get nodes```

``` kubectl get nodes --output wide ```

``` kubectl get nodes --output json ```
If there is a specific field you want to find, such as the CPU architecture, to determine if a node is Intel or ARM, you can run:

``` kubectl get node k3d-k3s-default-server-0 --output jsonpath="{.status.nodeInfo.architecture}" ```

``` kubectl top pod --all-namespaces ```

``` kubectl top node ```

``` kubectl describe node ```


[Multipass](https://canonical.com/multipass)


# Despliege de prueba

```
docker build -t flask-app:0.1.0 .
docker run --name flask-app -p 5000:5000 flask-app:0.1.0 
```

```
docker rm -f flask-app
docker build -t flask-app:0.1.1 .
```


```
docker run --name flask-app -p 5000:5000 flask-app:0.1.1

docker login --username alexallis2
# Paste the Access Token as your password

docker build -t docker.io/alexellis2/flask-app:0.1.1 .
docker push alexellis2/flask-app:0.1.1
```

There are three ways to access a Pod or service within a Kubernetes cluster:

Port-forwarding use of kubectl
Exposing a LoadBalancer using a cloud service or software addition like [MetalLB](https://metallb.io/) or [inlets-operator](https://github.com/inlets/inlets-operator)
Exposing a NodePort