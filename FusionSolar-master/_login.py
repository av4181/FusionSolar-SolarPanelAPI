import requests

user = 'De_Haes_API'
password = 'Sveasolar2023!'

session = requests.session()
session.headers.update({'Connection': 'keep-alive', 'Content-Type': 'application/json'})

url = f'https://eu5.fusionsolar.huawei.com/thirdData/login'
body = {
    'userName': user,
    'systemCode': password
}

session.cookies.clear()
r = session.post(url=url, json=body)
r.raise_for_status()

print(r.cookies.get(name='XSRF-TOKEN'))