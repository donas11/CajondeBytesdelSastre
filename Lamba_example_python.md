### Ejemplos Python en AWS Lamba
```import json
import boto3

def lambda_main(evento, contexto):

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
```
import json
import boto3
import susbprocess
 

def lambda_main(evento, contexto:

 pip_list = subprocess.check_output('pip list',shell=True).decode('utf-8').splitlines()
 return {
     'StatusCode' : 200,
     'body': 
 }
```
Set up local development enviroment for AWS
```python3.9 -m venv newenv```
```source newenv/bin/activate```
```ls -ltr```
```pip install request -t .```
```ls -ltr```
```pip install boto3```
```vi app.py```

```
import json
import boto3
import susbprocess

def lambda_main(evento, contexto):
  bucket_name = os.environ.get('bucket_name')
  cliente_s3 = boto3.client('s3')
  cliente_s3.put_object(
    Body=content
    Bucket='bucket_name',
    Key= 'capetacreada/2015-01-01-15.json.gz'
  )
```
Hacemos Zip de todo el envirament con todo
 ```zip -r awslambdaexample.zip . -x newenv/\*```

le damos a donde esta la app  , hay que darle Add permisions  / Attach Policies  -> AmazonS3FullAccess

Configuration/enviroment variables / edit / add enviroment variable Key bucket_name Value aigithub

```python3.9 -m venv newenv```
```source newenv/bin/activate```
```ls -ltr```
```pip install request -t .```
```ls -ltr```
```pip install boto3```
```vi app.py```

```
import json
import boto3
import requests
import susbprocess

def lambda_main(evento, contexto):
  bucket_name = os.environ.get('bucket_name')

content = requests.get('https://data.gharchive.org/2015-01-01-15.json.gz').content

  cliente_s3 = boto3.client('s3')

cliente_s3.put_object(
  Body=content
  Bucket='bucket_name',
  Key= 'capetacreada/2015-01-01-15.json.gz'
)

for object_names = []
for object in Objects:
  object_names.append(object['Key'])

return {
     'StatusCode' : 200,
     'object_names': object_names
 }

```
