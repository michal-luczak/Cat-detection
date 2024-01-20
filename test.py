import requests

url = 'http://127.0.0.1:5000/detect-cat'

files = {'image': (open('cat1.jpg', 'rb'))}

response = requests.post(url, files=files)

print(response.text)
