"""**Zadanie 4: Wzorzec publikacji/subskrypcji**

- **Cel**: Dystrybucja wiadomości do wielu odbiorców.
- **Instrukcje**:
  - Utwórz wymianę (exchange) typu `fanout` o nazwie "logs".
  - Zmodyfikuj producenta, aby wysyłał wiadomości do wymiany "logs" zamiast bezpośrednio do kolejki.
  - Napisz kilku konsumentów, którzy tworzą własne, unikalne kolejki i wiążą je z wymianą "logs".
  - Sprawdź, czy wszyscy konsumenty otrzymują kopie wysłanych wiadomości."""


import pika


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    for i in range(6):
        message = f"Message no. {i}"
        channel.basic_publish(
            exchange='logs',
            routing_key='',
            body=message.encode()
        )

        print(f"[x] Sent {message}")

    connection.close()


if __name__ == "__main__":
    main()
