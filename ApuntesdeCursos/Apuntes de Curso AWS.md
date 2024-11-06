---
title: Apuntes de Curso AWS
created: '2024-10-24T23:43:16.709Z'
modified: '2024-11-06T22:57:49.840Z'
---

# Apuntes de Curso AWS
## ¿Qué es el Cloud?
Un ordenador en otro lado que nos alquilan parte por su uso
## AWS Amazon Web services
Colección de servicios de computación en la nube que los Ofrece Amazon
* Flexivilidad escalado vertical y horizontal
## UI
## EC2 Elastic Cloud Computing
* Capacidad de crear una Instacia de una Maquina
  ```Lanzar Instancia```
    * Nombre
    * Choose Amazon Machine Image (AMI) 
      * Elegimos la imagen del SO
    * Tipo de Instancia 
      * Comparar tipos de instancias
    * Par de Claves
      * Creamos claves: (Privadas)
        * RSA 
        * ED25519 
        * formatos:
          * pem
          * ppk
        * Guardamos archivos en un sitio seguro
    * Configuración de red
      *  Mejor que estén en la misma red por la latencia, para tener menos, 
      * Ventajas de seguridad al estar en la misma red
      * Creamos grupo de seguridad (como Firewall)
      * Allow SSH,HTTP,HTTPS

## Base de datos 
  * DocumentDB
    * compatible con MongoDB 
  * DynamoDB
    * Capacidad
    * Por uso
      * Escalable
    * Amazon MemoryDB for Redis
    * RDS RDS (Relational DataBase Services)
      * Aurora(MSQL compatible)
      * Aurora(PostGre compatible)
      * MySQL
      * MariaDB
      * PostgreSQL
      * Oracle
      * Microsoft SQL Server
      * IBM Db2
      
## S3 y AWS CLI
#### S3 Simple Storage Service
* Buckets (Objetos)  
* Imagenes
* Videos
* Documentos
* JS/HTML/CSS
Cuanto más disponibilidad (menos latencia) > más caro

###### Politicas para Buckets
``` {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/your-username"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```



``` 
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/your-username"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```
##### AWSCLI
IAM > Crear Usuario --->
Nombre = username

Politicas de Permisos 

Credenciales
Key y el Secret

```aws configure```
Key y Acces key

 


## AWS Lambda
Solo cuando lo necesita (solo se paga por el tiempo de computación)
* Lambda Funtions
---> Deploy 
---> Test
* Monitorizar el lambda
  * Logs
* Agregar desencadenador
* Agregar destino --> por ejemplo a una Queue
* URL de la función 


## Crear una web
## Hospedaje
  * Base de datos
  * Almacenaje (Imagenes)
  
## Mailing 
  * Cola de Eventos
# Enrutamiento
# Transacciones


## Spike en un server  (1000 usuarios en una hora) (No downtime) (más complejo por Balancear) (mayor disponibilidad al tener redundancia)
### Escalar horizontal (Añadir/quitar Vecinos )
  * Añadimos otro servidor 
### Escalar Vertical (Hacerlo más grande o hacerlo más pequeño (para ahorrar recursos)) (downtime-pierdes la conectividad un momento)
  * Añadir/Quitar RAM
  * Mejorar/Reducir Velocidad CPU
  * Aumentar/Bajar Alamacenaje

## Elegir la Region para el servicio en concreto
