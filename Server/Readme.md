# Carpeta para cosas que realizo en un Servidor de pruebas

### Ampliación storage 
#### Primero copiamos todo el contenido del almacenamiento en un archivo:
``` sudo dd if=/dev/sdb of=/home/user/Imagenserver.iso ```


#### Segundo copiamos todo el contenido desde el arhivo al nuevo almacenamiento:
``` sudo dd if=/home/user/Imagenserver.iso of=/dev/sdb```