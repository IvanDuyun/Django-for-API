import requests
import json

param = {
            "client_id": "386b971b-3607-4c15-802b-ccafcf7b0453",
            "client_secret": "YmbDsds6C2B25C2raGgpEaI2Kqxk78ZO7v3b4hFTljqRi6WazqmfDfrOjTDPhj1R",
            "grant_type": "authorization_code",
            "code": "def50200f0ac7ac81dc75c614202fb5b4e5eba7dd53a38d8531a7569b9bfe16e82192b82fdaf8f16b357c02e40bbd382095e5896a4a3a70731a81621e2aa564df104a7ab7b05078a827a1a629526f9082ccadc3963e4abc54c76e30973eb315a1738b8b190c41ca7ee34753a45facf6186c8309fe7c9c2cb891791f8607c7e0b758bad38ff83746d28bf4e76dc9f9772eee95825c0e849fcada16c3242db40732ede09ff8a60872947da7af4669107258b20ef59b272230107f9c409442a3379c08694780d1e9f05bba6603ffb668b460949854792b37952ff4cc38b7486a27013f1038ea87c0e929a634eb5ee837c0060f78ce93e444fe208beb89a92c801419f8c9f48e8a08c61388265b0d0e1d9fc359b17727435369fdf06c99a46630513f649331a7533a9a0625c322baba9d5268d8f1bff355d5001eadac09ca2ad116acbdfd53d5e2d366aae868277d113dbe9d38f57414151f11a29b6f74b976f79cee39f3f544ca4c8153777656c4eb0a23ccf2035dfc46ec2e73a2091e92d43013744db50b74b3b814b3cd25fa40f33ba6a8763586fc3514495aaa3df877c1e4c34fc56c9e40d14b6ddf26d83cae121bc6537e91795632f2e0e779bfb14c602197a52e5309f2fcb2f1a2736ce267f86e417d1083b5c73",
            "redirect_uri": "https://terabit.ai/"
         }

req = requests.post("https://alinev.amocrm.ru/oauth2/access_token", data=param)
req = req.json()
rt = req['refresh_token']
at = req['access_token']

with open("refresh_token.txt", "w") as file:
    file.write(rt)

with open("access_token.txt", "w") as file:
    file.write(at)