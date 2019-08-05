#this script get the message from the publishing queue of that channel. 


import redis
import time
r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
chnnel=input("Enter a channel to subscribe : ")
p.subscribe(chnnel)

while True:
    message = p.get_message()
    if message:
        print (message['data'])
    time.sleep(0.01)    #checks for the message in queue after every  0.01 seconds.
