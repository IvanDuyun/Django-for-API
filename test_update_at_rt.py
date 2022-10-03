import requests
import json

with open('refresh_token.txt', 'r') as file:
    rt_last = file.read()

with open('access_token.txt', 'r') as file:
    at_last = file.read()

param = {
          "client_id": "386b971b-3607-4c15-802b-ccafcf7b0453",
          "client_secret": "YmbDsds6C2B25C2raGgpEaI2Kqxk78ZO7v3b4hFTljqRi6WazqmfDfrOjTDPhj1R",
          "grant_type": "refresh_token",
          "refresh_token": rt_last,
          "redirect_uri": "https://terabit.ai/"
        }

req = requests.post("https://alinev.amocrm.ru/oauth2/access_token", data=param)
req = req.json()
rt = req['refresh_token']
at = req['access_token']

if not (at == at_last and rt == rt_last):
    print('токены обновились')

with open("refresh_token.txt", "w") as file:
    file.write(rt)

with open("access_token.txt", "w") as file:
    file.write(at)