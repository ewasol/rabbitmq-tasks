import pika
import uuid


class RpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue

        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.queue_name,
                correlation_id=self.corr_id
            ),
            body=str(n)
        )
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


if __name__ == "__main__":
    rpc_client = RpcClient()
    number = int(input("Enter a number: "))
    print(f" [x] Requesting factorial({number})")
    response = rpc_client.call(number)
    print(f" [x] Got {response}")
