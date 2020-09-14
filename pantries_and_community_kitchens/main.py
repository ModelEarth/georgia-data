#pip3 install these packages
import requests
import json

#The url is ridiculously long so I just made a constants file
from constants import food_bank_url, pantry_community_kitchens


def main():
    # Make get call to food bank api
    page = requests.get(url=food_bank_url)
    #transform into json object
    data = page.json()
    #check if request was successfull
    if page.status_code == 200:
        #uplpad data to json file
        upload_data_as_json(data)
        print("uploaded food bank locations to json file")
    else:
        print("Unable to access api")


def upload_data_as_json(data):
    food_banks = json.dumps(data["features"])
    f = open(pantry_community_kitchens, "w")
    f.write(food_banks)
    f.close()


if __name__ == '__main__':
    main()
