### Ejemplos Python en AWS Lamba
```
import json
import boto3

def lambda_main(evento, contexto:

  # cliente
  cliente_s3 = boto3.client('s3')

  # cubo 
  buckects = s3_client.list_buckets()

  #recoge el cubo del evento
  bucket_name = evento['bucket_name']

  objects = s3_client.list_objects()
  objects_name = []

  # nombre de los cubos
  buckets_name = []
  print(buckects)
  print(objects)
     
  for bucket in buckets['Buckets']:
       buckets_name.append(bucket['Name')

  for object in objects['Contents']:
       objects_name.append(object['Key')

  return {
      'StatusCode' : 200,
      'body': evento,
      'buckects' buckects
  }
```
Necesitas dar permisos AmazonS3ReadOnlyAccess para que no de una excepción

