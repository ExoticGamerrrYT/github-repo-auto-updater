import os
import time
import requests
from appdirs import user_data_dir
from plyer import notification
from zipfile import ZipFile
from git import Repo
import shutil

appdataDir = user_data_dir("3xotic.Dev")
textDir = os.path.join(appdataDir, "directory.txt")
desktopDir = os.path.join(os.path.expanduser("~"), "Desktop")
logFileDir = os.path.join(appdataDir, "LOG.txt")

def check_for_updates(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        return commits[0]['sha']
    else:
        print(f"Error: No se pudo obtener la información del repositorio {username}/{repo_name}.")
        return None

def notify_update():
    notification.notify(title="GitHub Update", message="¡Nuevo commit en el repositorio!", timeout=10)

def get_last_commit_sha():  # Obtenemos la carpeta de datos de la aplicación
    file_path = os.path.join(appdataDir, "last_commit.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return None

def save_last_commit_sha(sha):  # Obtenemos la carpeta de datos de la aplicación
    if not os.path.exists(appdataDir):
        os.makedirs(appdataDir)
    
    file_path = os.path.join(appdataDir, "last_commit.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(sha)

def download_github_repository(repo_url, destination_folder):
    """for file in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, file)
        os.remove(file_path)"""
    #shutil.rmtree(destination_folder, ignore_errors=True)
    try:
        # Hacer una solicitud a la API de GitHub para obtener el archivo zip del repositorio
        zip_url = repo_url.replace("github.com", "api.github.com/repos") + "/zipball"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(zip_url, headers=headers)
        
        if response.status_code == 200:
            # Guardar el archivo zip en una ubicación temporal
            zip_file_path = os.path.join(destination_folder, "temp.zip")
            with open(zip_file_path, "wb") as f:
                f.write(response.content)

            # Extraer el contenido del archivo zip omitiendo la carpeta .git
            with ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(destination_folder)

            # Eliminar el archivo zip temporal
            os.remove(zip_file_path)
            print("Repositorio descargado exitosamente.")
        else:
            print("Error al descargar el repositorio. Código de estado:", response.status_code)
    except Exception as e:
        print("Error al descargar el repositorio:", e)

def makeAllFolders():
    pass

def writeToLOG(message):
    with open(logFileDir, "a", encoding="utf-8") as file:
        file.write(message + "\n")

if __name__ == "__main__":
    username = "ExoticGamerrrYT"
    repo_name = "test-repo"
    repoUrl = "https://github.com/ExoticGamerrrYT/test-repo"

    last_commit_sha = get_last_commit_sha()
    while True:
        if not os.path.exists(appdataDir):
            os.makedirs(appdataDir)
        try:
            with open(textDir, "r", encoding="utf-8") as file:
                textOfDirText = file.read()
        except:
            file = open(textDir, "w", encoding="utf-8")
            file.write(desktopDir)
        finally:
            with open(textDir, "r", encoding="utf-8") as file:
                textOfDirText = file.read()

        if not os.path.exists(textOfDirText):
            writeToLOG(r"Error: The directory wrote in directory.txt is not valid. Go to C:\Users\<your user>\AppData\Local\3xotic_dev\3xotic_dev and change that shit.")
            os.startfile(appdataDir)
            exit()
        
        os.chdir(textOfDirText)
        if not os.path.exists("repo_download"):
            os.makedirs("repo_download")
        
        downloadFinalPath = os.path.join(textOfDirText, "repo_download")
        print(downloadFinalPath)

        os.chdir(textOfDirText)
        if not os.path.exists("repo_download"):
            os.makedirs("repo_download")
        current_commit_sha = check_for_updates(username, repo_name)
        if current_commit_sha and current_commit_sha != last_commit_sha:
            last_commit_sha = current_commit_sha
            save_last_commit_sha(last_commit_sha)
            download_github_repository(repoUrl, downloadFinalPath)
            notify_update()
        time.sleep(10)