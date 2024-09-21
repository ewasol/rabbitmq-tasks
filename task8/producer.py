"""
**Zadanie 8: Trwałość wiadomości i kolejek**

- **Cel**: Zapewnienie, że wiadomości i kolejki przetrwają restart serwera RabbitMQ.
- **Instrukcje**:
  - Skonfiguruj kolejki i wymiany jako trwałe (durable).
  - Ustaw właściwość wiadomości `delivery_mode=2`, aby były trwałe.
  - Przetestuj zachowanie systemu po restarcie RabbitMQ.
"""
import pika


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

    for i in range(5):
        task = f'Task no. {i}'
        channel.basic_publish(
            exchange='persistent_exchange',
            routing_key='task_key',
            body=task.encode(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print(f" [x] Sent '{task}'")

    connection.close()


# TODO: restart server: sudo systemctl restart rabbitmq-server

if __name__ == "__main__":
    main()
