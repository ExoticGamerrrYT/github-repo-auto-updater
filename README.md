# GitHub Repo Auto-Downloader
## What is this?
This is a program that each time a commit is pushed to a repo the script notifies and downloads it. Also it makes folders in ``LOCALAPPDATA`` and in ``Desktop``.

## ¿Que hace esto?
1. Si existe una carpeta llamada ``3xotic_dev``, no se hace nada, en el caso de que si exista se creará.
2. Si dentro de esa carpeta hay un archivo llamado ``directory.txt`` se mira si tiene algo escrito, si no tiene nada escrito se escribirá la ruta hacia el escritorio y si tiene una ruta se usa esa, en el caso de que la ruta no funcione se escribe al archivo LOG el error, se abre la carpeta del archivo ``directory.txt`` y se cierra el programa (``exit()``). Si no hay archivo ``directory.txt`` se crea y se escribe la ruta hacia el escritorio.
3. Se lee la ruta escrita en ``directory.txt`` y se usa para descargar el repositorio.

## License
This is under Creative Commons license. If you want to modify something you will need to follow the same license and my name and a link to my GitHub profile will hve to appear somewhere. You cant make benefits from this project.

<p align="center">
    <img src="images/creativecommons.svg" width="50" height="50">
</p>

### Contact
Discord: ``3xotic.``