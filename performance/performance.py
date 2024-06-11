from pathlib import Path

from locust import HttpUser, TaskSet, task, between


class UserTaskSet(HttpUser):
    wait_time = between(1, 2)
    host = "https://dev.api.hutbot.pizzahut.io/"

    def on_start(self) -> None:
        print('load test started')
        payload = {
            #     payload here
        }

    @task
    def get_api(self):
        parent_path = Path(__file__).resolve().parents[0]
        token_file = f'{parent_path}/token.txt'
        token = open(token_file, "r").read()
        headers = {
            'Accept': 'Application/Json',
            'Authorization': 'Bearer {}'.format(token)
        }
        with self.client.get("/v1/activity-feeds/feeds?offset=0&pageSize=20",
                             name="Get Feed",
                             catch_response=True,
                             headers=headers) as response:
            if response.status_code == 200:
                value = response.json()
                print(value)
                response.success()
            else:
                response.failure("Failed")

    def on_stop(self):
        print('Finished')
