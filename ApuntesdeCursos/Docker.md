---
title: Docker
created: '2024-10-25T12:29:45.727Z'
modified: '2024-11-02T01:51:11.280Z'
---

# Docker

### Docker Hub
* Description
  * enviroment variables
    ```-e VARIABLE_ENTORNO ```

## Comandos basicos
  * nombrar
    * contenedor
      ``` --name nombre_contenedor ```
    * tag
      ``` name_image_contenedor:TAG ```
  * rename
    ``` Docker rename contenedor nuevo_combre```
  * Eliminar contenedor
    ``` Docker rm <conatainer_id/container_name> ```
    * ``` -f ```para forzar apagarlo 
    * Todos los que han terminado: ``` docker rm $(docker ps --filter status=exited -q) ```
  * Eliminar imagenes  
    * ``` docker rmi ubuntu:latest ```
    * ``` docker rmi $(docker images) ```
  * Ver todos los procesos con su tamaño utilizado
    ``` docker ps -a -s```
  * Buscar images
    ```Docker search nombre_a_buscar ```
  * Pararlo
    ``` Docker stop contendedor ```
  * Restart
    * ``` Docker restart contendedor ```
    * ``` --time -t ```
### Volumes
``` docker run -d --name devtest --mount source=myvol,target=/usr/share/nginx/html nginx:latest ```

Check docker volume created
```docker inspect name_conatiner```
``` 
"volumenDriver": "",
"volumenFrom": "null",
      "type": "volume",
      "Source": "myvol",
```
Borrar el volumen
```docker volume rm myvol```
Remove all unused volumes
```docker volume prune```

### Logs
  * ```docker logs -f contenedor ```

### Docker info
### Docker stats

### Mover archivos del contenedor al Host
```docker cp NombreContenedor:RutaContenedor RutaHost/Archivo```
### Mover archivos del Host al contenedor
```docker cp RutaHost/Archivo NombreContenedor:RutaContenedor/Archivo```
### Guardar imagen 
```docker save ni_image:latest | gzip > /home/images/myimage.tar.gz```
### importar imagen
``` docker load < /home/images/myimage.tar.gz```

## Docker Facilita CI/CD
### Continuous Integration (CI) (Pipeline)
* Build -> Test -> Merge

### Continuous Deployt (CD) (Pipeline)
* Liberación automática al repositorio 
* Despliegue automatico hacia producción


## Docker File
```
FROM:
MAINTAINER:
RUN:
CMD:
ENTRYPOINT command
ENV
WORKDIR

```
Dentro del contenedor podemos imprimir los values del ENV
``` printenv ```
``` printenv  | grep -i jenkins```
``` printenv  | grep -i flask```
``` printenv  | grep -i mongo```


## Docker Networking
``` docker network ls ```
``` docker inspect bridge(Conatiner_name) ```
Create own network
```docker network create mynetwork```
para poner el contenedor en esa red 
``` --network ```

contenedor dashboard 
portainer



## Docker Swarm
```sudo docker swarm init ```
```sudo docker node ls ```
```sudo docker stack deploy --compose-file dcfile.yml docker-swarm ```
```sudo docker stack services docker-swarm ```
```sudo docker swarm leave --force```



## Kubernetes
Expose application deployed
```kubectl expose deployment web-server --type LoadBalancer --port 80 --target-port 80```
Inspecting application deployed
```kubectl get pods```
kubectl get service web-server
```Kubectl logs –f {pod}```


## GKE (google Kubernetes Engine)
Set project-id and zone
```gcloud config set project webserver-demo-gke```
```gcloud config set compute/zone asia-southeast1```
Create GKE Cluster
```gcloud container clusters create webserver-gke-cluster --num-nodes=1```
```gcloud container clusters get-credentials webserver-gke-cluster```
** above cmd configures kubectl to use the cluster **
Deploy Application to Cluster
```kubectl create deployment web-server --image=asia.gcr.io/ {project-name}/my-web:V1```


## Docker Content Trust:

habilita Docker Content Trust
```export DOCKER_CONTENT_TRUST=1````
Notary Server: A Notary server should be
available for signing and verifying
signatures.

creating key 
``` docker trust key generate name_key```

import key 
```docker trust key load [Ruta_Formato_PEM] –name [name_key] ```
add signer: 
```docker trust signer add –key [archivo_clave_PEM] [name_signer] [REPOSITORY] ```
remove signer: 
```docker trust signer remove [NAME] [REPOSITORY]```
inspect repository:
 ```docker trust inspect –pretty [REPOSITORY]```
creating key : 
```docker trust key generate [NAME]```
 Rechazar Imágenes sin Firma
```export DOCKER_CONTENT_TRUST=1 ```

Enabling DCT Habilitar Docker Content Trust en el Daemon:: 
```vi /etc/docker/daemon.json```

```
{
  "content-trust": {
    "mode": "enforced"
  }
}
```

#### Automation (Esto es útil para escenarios de automatización en CI/CD, donde Docker necesita firmar imágenes sin intervención manual.)
Genera una contraseña codificada en base64 usando tu archivo de clave privada.
``` export ENCODED_PASSPHRASE=$(cat ~/.docker/trust/private/baba7529e7dfa46112aebe8b60817a0a5666ce440afd5cfd16066fdc34d24ff4.key | base64) ```

Exporta esta contraseña para que Docker la use como la clave de firma:
``` export DOCKER_CONTENT_TRUST_REPOSITORY_PASS_PHRASE=$ENCODED_PASSPHRASE ```

