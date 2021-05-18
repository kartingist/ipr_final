import requests
import random
import pytest
import json

login=['user'+str(random.randint(30000, 39999))]

@pytest.mark.parametrize('login', login,  scope='function')
def test_api_user_registration(login):
    response=requests.post('http://users.bugred.ru/tasks/rest/doregister',
                  data={'email': f'{login}@gmail.com', 'name': f'{login}', 'password': '123'})
    resp = response.json()
    if f'{login}@gmail.com' in response.text and 'error' not in response.text:
        pass
    else:
        assert False, resp['message']


@pytest.mark.parametrize('login', ['user'+str(random.randint(30000, 39999))],  scope='function')
def test_api_registration_no_pass(login):
    response=requests.post('http://users.bugred.ru/tasks/rest/doregister',
                  data={'email': f'{login}@gmail.com', 'name': f'{login}', 'password': ''})
    resp = response.json()
    if 'error' not in response.text:
        assert False, 'удалось зарегистрироваться без пароля, ответ сервера: '+ response.text
    else:
        assert False, resp['message']
#
@pytest.mark.parametrize('login', login)
@pytest.mark.parametrize('pwd',[('123'), ('')])
def test_api_dologin(login, pwd):
    data={'email': f'{login}@gmail.com', 'password': pwd}
    response=requests.post('http://users.bugred.ru/tasks/rest/dologin',json.dumps(data))
    resp = response.json()
    if resp['result'] ==False:
        assert False, 'авторизация не удалась, некорректные данные'
    # print(resp['result'])


@pytest.mark.parametrize('login', login)
def test_api_del_user(login):
    data={'email': f'{login}@gmail.com'}
    response=requests.post('http://users.bugred.ru/tasks/rest/deleteuser',json.dumps(data))


@pytest.mark.parametrize('login', login)
@pytest.mark.parametrize('email', [f'{login}@gmail.com', ''])
def test_api_CreateUser(login, email):
    data={'email': f'{login}@gmail.com',
          "name": login,
          "tasks": [12],
          "companies": [36,37]}
    response=requests.post('http://users.bugred.ru/tasks/rest/CreateUser',json.dumps(data))
    resp= response.json()
    if 'error' in response.text:
        assert False, resp['message']





