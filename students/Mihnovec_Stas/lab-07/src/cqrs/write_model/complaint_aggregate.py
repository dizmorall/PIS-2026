# Это упрощенная версия агрегата из Lab #3 для демонстрации.
# Write Model содержит сложную логику, вложенные сущности (Review) и генерирует события.

class ComplaintWriteModel:
    def __init__(self, id: str, news_url: str):
        self.id = id
        self.news_url = news_url
        self.status = "PENDING"
        self.reviews = []  # Вложенные сущности
        self.events = []   # Доменные события
        
    def add_review(self, review):
        # ... Сложная валидация (инварианты) ...
        self.reviews.append(review)
        # Генерируем событие для синхронизации
        self.events.append({
            "type": "ReviewAddedEvent",
            "complaint_id": self.id,
            "is_fake": review.is_fake
        })