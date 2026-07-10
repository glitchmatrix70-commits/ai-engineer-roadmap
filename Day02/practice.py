import requests
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

data = response.json()

print("Task 1")
print("Name -> " + data['name'])
print("Email -> " + data['email'])
print("Phone -> " + data['phone'])
print("Company -> " + data['company']['name'])

print("*" * 20)
response1 = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data1 = response1.json()

print("Task 2")
print("Title -> " + data1['title'])
print("Completed -> " , data1['completed'])