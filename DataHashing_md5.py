import hashlib
import json


def data_hashing():
    with open('countries.json', encoding='utf-8') as f:
        file_json = json.load(f)
        for dictionary in file_json:
            countries = dictionary['name']['common']
            hash_object = hashlib.md5(str.encode(countries))
            yield hash_object.hexdigest()


for hashed_data in data_hashing():
    print(hashed_data)
