"""**Zadanie 2: Tworzenie prostego producenta i konsumenta**

- **Cel**: Zrozumieć podstawowy mechanizm wysyłania i odbierania wiadomości.
- **Instrukcje**:
  - Napisz program producenta, który wysyła wiadomość "Hello World!" do kolejki o nazwie "hello".
  - Napisz program konsumenta, który odbiera wiadomość z kolejki "hello" i wyświetla ją na ekranie.
  - Uruchom oba programy i upewnij się, że komunikacja działa poprawnie."""

import pika
import time 


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    for i in range(5):
        message = f"Hello World {i}"
        channel.basic_publish(exchange='', routing_key="hello",
                              body=message.encode())

        print(f"[x] Sent {message}")
        time.sleep(1)

    connection.close()


if __name__ == "__main__":
    main()
