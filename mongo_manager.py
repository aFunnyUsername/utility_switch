from pymongo import MongoClient 
from sshtunnel import SSHTunnelForwarder
import time


def connect_to_remote():
    server = SSHTunnelForwarder(
        ('98.240.156.58', 3232),
        ssh_username='jakem',
        ssh_password='kanyEwEst808!',
        remote_bind_address=('127.0.0.1', 27017))
    
    server.start()
    time.sleep(3)

    client = MongoClient('127.0.0.1', server.local_bind_port)

    return server, client





def connect_to_mongo():
    return None 

def to_mongo(data):
    server, client = connect_to_remote()

    db = client['UTIL_SWITCH_DB']  

    for service_area in data:
        coll = db[service_area]
        plans = data[service_area] 
        for plan in plans:
            coll.insert({'supplier': plan})

    server.close()
    client.close()
    return None





