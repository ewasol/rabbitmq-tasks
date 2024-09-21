import pika


def callback(ch, method, properties, body):
    print(
        f" [x] Consumer {consumer_id} received '{body.decode()}' with routing "
        f"key '{method.routing_key}'"
    )


def main(consumer_id, binding_key):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='')
    queue_name = result.method.queue

    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=binding_key
    )

    print(
        f' [*] Consumer {consumer_id} waiting for logs with binding key '
        f'"{binding_key}". To exit press CTRL+C')

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == "__main__":
    import sys
    consumer_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    binding_key = sys.argv[2] if len(sys.argv) > 2 else 'info'
    main(consumer_id, binding_key)
