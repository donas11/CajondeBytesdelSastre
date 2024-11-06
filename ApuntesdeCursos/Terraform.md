---
title: Terraform
created: '2024-10-26T01:46:32.551Z'
modified: '2024-11-06T23:19:22.009Z'
---

# Terraform

## Es una herramienta IaaC (Infrastructure as Code) (Infraestructura como Codigo)
* Es inmutable (borra y crea nueva instacia con la nueva caracteristica)
* Es declarativo
## Maneras de interactuar con la Infraestructura:
* CLI / API
* GUI
* IaC
  * Automatización
  * Reduce errores
  *  Provisioning -Escalable
  * control de versiones
  * CI/CD

## herramientas IaaC
* Provisioning (Aprovisionamiento)
  * Crear Recurso
    * Levantar un MV
    * Levantar un Contenedor
    * Levantar un servidor
  * Herramientas
    * Terraform
      * Cloud agnostic
    * AWS cloudFormation
      * AWS
* Configuration Management (Gestion de la configuración)
  * Herramientas
    * Ansible
    * puppet
    * chef

## Instalación Terraform en Linux 
```
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

## Check Instalation
```terraform -help```
```terraform version```

## configurar creenciales AWS (IAM)
* Crear grupo de Usuarios
  * Name = TeamInsfrastucture
    * Permisos : AdministratorAccess
* Usuarios 
  * Name = AdminUserTerraform
  * Agregamos a grupo TeamInsfrastucture ,creado antes
  
* TeamInsfraestructure
  * credenciales de Seguridad
    * claves de acceso --> Crear clave de acceso
      * Access Key ID: AKIAIOSFODNN7EXAMPLE
      * Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
#### Para hacerlo de forma más segura 
```aws configure```
Nos solicita:
  * AWS Access Key ID[**************]:
  * AWS Secret Access Key[**************]:
  * Default region name[eu-south-2]:
  * Default output format[json]:
podriamos hacer tambien:
```
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGIOM=eu-south-2
```
### comando AWS listar en terminal
``àws s3 ls```


## Arquitectura 
* Archivos de configuración - .tf
  * Declarar los recursos
* Infraestructure Provisioning
  * Permite conectarse 
* Archivo de variable - .tfvars
  * Asignamos el valor de las variables
* Archivos de Estado
  * Estado actual de la infraestructura - .tfstate
* Backend (Donde se almacena el Estado)
  * Local
  * Remoto 
    ```
    terraform {
      backend "gcs"{
          bucket  = "tf-state-prod"
          prefix = "terraform/state"
      }
    }
    ```

## comandos
* ```terraform init```
  * Se descargan los providers de los proveedores declarados en nuestro archivo de configuración
    * AWS
    * Google Cloud
    * Azure
* ```terraform plan```
  * compara la configuración declarada con la del estado actual
    * Se genera un plan con los recursos que 
      * va a borrar
      * va a necesitar
* ```terraform apply```
  * ejecuta el plan generado
  * ```--auto-aprove ``` imprescidible para automatizar sin intervencion humana
* ```terraform destroy```
  * destruye todo
  * <span style="color: red;">TODO TODO </span>  ``` terraform destroy --auto-aprove ``` 
* ```terraform validate```
* ```terraform fmt``` tabula los archivos si estan mal tabulado 


## Script main.tf
```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-south-2"
  acces_key    = AKIAIOSFODNN7EXAMPLE
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}


resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}
```
### Iniciamos los providers
```Terraform init```
* crea carpeta ```.terraform``` archivo ```lock.hcl```
### Compara lo que he definido con nada(por que no hay estado actual, ya que es nuevo)
```Terraform plan```
#### ver el plan paso a paso
#### Ver catalogos de AMI para saber los parametros
### Aplicamos en plan
```Terraform apply```
* se crea el archivo ```terraform.tfstate```
##### Chekeamos que las instancias se estan ejecutando

### Destruimos todo
```terraform destroy```
##### Chekeamos que las instancias se estan cerrandose y terminan


### Otros ejemplos:
```
resource "aws_s3_bucket" "s3_bucket" {
  acl           = "private"
  bucket_prefix = "testbucket"
  region        = "eu-south-2"
}
```

#### Crea: 
* un provider configuration 
```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region = "eu-south-2"
}

```
* Create EC2 resource block:
```
resource "aws_EC2" "resource_EC2" {
  tags = {
    Name = "MyInstanceEC2"
  }
}

```
* Crea un argument AMI y añade un AMI para Windows 2019
Buscamos
``` 
aws ec2 describe-images --owners amazon --filters "Name=name,Values=Windows_Server-2019*" --query "Images[*].[ImageId,Name,CreationDate]" --output text --region eu-south-2
```

```
resource "aws_EC2" "resource_EC2_windows" {
  ami           = ami-0123456789abcdef0
  tags = {
    Name = "MyInstanceEC2"
  }
}

```
* crea una instacia de type argument y establecelo as t2.micro

```
resource "aws_EC2" "resource_EC2_windows" {
  ami           = ami-0123456789abcdef0
  instance_type = "t2.micro"
  tags = {
    Name = "MyInstanceEC2"
  }
}

```

#### Crea: 
* crea un provider configuration
```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region = "eu-south-2"
}
```
* crea un recurso EC2 estableciendo como una instancia de tipo ami
```
resource "aws_EC2" "resource_EC2" {
  ami           = ami-0a8e758f5e873d1c1
  instance_type = "t2.micro"
}
```
* Crea 3 tags para la instancia, incluyendo nombre de la etiqueta
```
resource "aws_EC2" "resource_EC2" {
  ami           = ami-0a8e758f5e873d1c1
  instance_type = "t2.micro"
  tags = {
    name = "Amazon_linux_2"
    environment = "dev"
    version = "0.0"
  }
}
```

#### Volume Rosource
```
provider "aws" {
  region = "eu-south-2"
}

resource "aws_EC2" "resource_EC2" {
  ami           = ami-0a8e758f5e873d1c1
  instance_type = "t2.micro"
}

resource "aws_ebs_volume" "volume_example"{
  availability_zone ="eu-south-2a"
  size              = 40
}

rosource "aws_volumen_attachment" "ebs_att"{
  device_name = "/dev/sdh"
  volume_id = aws_ebs_volume.example.id
  instance_id = aws_instance.tags-test.id
}
```


# Azure -Terraform
## Azure authentification
```az login```
`` az account --help```
```account set --subscription "a6d9c59-4d51-a944-9cc278b67c8a" ```

## Azure provider

