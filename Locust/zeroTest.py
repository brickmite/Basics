from locust import HttpLocust, TaskSet, task
import zeroLib, websocket

class UserBehavior(TaskSet):
    tasks = {
        zeroLib.dashboard: 1,
        zeroLib.clients: 1,
        zeroLib.downloads: 1,
        zeroLib.winDownload: 1,
        zeroLib.linDownload: 1,
        zeroLib.administration: 1,
        zeroLib.detective: 1
    }

    def on_start(self):
        zeroLib.login(self)
    
    def on_stop(self):
        zeroLib.logout(self)

class WebsiteUser(HttpLocust):
    host = "http://mnl406win:8888"
    task_set = UserBehavior
    max_wait = 15000
    min_wait = 5000