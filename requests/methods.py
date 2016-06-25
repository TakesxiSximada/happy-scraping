import requests
url = 'http://127.0.0.1:8888'

res = requests.get(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.post(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.put(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.patch(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.head(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.delete(url)
print(res.headers['receive'])
print(res.content)
print()

res = requests.options(url)
print(res.headers['receive'])
print(res.content)
print()
