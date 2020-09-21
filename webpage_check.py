import requests

BESTBUY_3080_URL = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
BESTBUY_GIGABYTE_3080_URL = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-10g-gddr6x-pci-express-4-0-graphics-card-black/6430621.p?skuId=6430621"
BESTBUY_EVGA_3080_URL = "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6432399.p?skuId=6432399"
EVGA_3080_URL = "https://www.evga.com/products/product.aspx?pn=10G-P5-3881-KR"
NEWEGG_ASUS = "https://www.newegg.com/asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453?Description=rtx%203080&cm_re=rtx_3080-_-14-126-453-_-Product"

NV_SHOP_URL = "https://www.nvidia.com/en-us/shop/geforce/?page=1&limit=9&locale=en-us&search=3080"

not_sold_out = "https://www.bestbuy.com/site/nvidia-geforce-rtx-2070-super-8gb-gddr6-pci-express-3-0-graphics-card-black-silver/6361328.p?skuId=6361328"


def get_url_text(location):
    endpoint = location
    header = {
        'User-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    try:
        r = requests.get(url=endpoint, headers=header, timeout=10)
        return r.text
    except:
        return None


def bestbuy_sweep():
    evga = get_url_text(BESTBUY_EVGA_3080_URL)
    fe = get_url_text(BESTBUY_3080_URL)
    giga = get_url_text(BESTBUY_GIGABYTE_3080_URL)
    if evga is None:
        return False
    elif "Sold Out</button>" not in evga:
        print("EVGA stock")
        return True
    if fe is None:
        return False
    elif "Sold Out</button>" not in fe:
        print("FE stock")
        return True
    if giga is None:
        return False
    elif "Sold Out</button>" not in giga:
        print("GIGABYTE stock")
        #
        return True
    return False


def other_sweep():
    evga = get_url_text(EVGA_3080_URL)
    newegg_asus = get_url_text(NEWEGG_ASUS)
    # print(evga)
    if evga is None:
        return False
    elif "Out of Stock" not in evga:
        print("EVGA official stock")
        return True
    if newegg_asus is None:
        return False
    elif "OUT OF STOCK" not in newegg_asus:
        print("newegg ASUS stock")
        return True
    return False
