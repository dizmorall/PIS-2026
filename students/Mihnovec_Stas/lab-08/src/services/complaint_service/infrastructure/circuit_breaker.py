import time

class CircuitBreaker:
    """Паттерн Предохранитель (Circuit Breaker) для защиты внешних HTTP вызовов"""
    
    def __init__(self, failure_threshold=3, recovery_timeout=60):
        self.failure_threshold = failure_threshold # Сколько ошибок допустимо
        self.recovery_timeout = recovery_timeout   # Секунд до попытки восстановления
        
        self.failures = 0
        self.state = "CLOSED" # CLOSED (работает), OPEN (сломано), HALF_OPEN (проверяем)
        self.last_failure_time = None
        
    def execute(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN" # Пробуем сделать тестовый запрос
            else:
                raise Exception("Circuit is OPEN: Внешний сервис недоступен, запрос отклонен (Fast Fail)")
                
        try:
            result = func(*args, **kwargs)
            # Если запрос прошел в режиме HALF_OPEN, чиним цепь
            if self.state == "HALF_OPEN":
                self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e
            
    def record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            print("[CircuitBreaker] Цепь РАЗОРВАНА! Сервис ИИ упал.")
            
    def reset(self):
        self.failures = 0
        self.state = "CLOSED"
        print("[CircuitBreaker] Цепь ВОССТАНОВЛЕНА. Сервис ИИ снова в сети.")