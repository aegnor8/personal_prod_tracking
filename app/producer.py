from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def send_unlock_event(key: str, value: str):
    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    p.produce('unlock_events', key=key, value=value, callback=delivery_report)
    Producer.flush()    