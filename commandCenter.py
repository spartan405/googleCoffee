import sys

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient, Client, Data
import sys
sys.path.insert(0, '/home/pi/')
import coffee

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = sys.argv[2]
ADAFRUIT_IO_USERNAME = sys.argv[1]  # See https://accounts.adafruit.com
                                                    # to find your username.

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'googleCoffee'

aio = Client(sys.argv[1],sys.argv[2])
data = Data(value=10)
aio.create_data(FEED_ID,data)



def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    # Subscribe to changes on a feed named DemoFeed.
	
    client.subscribe(FEED_ID)

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)
	
	
#takes in value from AdafruitIO feed. THis value should change based on Google Assistant input
def message(client, feed_id, inputIO):
		
		if inputIO == '0':
			coffee.main(sysargv[3])
			delete(feed_id, 1)
		else:
			print('Feed {0} recieved new value: {1}'.format(feed_id,inputIO))
		
		
		
# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
while True:
    try:
        client.connect()
        break
    except:
       print('connection error')
	
# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
client.loop_blocking()