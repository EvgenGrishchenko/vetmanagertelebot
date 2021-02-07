import requests
from datetime import datetime
from datetime import timedelta
config = { 'name':'your bot name',
        'token':'your bot token',
        'vettoken':'your vetmanager API token',
        'domain':'your domain vetmanager '
       }
def kon_post_animal(spi, animal):
    url = "https://"+config['domain']+".vetmanager.ru/rest/api/pet"

    payload = {"owner_id": spi
        , "alias": animal
        , "skip_checking": "1"
               }
    headers = {'Content-Type': 'application/json',
               "X-REST-API-KEY": config['vettoken'],
               'cache-control': 'no-cache'
               }
    response = requests.request("POST", url, headers=headers, data=payload)
    pet_lists = response.json()
    return pet_lists
def kon_post_client(surname,name,middle):
    url = "https://" + config['domain'] + ".vetmanager.ru/rest/api/client"
    payload = {"last_name": surname
        , "first_name": name
        , 'middle_name': middle
               }
    headers = {'Content-Type': 'application/json',
               "X-REST-API-KEY": config['vettoken']
               }

    response = requests.request("POST", url, headers=headers, data=payload)
    clients_list = response.json()
    return clients_list
def kon_sarch_pet():
    url = "https://"+config['domain']+".vetmanager.ru/rest/api/pet"
    headers = {'Content-Type': 'application/json',
               "X-REST-API-KEY": config['vettoken'],
               'cache-control': 'no-cache'
              }
    response = requests.get(url, headers=headers)
    pet_lists=response.json()
    return pet_lists
def kon_client():
    url = "https://"+config['domain']+".vetmanager.ru/rest/api/client"
    headers = {
                "X-REST-API-KEY": config['vettoken']
                }
    response = requests.get(url, headers=headers)
    clients_list = response.json()
    return clients_list
def register(spi, pet_ids, hours):
    now = datetime.now()+ timedelta (days = 1)
    url = "https://"+config['domain']+".vetmanager.ru/rest/api/admission"

    payload = {"admission_date": now.strftime("%Y-%m-%d "+ hours +":%M:%S")
               , "admission_length":"00:20:00"
               , "status": "not_approved"
               , "client_id": spi
               , "clinic_id":"1"
               , "patient_id": pet_ids
              }
    headers = {
      "X-REST-API-KEY": config['vettoken']
    }
    response = requests.request("POST", url, headers=headers, data = payload)
