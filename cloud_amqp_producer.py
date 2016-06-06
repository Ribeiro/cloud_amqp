import pika, os, logging, sys
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://ohnqmmap:D0B8NCh_JXpoQiy_Untg8PMiLAc7kk7K@jellyfish.rmq.cloudamqp.com/ohnqmmap')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='input_queue') # Declare a queue
# send a message
channel.basic_publish(exchange='', routing_key='input_queue', body=sys.argv[1])
print " [x] Sent " + sys.argv[1]