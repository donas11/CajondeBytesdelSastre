# comandos
Anotaciones comandos

# Docker 
* ## Mover archivos del contenedor al Host
  ```docker cp NombreContenedor:RutaContenedor RutaHost/Archivo```
* ## Mover archivos del Host al contenedor
  ```docker cp RutaHost/Archivo NombreContenedor:RutaContenedor/Archivo```




# Personalización Custumize pantalla inicio

### nombre icono version 20.04
```launcher_bfb.png```     
### Carpeta icono inicio 
 ```/usr/share/unity/icons/```
### Archivo a Modificar
```/lib/plymouth/themes/ubuntu-logo/ubuntu-logo.script```
### Lineas del archivo que modificar 
```Window.SetBackgroundTopColor (0.0, 0.00, 0.0); # Nice colour on top of the screen fading to ```
```Window.SetBackgroundBottomColor (0.0, 0.00, 0.0); # an equally nice colour on the bottom ```
### Actualizar el imitramfs 
```sudo update-initramfs -u```

## Icono iniciador en versiones antiguas
```/usr/share/plymouth```  

```gksudo /opt/extras.ubuntu.com/menulibre/bin/menulibre```
```Gnome-tweak-tool```
```unity tweak tool```

```sudo apt install gnome-tweak-tool```
```gnome-tweak-tool```

```sudo gedit /usr/share/icons/default/index.theme```


```sudo apt-get install plymouth-theme*```
```sudo apt-get install plymouth```
```sudo update-alternatives --config default.plymouth```

```sudo update-initramfs -u```


## Make a temporary text file using vim/gedit/cat/whatever
```cat > vaio.po```
```msgid "Ubuntu Desktop"```
```msgstr "VA10 OS"```

```cd /usr/share/locale/en/LC_MESSAGES```
```sudo msgfmt -o unity.mo /vaio.po```

