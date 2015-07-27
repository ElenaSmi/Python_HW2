__author__ = 'Elena'

import requests
import json

def create_folder(name, domain=None, username=None,password=None, content_type=None,
                  accept=None, method=None, test_path=None):

    if domain is None:
        domain = 'https://istepanko25.qa-egnyte.com'
    if content_type is None:
        content_type = 'application/json'
    if username is None:
        username = 'admin'
    if password is None:
        password = 'apitest2'
    if method is None:
        method ='Post'
    if accept is None:
        accept = 'application/json'
    if test_path is None:
        test_path = 'Shared/smoke_test/'

    endpoint = '/public-api/v1/fs/'
    url = domain + endpoint + test_path + name
    headers = dict()
    headers['Content-Type'] = content_type
    headers['Accept'] = accept

    data = dict()
    data['action'] = 'add_folder'

    data = json.dumps(data)# translates from dict to json

    r = requests.request(
        url = url,
        auth = (username, password),
        headers = headers,
        data = data,
        method = method
    )
    return r

for i in range(10):
    resp = create_folder(name = 'test%s' % i)
    data = resp.content
    status_code = resp.status_code
    headers = resp.headers

print('\nData:\n%s\nStatus_code:\n%s\nHeaders:\n%s' % (data, status_code, headers))

def delete(domain=None, username=None, password=None, method=None, test_path=None):
#curl 'https://istepanko25.qa-egnyte.com/public-api/v1/fs/Shared/test2' -u admin:apitest2 -X DELETE -v
    if domain is None:
        domain = 'https://istepanko25.qa-egnyte.com'
    if username is None:
        username = 'admin'
    if password is None:
        password = 'apitest2'
    if method is None:
        method = 'Delete'
    if test_path is None:
        test_path = 'Shared/smoke_test/'

    endpoint = '/public-api/v1/fs/'
    url = domain + endpoint + test_path

    r = requests.request(
        url = url,
        auth = (username, password),
        method = method)
    return r

resp = delete()
status_code = resp.status_code


print('\nStatus_code:\n%s' % (status_code))
