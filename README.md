---

**Zadanie 1: Instalacja RabbitMQ i przygotowanie środowiska**

- **Cel**: Zainstalować RabbitMQ i upewnić się, że środowisko jest gotowe do pracy.
- **Instrukcje**:
  - Zainstaluj RabbitMQ na swoim komputerze lub skonfiguruj dostęp do zdalnego serwera RabbitMQ.
  - Upewnij się, że możesz uzyskać dostęp do panelu zarządzania RabbitMQ (domyślnie na porcie `http://localhost:15672`).
  - Zainstaluj bibliotekę klienta dla języka programowania, którego używasz (np. `pika` dla Pythona).

---

**Zadanie 2: Tworzenie prostego producenta i konsumenta**

- **Cel**: Zrozumieć podstawowy mechanizm wysyłania i odbierania wiadomości.
- **Instrukcje**:
  - Napisz program producenta, który wysyła wiadomość "Hello World!" do kolejki o nazwie "hello".
  - Napisz program konsumenta, który odbiera wiadomość z kolejki "hello" i wyświetla ją na ekranie.
  - Uruchom oba programy i upewnij się, że komunikacja działa poprawnie.

---

**Zadanie 3: Implementacja kolejki roboczej (Work Queue)**

- **Cel**: Rozdzielanie zadań między wieloma konsumentami.
- **Instrukcje**:
  - Zmodyfikuj producenta, aby wysyłał wiele wiadomości zawierających różne teksty.
  - Dodaj w konsumentach sztuczne opóźnienie (np. `sleep`), aby symulować czasochłonne zadania.
  - Upewnij się, że wiadomości są rozdzielane równomiernie między konsumentów.
  - Włącz potwierdzenia wiadomości (acknowledgments) w konsumentach.

---

**Zadanie 4: Wzorzec publikacji/subskrypcji**

- **Cel**: Dystrybucja wiadomości do wielu odbiorców.
- **Instrukcje**:
  - Utwórz wymianę (exchange) typu `fanout` o nazwie "logs".
  - Zmodyfikuj producenta, aby wysyłał wiadomości do wymiany "logs" zamiast bezpośrednio do kolejki.
  - Napisz kilku konsumentów, którzy tworzą własne, unikalne kolejki i wiążą je z wymianą "logs".
  - Sprawdź, czy wszyscy konsumenty otrzymują kopie wysłanych wiadomości.

---

**Zadanie 5: Routing wiadomości**

- **Cel**: Kierowanie wiadomości na podstawie kluczy routingu.
- **Instrukcje**:
  - Zmień typ wymiany na `direct` o nazwie "direct_logs".
  - Producent powinien wysyłać wiadomości z kluczami routingu, takimi jak "info", "warning", "error".
  - Konsumenci subskrybują wiadomości na podstawie wybranych kluczy routingu.
  - Przetestuj, czy konsument otrzymuje tylko te wiadomości, które są zgodne z jego kluczem routingu.

---

**Zadanie 6: Wymiana typu `topic`**

- **Cel**: Użycie wzorców w kluczach routingu do bardziej elastycznego kierowania wiadomości.
- **Instrukcje**:
  - Utwórz wymianę typu `topic` o nazwie "topic_logs".
  - Producent wysyła wiadomości z kluczami routingu w formacie "system.severity" (np. "kern.critical").
  - Konsumenci subskrybują wiadomości używając wzorców, takich jak "*.critical" lub "kern.*".
  - Sprawdź, czy konsument otrzymuje właściwe wiadomości na podstawie wzorca.

---

**Zadanie 7: Zdalne wywołanie procedur (RPC)**

- **Cel**: Implementacja mechanizmu RPC z użyciem RabbitMQ.
- **Instrukcje**:
  - Zaimplementuj serwer RPC, który wykonuje pewną operację (np. oblicza silnię liczby).
  - Klient wysyła żądanie z liczbą, a serwer zwraca wynik obliczeń.
  - Użyj właściwości wiadomości `reply_to` i `correlation_id` do obsługi odpowiedzi.
  - Upewnij się, że klient otrzymuje poprawną odpowiedź od serwera.

---

**Zadanie 8: Trwałość wiadomości i kolejek**

- **Cel**: Zapewnienie, że wiadomości i kolejki przetrwają restart serwera RabbitMQ.
- **Instrukcje**:
  - Skonfiguruj kolejki i wymiany jako trwałe (durable).
  - Ustaw właściwość wiadomości `delivery_mode=2`, aby były trwałe.
  - Przetestuj zachowanie systemu po restarcie RabbitMQ.

---

**Zadanie 9: Potwierdzenia producenta (Publisher Confirms)**

- **Cel**: Zapewnienie, że wiadomości zostały poprawnie zapisane przez RabbitMQ.
- **Instrukcje**:
  - Włącz w producentach mechanizm potwierdzeń wydawcy.
  - Obsłuż scenariusze, w których wiadomość nie może zostać dostarczona (np. brakująca wymiana).
  - Zaimplementuj logikę ponownej wysyłki lub obsługi błędów.

---

**Zadanie 10: Bezpieczeństwo i autoryzacja**

- **Cel**: Zabezpieczenie komunikacji z RabbitMQ.
- **Instrukcje**:
  - Skonfiguruj użytkowników i uprawnienia w RabbitMQ.
  - Włącz SSL/TLS dla połączeń klient-serwer.
  - Zmodyfikuj aplikacje, aby korzystały z bezpiecznych połączeń i uwierzytelniania.
