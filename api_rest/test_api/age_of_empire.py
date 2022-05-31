import requests

def test_valida_1():

    url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/1/re'
    r = requests.get(url)

    assert True if r.status_code == 200 else False, r.status_code

    #print(r.status_code)

    #print(r.json())