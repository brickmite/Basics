#cd C:\Users\dancheta\Documents\Tools\Scripts\StartUp   For CMD Execution
#C:\Users\dancheta\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup    Boot Folder Location

#Import Libraries
import webbrowser
import subprocess
import time

#Set Global Variables
progs = [
    'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE',
    'D:\\KeePass-2.43\\KeePass.exe',
    'C:\\Program Files (x86)\\Mobatek\\MobaXterm\\MobaXterm.exe'
]

links = [
    'https://timesheet.openit.com/Timesheet#!/',
    'https://openitonline.sharepoint.com/:x:/r/employee_info/_layouts/15/guestaccess.aspx?rtime=Jc2dcC8710g&share=EZEevVDSKTpKvEGufWCqnO4BPjIVYDbFX6QGcfSArnPmgQ',
    'http://git/openit/zero/-/boards',
    'https://openitonline.sharepoint.com/:x:/r/employee_info/_layouts/15/Doc.aspx?sourcedoc=%7B012462D0-3DEE-4E1E-8C3D-4EE6DD8B5C3A%7D&file=Centralized%20Test%20Cases.xlsm&action=default&mobileredirect=true&cid=b802fdd2-6a6b-49a3-9ff7-f0a5e9eb2704',
    'http://localhost:8089/',
    'http://mnl406win:8888/'
    # 'http://mnl326win:8888/'
]

#Create Functions or Methods

    #Login to links???
    #First thing you do???

#Execute
time.sleep(10)

for x in range (len(progs)):
    subprocess.Popen([[progs[x]]])

for i in range (len(links)):
    webbrowser.open(links[i], new=1)