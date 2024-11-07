import requests

# GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())

# POST-запрос
new_post = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print(response.json())

# PUT-запрос
update_post = {'id': 1, 'title': 'updated title', 'body': 'updated body', 'userId': 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=update_post)
print(response.json())

# DELETE-запрос
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)  # Ожидается код 200 или 204




