#this script publish the message to a particular channel

import redis
queue = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = queue.pubsub()

ch=input("Enter the channel to publish")
mssg=input("Enter the message to publish") 
queue.publish(ch,ch+" says : "+mssg)

