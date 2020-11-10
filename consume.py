import json
from kafka import KafkaConsumer


def format_dict():
    '''
    Summary:
            - Take the message and format into a dict of structure {'flight_id' : {'lat' : lat, 'long' : long}, ... }
    '''

    return None

def print_nicely(my_dict):
    '''
    Summary:
            - Print things out nicely
    '''

    for entry in my_dict:
        print("New Entry: %s | Latitude %.3f | Longitude %.3f" % (entry, my_dict['lat'], my_dict['lon']))

    return None


def main():

    consumer = KafkaConsumer('adsb-data', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

    for message in consumer:

        # Decode the received message
        ascii_msg = message.value.decode('ascii')
        # Do some formatting
        ascii_msg = ascii_msg.replace("'", "\"")
        # Turn into a dict
        output_dict = json.loads(ascii_msg)

        '''
        ############## CUSTOM CODE GOES HERE ###################
        '''
        print_nicely(output_dict)
        '''
        ########################################################
        '''


    return None

if __name__ == "__main__" : main()
