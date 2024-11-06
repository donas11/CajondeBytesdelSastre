---
title: Git
created: '2024-10-26T22:34:37.906Z'
modified: '2024-11-01T02:30:26.589Z'
---

# Git
Es un control de versiones
## Ventajas
* No borra ,añade información
* Integridad

#Instalación:
```apt-get install git```
or
```https://git-scm.com/download/linux ```

## Crear un nuevo repositorio
```git init```
## Git status
```git status```
* Tracked
* Ignored
* Untracked
## Config user

``` git config --global user.name "user"```
``` git config --global user.email "user@email.com"```
``` git config --global --list"```
``` git config --list"```
## Añadir
```git add archivo```
```git add ```
```git add .```
```git add --all```
```git remote add origin ```
## eliminar
desde el working directory
```git rm archivo```
```git rm -f ```
desde el index (Staging area)
```git rn --cached archivo```

## mover 
(like a swap)
```mv stuff newstuff```
```git rm stuff```
```git add newstuff```
or 
```git mv stuff newstuff```
## Commit
```git commit ```
---> ```Mensaje ```
or
```git commit -m "Mensaje"```
```git commit -a```
```git commit -all```

## Archivos .gitignore
exemplo de archivo .gitignore xD
```
T-1_config.yaml
T-1_training_notes.ipynb
T-600_weights.pt
T-600_data.json
T-700_train.py
T-700_structure.json
T-800_weights.bin
T-800_inference.onnx
T-850_hyperparameters.yaml
T-850_evaluation.ipynb
T-888_model.onnx
T-888_tokens.json
T-900_model.bin
T-900_config.yaml
T-1000_adaptation.onnx
T-1000_skills.json
T-X_architecture.yaml
T-X_inference_config.json
Rev-9_data.json
Rev-9_weights.ckpt
T-3000_config.yaml
T-3000_model_weights.pt
T-5000_testing.yaml
T-5000_dataset.json
```


## · estados
Work dictory Project Dictory /Working tree --> Staging area /Index / Cache --> (Local Repository) Commit
In Staging area can:
```git restore --staged```
```git rm cached```
```git restore --staged archivo.md```
```git restore add -p```

##  Historial de commits
```git log```
```git show d49b8c495137d3045ae6d5166efbd432678bcf59```
```git show d49b8c495137d3045ae6d5166efbd432678bcf59:readme.md```
```git log```
```git log --summary```
```git log --oneline```


## Remote Clone
```git remote -v```
```git remote remove origin```
```git remote add origin https://github.com/donas11/CajondeBytesdelSastre.git ```
```git remote add origin ssh://git@github.com/donas11/CajondeBytesdelSastre.git```
```git remote set-url origin ssh://git@github.com/donas11/CajondeBytesdelSastre.git```
tambien sirve como el init
```git clone https://github.com/donas11/CajondeBytesdelSastre.git ```

## branch
list branchs
```git branch ```
List branch remote and local
``` git branch -a ```
Muestra la rama actual
```git show-branch ```
checking/Changing out branch
```git chekout branchname```
Creating too
```git chekout -b branchname``` 

Creating a branch
```git branch newbranch```
Creating a branch y nos cambia a ella
```git checkout -b branchname```
Clone a remote branch y nos cambia a ella
```git checkout -b branchname origin/branchname```
Renombrar
```git branch -m oldbranchname branchname```
Deleting a branch
```git branch -d branchname```
Diferencia entre branchs
```git diff Initial_branch Final_branch```
Cambia a la rama
```git checkout branchname```
Cambia a una rama activa
```git checkout -	```
Descarta cambios el nombre
```git checkout -- archivo```

```git config --global init.defaultBranch main```


## Merges
La activa con la rama concreta
```git merge name_other_branch```
Cobina dos ramas
```git merge inital_branch final_branch```



## Push 
En la rama actual
```git push``` 	
rama local ---> al remoto
```git push origin mybranch ```
rama local ---> al remoto y se posicion en la rama en git
```git push -u origin mybranch ```
Elimina la rama remota
```git push origin --delete mybranch```

## Pull 
```git pull	```
```git pull origin mybranch ```



## Generate SSH Key for github
In client pc
```cd ~/.ssh```
``` ssh-keygen -t rsa -C "email@email_server.com" ```
```clip < ~/.ssh/id_rsa.pub```
 In server (github)
Settings -->  SSH and GPG Keys --> new SSH Key --> add SSH Key


## was sind die bestandteile von github? ¿Cuáles son los componentes de github?
##### Projekt,Repository,Verzeichnis --> Zugriffsrechte  < -- Organiationen & Teams Bilden
* Github-pages
* versionverwaltung (gestión de versiones)
* code hosting (alojamiento de código)
* Issues (Asuntos)
* Wiki

## Issue Report Template example:
```
### 🐞 Issue Report Template

**Título:**  
_Breve descripción del problema (ej., "Error al cargar la página de inicio en dispositivos móviles")._

---

#### 📋 Descripción

**Descripción del problema:**  
_Descripción breve del problema encontrado._

**Pasos para reproducir:**  
1. _Paso 1: Ir a la página o sección..._
2. _Paso 2: Realizar la acción..._
3. _Paso 3: Describir el resultado._

**Comportamiento esperado:**  
_Describe lo que debería ocurrir en lugar del problema._

---

#### 🖥️ Información Técnica

- **Versión del software:**  
- **Sistema operativo:**  
- **Navegador y versión (si aplica):**  

---

#### 📸 Capturas de pantalla o Videos

_Agrega capturas o videos aquí._

---

#### 📄 Archivos de Log (si aplica)

_Adjunta archivos de log relevantes aquí._

---

#### 📋 Información Adicional

_Cualquier otra información relevante._

```
## deshacer cambios en local
* los últimos cambios
```git stash```
* todos los cambios
```git stash clear```



## deschacer commit 
Hacerle mas cambio añadir comentario 
```git commit --amend -m "Cambio en la version```
* si estan los cambios en local y no has hecho push 
  * manteniendo los cambios
```get reset --soft HEAD~1```
  * sin  mantener los cambios
```get reset --hard HEAD~1```
* Si has hecho push al repositorio
encontramos el id del commit hecho
```git log --oneline```
y utilizamos:  
```git revert id_commit ```
