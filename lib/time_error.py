import requests

class TimeError:
    def __init__(self, requester, time):
        self.requester = requester
        self.time = time
    def error(self):
        return self._get_server_time() - self.time.time()
    def _get_server_time(self):
        response = self.requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]

