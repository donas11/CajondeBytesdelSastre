---
title: DEVOPS CI / CD Agile
created: '2024-10-25T00:49:23.900Z'
modified: '2024-10-25T23:55:31.359Z'
---

# DEVOPS CI / CD Agile
## Continuos Integration
* hace un merge de todo el codigo de trabajo en el branch master
* Reviews de Codigo, Compile /build ,Test unitarios, Test de Integración

## Continuous Delivery
* Deploy a Servidores de Test
  * UAT (User Acceptance Testing),QA (Quality Assurance)
* construcciones son Entregadas a traves del life Cycle

## Continuos Deployment 
  * Deploy a Servidor de producción o release

## Software development life cycle 
CODE > BUILD > TEST > RELEASE > DEPLOY > OPERATE > MONITOR > PLAN > CODE

Dependiendo del Proyecto a realizar las herramientas pueden estar en diferentes lugares Por ejemplo Docker puede estar en build o en deploy

### Code 
  #### Tools 
    * Gitlab
    * git
    * gitea
    * Confluence
    * Jira Software
  
### Build
  #### Tools
    * npm
    * gradle  
    * docker
    * maven
    * sbt
  
### Test
  #### Tools
    * Mocha
    * Jest
    * Junit 5
    * cucumber
    * Selenium Testing

### Release
  #### Tools
    * Jenkins
    * Circle CI
    * AWS CodeDeploy
    * Codeship

### Monitor
  #### Tools
    * Nagios
    * splunk
    * datadog
    * Amazon CloudWatch

### Operate
  #### Tools
    * Kubernetes
    * Amazon EKS
    * Google Kubernetes Engine (EKS)
    * AWS ECS
    * Ansible

### Deploy
  #### Tools
    * AWS
    * Google CLoud
    * Helm
    * Ansible
    * Docker
    * DC/OS

### Plan
  #### Tools
    * Confluence
    * Jira Software
    * Trello

## Waterfall Model (SDLC)
* Requeriments Collection 
  * Project Manager ->Client
* Analysis 
  * Equipo -> PM -> cliente
* Design 
  * Arquitects -> equipo
* Building 
  * Equipo
* Validator
  * Equipo
* Packaging
  * Equipo -> cliente



