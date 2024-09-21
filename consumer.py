import pika


def callback(ch, method, properties, body):
    print(f"[x] Received {body}")


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_consume(queue="hello", on_message_callback=callback,
                          auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    main()
