import json
import pika

class RabbitMQSubscriber:
    """Подписчик на события домена (Входящий адаптер)"""
    
    def __init__(self, connection_url: str):
        self.connection_url = connection_url
        self.exchange = "news_domain_events"
        self.queue_name = "notification_service_queue"
    
    def start_listening(self):
        connection = pika.BlockingConnection(pika.URLParameters(self.connection_url))
        channel = connection.channel()
        
        channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')
        # Создаем уникальную очередь для этого микросервиса
        channel.queue_declare(queue=self.queue_name)
        channel.queue_bind(exchange=self.exchange, queue=self.queue_name)
        
        def callback(ch, method, properties, body):
            event = json.loads(body)
            if event["event_type"] == "ComplaintCreated":
                print(f"[Email] Отправка уведомления модераторам о новой жалобе: {event['data']['id']}")
            elif event["event_type"] == "ComplaintClosedAsFake":
                print(f"[Email] Отправка предупреждения автору новости: {event['data']['news_url']}")
        
        channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        print("[EventBus] NotificationService ожидает событий...")
        channel.start_consuming()