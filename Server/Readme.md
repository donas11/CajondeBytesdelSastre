# Carpeta para cosas que realizo en un Servidor de pruebas

### Ampliación storage 
#### Primero copiamos todo el contenido del almacenamiento en un archivo:
``` sudo dd if=/dev/sdb of=/home/user/Imagenserver.iso ```


#### Segundo copiamos todo el contenido desde el arhivo al nuevo almacenamiento:
``` sudo dd if=/home/user/Imagenserver.iso of=/dev/sdb```

#### Empezamos bien desde cero 
Como se tiene un respaldo en el almacernamiento anterior se decide configurarlo de nuevo para:
* La creación de todos los usuarios 
* Creación de un grupo para ssh
* establecer una contraseñas por defecto a los usuarios
* y forzar a que cambien la contraseña en el primer inicio
mediante un script:

``` #!/bin/bash

# Contraseña predeterminada
DEFAULT_PASSWORD="Contraseña1234"

# Grupo de SSH específico para SSH
SSH_GROUP="sshusers"

# Verifica si se han pasado usuarios como argumentos
if [ "$#" -eq 0 ]; then
    echo "Por favor, proporciona al menos un nombre de usuario como argumento."
    echo "Uso: $0 usuario1 usuario2 ..."
    exit 1
fi

# Crea el grupo de SSH si no existe
if ! getent group "$SSH_GROUP" > /dev/null; then
    sudo groupadd "$SSH_GROUP"
    echo "Grupo $SSH_GROUP creado para los usuarios de SSH."
fi

# Itera sobre los argumentos (nombres de usuarios)
for usuario in "$@"; do
    # Verifica si el usuario ya existe
    if id "$usuario" &>/dev/null; then
        echo "El usuario $usuario ya existe. Saltando..."
    else
        # Crea el usuario con directorio home y shell de bash
        sudo useradd -m -s /bin/bash "$usuario"
        echo "Usuario $usuario creado."

        # Establece la contraseña predeterminada
        echo "$usuario:$DEFAULT_PASSWORD" | sudo chpasswd

        # Fuerza el cambio de contraseña al primer inicio de sesión
        sudo chage -d 0 "$usuario"
        echo "Contraseña establecida para $usuario y cambio forzado en el primer inicio."

        # Añade el usuario al grupo de SSH
        sudo usermod -aG "$SSH_GROUP" "$usuario"
        echo "Usuario $usuario añadido al grupo $SSH_GROUP para acceso SSH."
    fi
done
 ```
Le damos permisos al script:
``` chmod +x create_and_configure_users.sh ```

Ejecutamos
```sudo ./create_and_configure_users.sh user1 user2 user3 ```