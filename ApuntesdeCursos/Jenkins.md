---
title: Jenkins
created: '2024-10-25T12:24:39.510Z'
modified: '2024-11-02T01:55:35.575Z'
---

# Jenkins
## update
```sudo apt update```
## install Java
```sudo apt install openjdk-11-jdk -y```
## check Java
``` java -version ```
## add repository key
```wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add - ```
## Append the Debian package repository address to the server’s sources.list
``` sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' ```
## update
```sudo apt update```
## install JenKins
```sudo apt install jenkins -y```
## check Jenkins
```sudo systemctl status jenkins```
## start JenKins
```sudo systemctl start jenkins```


# install credentials v2.5 to current dir por la escifica opcdión -d
```java -jar jenkins-plugin-manager-.* --awr /usr/lib/jenkins.war --plugins credentials:2.5 -d . ```
# mover manualmente el credential.jpi (el archivo de plugin) a var/lib/jenkins/plugins
```cp credentials.jpi /var/lib/jenkins/plugins/ ```
# Reiniciamos servicio 
```sudo service jenkins restart```


Declarative Pipeline syntax example Jenkinsfile:
```
pipeline{
  agent any 
  stages {
    stage('Build'){
      steps{
        echo "Build Stage"
        echo env.BUILD_NUMBER
      }
    }
    stage('Test'){
      steps{
        echo "Test stage"
        echo "the espacio de trabajo es: ${env.WORKSPACE}"
      }
    }
    stage('Deploy'){
      steps{
        echo "Deploy Stage"
        echo "El resultado actual es : ${currentBuild.currentResult}
      }
    }
  }
}
```

## Declarative Pipeline syntax example Jenkinsfile Run Docker :
## Dasboard -> Plugin Manager --> Docker

```
pipeline{
  agent any 
  enviroment{
    registry = "Kss7/checks"
    img = "$registry" + ":${env.BUILD_ID}
    registryCredential = 'docker-hub-login'
  }
  stages {
    stage('Checkout'){
      steps{
        git branch: 'main',url: 'https://github.com/kss7/SmartFlasAPP.git'
        sh 'ls -la'
      }
    }
    stage('Build'){
      steps{
        echo "Build our image"
        script{
          dockerImg = docker.build("${img}")
        }
      }
    }
    stage('Deploy Run'){
      steps{
        echo "Deploy and Run"
          script{
            cont = docker.image("${img}").run('-d -p 5000:5000')
          }
      }
    }
    stage('Run'){
      steps{
        echo "Run Image"
        sh returnStdout:true,script:"docker run -d --name ${JOB_NAME}-p 5000:5000 ${img}"
      }
    }
  }
}
```
## Jenkins/newJob
* Item name -> PipelineDockerCmdStopContainer 
* Select Pipeline -> OK
* Advanced Project Options -> Script -> Apply -> Save
## Dasboard -> PipelineDockerCmdStopContainer --> Build Now

## SSH Connection
* Public -> va para el servidor
* Privada -> la tienes tú guardaita desde donde accedes (cliente)
* Generar
  * Entramos como root ```sudo -i```
  * cambiamos a la carpeta que queramos ejemplo .credentials ```cd .autorized_keys```
  * generamos ``` ssh-keygen ``` 
  * elegimos donde guardarlo guardará en la carpeta ```/.autorized_keys/.ssh/id_rsa/```
  * introducimos un passphrase la que queramos
  * Dasboard -> Plugin Manager --> ssh-agent
  * Manage Jenkins -> Manage Credentials
    * Stores scoped to Jenkins -> Jenkins -> (System) -> Global credentials(unrestricted) -> add credentials
      * Kind -> SSH Username with private Key
      * ID = docker-host-root-keys
      * Username = docker
      * Enter Directly --> copy of cat id_rsa
      * passphrase = la que hayamos querido
  * Dasboard -> All
    * Item name -> ssh-keys-testing
    * Select Pipeline -> OK
    * Advanced Project Options -> Script -> Pipeline Syntax -> Sample step : sshagent: SSH Agent --> docker-host-ssh-keys
    * 
    ```
    node {
      sshagent(['docker-host-ssh-keys']){
        sh 'ssh -o StrictHostKeysChecking=no -1 docker Direccion_ip_server '  
        // podemos añadir por ejemplo "uname -a" o "who"
      }
    }
    
    ```

## Allow a usuraios de Jenkins acceder to the docker socket
<span style="color: red;">Tipico Error : got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:]</span>
```sudo usermod -aG docker jenkins```
```sudo systemctl restart jenkins```

## Manage Jenkins -> Manage Plugins --> installed --> 
  * cloudBees Docker Build and publish plugin
  * ssh Agent Plugin
## Manage Jenkins -> Manage Credentials -->
  * docker-test (docker login with ssh)
    * Scope -> Global (jenkins,nodes item,all child items,etc)
    * ID = docker-test
    * Description = docker login with ssh
    * Username = docker
    Private Key --> Enter directly (you Know)

## Manage Jenkins -> Manage Credentials -->
  * Kss7(docker-hub-login)
    * Scope -> Global (jenkins,nodes item,all child items,etc)

    * ID = docker-hub-login
    * Description = docker-hub-login
    * Username = kss7
    * password = 
    * Private Key --> Enter directly (you Know)


```
def img
pipeline {
    environment {
        registry = "kss7/python-jenkins" //To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.
        registryCredential = 'docker-hub-login'
        dockerImage = ''
    }
    agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/kss7/SimpleFlaskUI.git'
            }
        }

        stage ('Stop previous running container'){
            steps{
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force' //this will delete all images
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
            }
        }


        stage('Build Image') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }



        stage('Test - Run Docker Container on Jenkins node') {
           steps {

                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
          }
        }

        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Test Server') {
            steps {
                script {
                    def stopcontainer = "docker stop ${JOB_NAME}"
                    def delcontName = "docker rm ${JOB_NAME}"
                    def delimages = 'docker image prune -a --force'
                    def drun = "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
                    println "${drun}"
                    sshagent(['docker-test']) {
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${stopcontainer} "
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${delcontName}"
                        sh returnStatus: true, script: "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${delimages}"

                    // some block
                        sh "ssh -o StrictHostKeyChecking=no docker@192.168.1.16 ${drun}"
                    }
                }
            }
        }


    }
```

## Para imagenes de Docker Firnadas de forma automatica

Dashboard > new item + --> freestyle project --name= pull-docker-dct --> OK

GENERAL > Build Steps --> Execute Shell --> docker pull miimagen/tag --> Save 

Dashboard > Build Executor Status --> Built-In_Node --> Configure --> Enviroment variables--> Add:

Name : ENCODED_PASSPHRASE

Value : $(cat ~/.docker/trust/private/baba7529e7dfa46112aebe8b60817a0a5666ce440afd5cfd16066fdc34d24ff4.key | base64)

Name : DOCKER_CONTENT_TRUST_REPOSITORY_PASS PHRASE

Value : ENCODED_PASSPHRASE

Name : DOCKER_CONTENT_TRUST

Value : 1


--> Save


Configure --->

Restrict where this project can be run
Label Expression:
master
----> Save

Build now /Console Output




