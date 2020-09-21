from api_check import inventory_api,backup_api
import time
import xmltodict
import threading
import webpage_check
import alarm

ring = threading.Event()
ring.clear()

def nvidia_api():
    while 1:
        try:
            r = inventory_api()
            if r is not None:
                #print(r.status_code)
                if r.status_code >= 200 and r.status_code < 300:
                    r_dict = xmltodict.parse(r.text)
                    inventory_status = r_dict.get('inventoryStatus').get('status')
                    if inventory_status != 'PRODUCT_INVENTORY_OUT_OF_STOCK':
                        print(inventory_status)
                        ring.set()
                    # else:
                    #     ring.clear()
            time.sleep(5)
        except Exception as e:
            print(e)

def nvidia_backup():
    while 1:
        try:
            r = backup_api()
            if r is not None:
                #print(r.status_code)
                if r.status_code >= 200 and r.status_code < 300:
                    r_dict = r.json()
                    inventory_status = r_dict['products'].get('product')[0].get('inventoryStatus').get('status')
                    if inventory_status != 'PRODUCT_INVENTORY_OUT_OF_STOCK':
                        print(inventory_status)
                        ring.set()
                    # else:
                    #     ring.clear()
                time.sleep(5)
        except Exception as e:
            print(e)

def alarm_t():
    while 1:
        try:
            ring.wait(None)
            alarm.alarm(3)
        except Exception as e:
            print(e)

def bestbuy():
    while 1:
        try:
            if webpage_check.bestbuy_sweep() or webpage_check.other_sweep():
                ring.set()
            else:
                ring.clear()
            #print("ok")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    t1 = threading.Thread(target=nvidia_backup)
    t2 = threading.Thread(target=nvidia_api)
    t3 = threading.Thread(target=alarm_t)
    t4 = threading.Thread(target=bestbuy)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
