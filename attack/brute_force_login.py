import requests

url = "http://localhost:8080/login"
data = {"rollno":"106121116", "password":"madhumitha"}
response = requests.post(url, json=data)
print(response.cookies)
