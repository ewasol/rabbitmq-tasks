"""

**Zadanie 7: Zdalne wywołanie procedur (RPC)**

- **Cel**: Implementacja mechanizmu RPC z użyciem RabbitMQ.
- **Instrukcje**:
  - Zaimplementuj serwer RPC, który wykonuje pewną operację (np. oblicza silnię liczby).
  - Klient wysyła żądanie z liczbą, a serwer zwraca wynik obliczeń.
  - Użyj właściwości wiadomości `reply_to` i `correlation_id` do obsługi odpowiedzi.
  - Upewnij się, że klient otrzymuje poprawną odpowiedź od serwera.
"""
import pika
from math import factorial


def on_request(ch, method, properties, body):
    n = int(body)
    print(f" [.] Calculating factorial({n})")
    response = factorial(n)

    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def rpc_server():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue='rpc_queue')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()


if __name__ == "__main__":
    rpc_server()
