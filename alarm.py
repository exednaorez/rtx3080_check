# from insteonplm import InsteonBytePLM

# bridge = InsteonBytePLM("COM4")
# bridge.start()

def alarm(times):
    # global bridge
    # bridge.write_command(plm_msg='770'+str(times))

    # TODO: Put your favorite way to notify you here
    print("OMG STOCK")

if __name__ == '__main__':
    print(alarm(3))