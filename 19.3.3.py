import requests

# GET
status = 'available'
res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print(f'Status: {res_get.status_code}\n')
print(res_get.text, '\n\n', '-' * 100)


# POST
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9222968140497181727, "category": {"id": 0, "name": "string"},
        "name": "doggie", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
res_post = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(f'Status: {res_post.status_code}\n')
print(res_post.json(), '\n\n', '-' * 100)


# PUT
headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
data_put = {"id": 9222968140497181727, "category": {"id": 0, "name": "string"}, "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}], "status": "available"}
res_put = requests.put('https://petstore.swagger.io/v2/pet', headers=headers_put, json=data_put)
print(f'Status: {res_put.status_code}\n')
print(res_put.json(), '\n\n', '-' * 100)


# DELETE
res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{9222968140497181727}', headers={'accept': 'application/json'})
print(f'Status: {res_delete.status_code}\n')
print(res_delete.json())
