"""**Zadanie 3: Implementacja kolejki roboczej (Work Queue)**

- **Cel**: Rozdzielanie zadań między wieloma konsumentami.
- **Instrukcje**:
  - Zmodyfikuj producenta, aby wysyłał wiele wiadomości zawierających różne teksty.
  - Dodaj w konsumentach sztuczne opóźnienie (np. `sleep`), aby symulować czasochłonne zadania.
  - Upewnij się, że wiadomości są rozdzielane równomiernie między konsumentów.
  - Włącz potwierdzenia wiadomości (acknowledgments) w konsumentach.
"""

import pika


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()

    channel.queue_declare(queue="work_queue")

    for i in range(6):
        message = f"Message no. {i}"
        channel.basic_publish(
            exchange='',
            routing_key="work_queue",
            body=message.encode(),
            properties=pika.BasicProperties(
                delivery_mode=2)
        )

        print(f"[x] Sent {message}")

    connection.close()


if __name__ == "__main__":
    main()
