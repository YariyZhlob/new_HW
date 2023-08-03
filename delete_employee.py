import requests


API_URL = 'http://127.0.0.1:5000/employees'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1cGVydXNlciJ9.TFbOhuR_QuXdrgYCLHOXibp_OW_ZNGgsozTo0130dVw'
ID_DELETED_EMPLOYEE = str(4)
FINAL_URL = API_URL + '/' + ID_DELETED_EMPLOYEE


headers = {'Authorization': f'Bearer {BEARER_TOKEN}', 'Content-Type': 'application/json'}

# data = {
#         "name": "Andrey",
#         "organization": "IT",
#         "role": "QA"
# }


response = requests.delete(url=FINAL_URL, headers=headers) #,json=data)

print(response.status_code)
print(response.json())

def test_deleted_employee():
    assert response.status_code==200
    assert response.json()['message']=='Employee deleted'