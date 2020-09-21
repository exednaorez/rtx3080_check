import requests


def inventory_api():
    endpoint = "https://api.digitalriver.com/v1/shoppers/me/products/5438481700/inventory-status"
    header = {"apiKey": "9485fa7b159e42edb08a83bde0d83dia"}
    try:
        r = requests.get(url=endpoint,headers=header, timeout=10)
        return r
    except:

        return None

def backup_api():
    endpoint = "https://in-and-ru-store-api.uk-e1.cloudhub.io/DR/products/en_us/USD/5438481700"
    try:
        r = requests.get(url=endpoint, timeout=10)
        return r
    except:
        return None