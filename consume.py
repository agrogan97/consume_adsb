import json
from kafka import KafkaConsumer

def main():

    consumer = KafkaConsumer('adsb-data', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

    for message in consumer:
        print("NEW MESSAGE")
        print(message)

    return None

if __name__ == "__main__" : main()
