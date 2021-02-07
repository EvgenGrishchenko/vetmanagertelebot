import vetconnect
import setup
from datetime import datetime
from datetime import timedelta

def write_client(message, surname, name, middle, animal, time):
    def create_client(message):
        clients_list = vetconnect.kon_post_client(surname, name, middle)
        client_list = list(filter(
            lambda clien_list: clien_list['last_name'] == surname and clien_list['first_name'] == name and clien_list[
                'middle_name'] == middle, clients_list['data']['client']))
        if len(client_list) == 0:
            create_client(message)
        else:
            for lis in client_list:
                if lis['last_name'] == surname and lis['first_name'] == name and lis['middle_name'] == middle:
                    spi = lis['id']
                    check_pet(message, spi, animal)
                else:
                    write_client(message, surname, name, middle, animal, time)
    def create_pet(message, spi, animal):
        pet_lists = vetconnect.kon_post_animal(spi, animal)
        tes = str(spi)
        pet_list = list(filter(lambda petlist: petlist['alias'] == animal and petlist['owner_id'] == tes, pet_lists['data']['pet']))
        if len(pet_list) == 0:
            create_pet(message, spi, animal)
        else:
            for lis in pet_list:
                if lis['alias'] == animal:
                    pet_ids = lis['id']
                    register(message, spi, pet_ids, time)
                else:
                    write_client(message, surname, name, middle, animal, time)
    def register(message, spi, pet_ids, time):
        hours = time
        vetconnect.register(spi, pet_ids, hours)
        now = datetime.now() + timedelta(days=1)
        tim = now.strftime("%Y-%m-%d " + hours + ":%M:%S")
        setup.mes(message, tim, surname, name, middle, animal)
    def check_pet(message, spi, animal):
        pet_lists = vetconnect.kon_sarch_pet()
        tes = str(spi)
        pet_list = list(filter(lambda petlist: petlist['alias'] == animal and petlist['owner_id'] == tes, pet_lists['data']['pet']))
        if len(pet_list) == 0:
            create_pet(message, spi, animal)
        else:
            for lis in pet_list:
                if lis['alias'] == animal:
                    pet_ids = lis['id']
                    register(message, spi, pet_ids, time)
                else:
                    write_client(message, surname, name, middle, animal, time)
    def search_client(message):
        clients_list = vetconnect.kon_client()
        client_list = list(filter(lambda clien_list: clien_list['last_name'] == surname and clien_list['first_name'] == name and clien_list['middle_name'] == middle, clients_list['data']['client']))
        if len(client_list) == 0:
            create_client(message)
        else:
            for lis in client_list:
                if lis['last_name'] == surname and lis['first_name'] == name and lis['middle_name'] == middle:
                    spi = lis['id']
                    check_pet(message, spi, animal)
                else:
                    write_client(message, surname, name, middle, animal, time)
    search_client(message)