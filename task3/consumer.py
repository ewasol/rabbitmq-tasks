import pika
import time


def callback(ch, method, properties, body):
    message = body.decode()
    print(f"[x] Receiving {message}")
    time.sleep(10)
    print(f"[x] Received {message}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main(consumer_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='work_queue', durable=False)

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='work_queue', on_message_callback=callback)

    print(
        f' [*] Consumer {consumer_id} waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    import sys
    consumer_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    main(consumer_id)
