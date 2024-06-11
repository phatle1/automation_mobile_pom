from pathlib import Path

from locust import HttpUser, TaskSet, task, between

parent_path = Path(__file__).resolve().parents[0]
token_file = f'{parent_path}/token.txt'

token = open(token_file, "r").read()


headers = {
    'Accept': 'Application/Json',
    'Authorization': 'Bearer {}'.format(token)
}


print(f'token{token}')

print(f'headers{headers}')