import pytest
import requests


BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1cGVydXNlciJ9.TFbOhuR_QuXdrgYCLHOXibp_OW_ZNGgsozTo0130dVw'

case_1 = ['1',{'employeeId': 1, 'name': 'Mikhail', 'organization': 'Accounting', 'role': 'Accountant'}]
case_2 = ['2',{'employeeId': 2, 'name': 'Ivan','organization': 'Support','role': 'senior_engineer'}]
case_3 = ['3', {'employeeId': 3, 'name': 'Anton', 'organization': 'Marketing', 'role': 'Marketer'}]

@pytest.mark.parametrize('emp_id, resp_result', (case_1, case_2, case_3), ids=['first_employee', 'second_employee', 'third_employee'])
def test_get_first_employee(emp_id, resp_result):
    API_URL = f'https://employees-api-i9ae.onrender.com/employees/{emp_id}'
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    response = requests.get(url=API_URL, headers=headers)
    resp_json = response.json()
    assert resp_json == resp_result, f'expected {resp_result} is not equal to {resp_json}'


# def test_get_second_employee():
#     API_URL = 'http://127.0.0.1:5000/employees/2'
#     result = {'employeeId': 2, 'name': 'Ivan','organization': 'Support','role': 'senior_engineer'}
#     headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
#     response = requests.get(url=API_URL, headers=headers)
#     resp_json = response.json()
#     assert resp_json == result, f'expected {result} is not equal to {resp_json}'

'''сделать single parametrize и multiple parametrize'''

