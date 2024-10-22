# chkdsk
  ``` chkdsk <Nombre_disco> /r /f ```
  * /r verifica
  * /f bbusca sectores defectuosos y trata recuperar la información legible
# diskpart ```diskpart```
## LIST
  ``` LIST DISK ```
    * Lista los discos
  ``` LIST PARTITION```
    * Lista las particiones
  ``` LIST VOLUME ```
    * Lista los volumnes 
## SELECT 
  ``` SELECT DISK=1 ``` or ``` SELECT DISK 1 ```
  * Seleccionar el disco y el número de disco que quieres elegir
  ``` SELECT PARTITION=1 ``` or ``` SELECT PARTITION 1 ```
  * Seleccionar la partición y el número de partición que quieres elegir
   ``` SELECT VOLUME=1 ``` or ``` SELECT VOLUME 1 ```
  * Seleccionar el volumen y el número de volumen que quieres elegir
 ## DETAIL 
  ``` DETAIL DISK ```
  * Detalles del disco
  ``` DETAIL PARTITION ```
  * Detalles de la partición
   ``` DETAIL VOLUME=1 ```
  * Detalles del volumen
 ## Crear volumen
   ``` create volumen simple ```
 ## Asignar Letra
  ``` assign letter=X ```
