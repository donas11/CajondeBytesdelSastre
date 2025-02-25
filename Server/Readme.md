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

para restringir el uso del ssh solo a estos usurios podemos hacer en el archivo  ``` /etc/default/dropbear ``` modificamos ``` DROPBEAR_EXTRA_ARGS="-G sshusers"``` para restringir solo al grupo sshusers el uso de él ```sudo systemctl restart dropbear ```

## Instalación de herramientas que utilizaremos
``` sudo apt install curl ```
``` sudo apt install wget ```
``` sudo apt install nmap ```
``` sudo apt install nano ```

## Instalación de Servicios que utilizaremos
```curl -s https://install.zerotier.com | sudo bash ```

```sudo apt install python3 python3-pip python3-venv```
```python3 -m venv devops```
```source devops/bin/activate```
```pip install localstack```


```sudo apt-get install ca-certificates curl gnupg lsb-release```

```sudo mkdir -p /etc/apt/keyrings```
```curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg```

```echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null```

```sudo apt-get update```
```sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin```

```localstack start & pip install awscli```

```nano ~/.bashrc  # o ~/.zshrc si usas Zsh```

```alias aws.="aws --profile localstack --endpoint-url=http://localhost:4566"```

```sudo apt install nodejs npm```

```node -v```
```npm -v```
```sudo npm install -g azurite```

# Instalación K3S
```mermaid 
graph TD;
    K3s["Raspberry Pi - K3s Master"]<--|Connection| K3sAgent["VAIO Laptop - K3s Agent"]

```

## Instalacion K3S en RaspberryPI

se escogio dietpi como distribución por que consumia menos RAM para asi poder disponer del maximo disponible de ella

```curl -sfL https://get.k3s.io | sh - ```

kubeconfig esta en ```/etc/rancher/k3s/k3s.yaml```

## Instalacion K3S en VAIO

```sudo k3s agent --server https://IPRaspberryPIserver:6443 --token ${NODE_TOKEN}```

el NODE_TOKEN viene en ```/var/lib/rancher/k3s/server/node-token```