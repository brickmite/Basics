import zipfile36
import shutil
import sys
import threading
import itertools
import os
import wget
import socket
from time import sleep

download_url = r"http://git/openit/zero/-/jobs/artifacts/master/download?job=build%20server"
download_path = r"C:\Users\dancheta\Downloads"
download_zip = r"C:\Users\dancheta\Downloads\artifacts.zip"
serverPath = [
    r"\\MNL548WIN\Users\dancheta\Desktop\CLIMS_Installers",
    # r"\\MNL785WIN\Users\dancheta\Desktop\CLIMS_Installers",
    r"C:\Users\dancheta\Downloads\CLIMS_Installers"
    ]

done = False

def loading():
    sys.stdout.write("\n")
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write("\rUnzipping Files... " + c)
        sys.stdout.flush()
        sleep(0.2)

def cleanUp():
    os.remove(download_zip)

try:
    print("Downloading the installer...")
    wget.download(download_url, download_path)

    for x in range(len(serverPath)):
        t = threading.Thread(target=loading)
        t.start()
        sourceMsi = serverPath[x] + r"\OpeniTCLIMSServer.msi"
        newMsi = serverPath[x] + r"\OpeniTCLIMSServer_.msi"
        sourceLog = serverPath[x] + r"\changelog.txt"
        newLog = serverPath[x] + r"\changelog_.txt"
        with zipfile36.ZipFile(download_zip, "r") as z:
            z.extractall(serverPath[x])
        shutil.move(sourceMsi , newMsi)
        shutil.move(sourceLog, newLog)
        sleep(10)

except FileNotFoundError as error:
    done = True
    print("\rUnzip Failed! %s!\nPlease check: %s" % (error.strerror, error.filename))
    cleanUp()

else:
    done = True
    print("\rUnzip was successful!")
    cleanUp()