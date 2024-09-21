import pika
import time


def callback(ch, method, properties, body):
    message = body.decode()
    print(f"[x] Receiving {message}")
    time.sleep(6)
    print(f"[x] Received {message}")


def main(consumer_id):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    result = channel.queue_declare(queue='')  # generate a queue with a
    # random, unique name
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name)

    print(f'[*] Consumer {consumer_id} waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback,
                          auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    import sys
    consumer_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    main(consumer_id)
