from locust import HttpLocust, TaskSet, task
import websocket

def login(self):
    self.client.post("/login", {"username": "admin","password": "admin"})

def logout(self):
    self.client.post("/logout", {"username": "admin","password": "admin"})

def dashboard(self):
    self.client.get("/")

def clients(self):
    self.client.get("/clients")

def downloads(self):
    self.client.get("/downloads")

def winDownload(self):
    self.client.get("/downloads/OpeniTCLIMSClient.msi")

def linDownload(self):
    self.client.get("/downloads/OpeniTCLIMSClient-linux-x64.rpm")

def administration(self):
    self.client.get("/administration")

def detective(self):
    self.client.get("/jobs/reccurring/REQ_STATUS")

#add websocket connections: e.g. Client connect or disconnect
#use api mapping tools or the tool used by the squad for api documentation