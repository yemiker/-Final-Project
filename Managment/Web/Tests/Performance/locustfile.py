from locust import HttpUser, task

class Load(HttpUser):
    @task
    def login_user(self):
        self.client.get("https://qa-admin.trado.co.il")