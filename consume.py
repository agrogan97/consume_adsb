import json
from kafka import KafkaConsumer


def format_dict():
    '''
    Summary:
            - Take the message and format into a dict of structure {'flight_id' : {'lat' : lat, 'long' : long}, ... }
    '''

    return None



def main():

    consumer = KafkaConsumer('adsb-data', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

    for message in consumer:
        print("NEW MESSAGE")
        # print(message)

        ascii_msg = message.value.decode('ascii')
        ascii_msg = ascii_msg.replace("'", "\"")
        output_dict = json.loads(ascii_msg)
        print("DECODED TYPE:", type(output_dict))

        # message.value gives us the value portion of each message
        for entry in message.value:
            print(entry)
            print("MESSAGE VALUE TYPE", type(entry))

    return None

if __name__ == "__main__" : main()
