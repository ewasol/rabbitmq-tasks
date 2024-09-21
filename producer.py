import pika
import time 


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost") # rabbitmq
    )
    channel = connection.channel()

    channel.queue_declare(queue="hello")
    # # channel.exchange_declare(exchange="my", exchange_type="fanout")

    for i in range(5):
        message = f"Hello World {i}"
        channel.basic_publish(exchange='', routing_key="hello", body=message)

        print(f"[x] Sent {message}")
        time.sleep(1)

    connection.close()


if __name__ == "__main__":
    main()
