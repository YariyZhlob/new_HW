import requests


API_URL = 'http://127.0.0.1:5000/employees/1'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1cGVydXNlciJ9.TFbOhuR_QuXdrgYCLHOXibp_OW_ZNGgsozTo0130dVw'

headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}

response = requests.get(url=API_URL, headers=headers)

print(response.status_code)
print(response.json())