"""
**Zadanie 6: Wymiana typu `topic`**

- **Cel**: Użycie wzorców w kluczach routingu do bardziej elastycznego kierowania wiadomości.
- **Instrukcje**:
  - Utwórz wymianę typu `topic` o nazwie "topic_logs".
  - Producent wysyła wiadomości z kluczami routingu w formacie "system.severity" (np. "kern.critical").
  - Konsumenci subskrybują wiadomości używając wzorców, takich jak "*.critical" lub "kern.*".
  - Sprawdź, czy konsument otrzymuje właściwe wiadomości na podstawie wzorca.
"""
import pika
import sys


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'

    channel.basic_publish(
        exchange='topic_logs',
        routing_key=routing_key,
        body=message.encode()
    )

    print(f" [x] Sent '{message}' with routing key '{routing_key}'")

    connection.close()


if __name__ == "__main__":
    main()
