import json
import pika

class RabbitMQPublisher:
    """Публикатор событий в шину RabbitMQ (Исходящий адаптер)"""
    
    def __init__(self, connection_url: str):
        self.connection_url = connection_url
        self.exchange = "news_domain_events"
    
    def publish(self, event_type: str, payload: dict) -> None:
        """Отправляет событие в обменник (Fanout)"""
        connection = pika.BlockingConnection(pika.URLParameters(self.connection_url))
        channel = connection.channel()
        
        # Создаем Exchange типа 'fanout' (рассылка всем подписчикам)
        channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')
        
        message = {
            "event_type": event_type,
            "data": payload
        }
        
        channel.basic_publish(
            exchange=self.exchange,
            routing_key='',
            body=json.dumps(message)
        )
        print(f"[EventBus] Опубликовано событие: {event_type}")
        connection.close()