<<<<<<< HEAD
# Docker 
## Mover archivos del contenedor al Host


``` docker cp NombreContenedor:RutaContenedor RutaHost/Archivo ```
## Mover archivos del Host al contenedor
=======
# Docker
>>>>>>> b24e931903b9af9ef343766e4baa3d3a9a70f53a

<<<<<<< HEAD
``` docker cp RutaHost/Archivo NombreContenedor:RutaContenedor/Archivo ```

=======
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

>>>>>>> b24e931903b9af9ef343766e4baa3d3a9a70f53a
