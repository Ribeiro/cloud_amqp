import pika, os, logging
logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://ohnqmmap:D0B8NCh_JXpoQiy_Untg8PMiLAc7kk7K@jellyfish.rmq.cloudamqp.com/ohnqmmap')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel


# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  print " [x] Received %r" % (body)

# set up subscription on the queue
channel.basic_consume(callback,
    queue='input_queue',
    no_ack=True)

channel.start_consuming() # start consuming (blocks)

#connection.close()