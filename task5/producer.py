"""
**Zadanie 5: Routing wiadomości**

- **Cel**: Kierowanie wiadomości na podstawie kluczy routingu.
- **Instrukcje**:
  - Zmień typ wymiany na `direct` o nazwie "direct_logs".
  - Producent powinien wysyłać wiadomości z kluczami routingu, takimi jak "info", "warning", "error".
  - Konsumenci subskrybują wiadomości na podstawie wybranych kluczy routingu.
  - Przetestuj, czy konsument otrzymuje tylko te wiadomości, które są zgodne z jego kluczem routingu.
"""
import pika
import sys


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'

    channel.basic_publish(
        exchange='direct_logs',
        routing_key=severity,
        body=message.encode()
    )

    print(f" [x] Sent '{message}' with routing key '{severity}'")

    connection.close()


if __name__ == "__main__":
    main()
