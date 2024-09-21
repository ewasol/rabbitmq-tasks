import pika
import time


def callback(ch, method, properties, body):
    task = body.decode()
    print(f" [x] Received '{task}'")
    time.sleep(3)
    print(f" [x] Finished '{task}'")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(
        exchange='persistent_exchange',
        exchange_type='direct',
        durable=True
    )
    channel.queue_declare(queue='durable_queue', durable=True)
    channel.queue_bind(
        exchange='persistent_exchange',
        queue='durable_queue',
        routing_key='task_key'
    )

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='durable_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    main()
