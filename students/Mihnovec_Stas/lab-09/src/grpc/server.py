import time
from concurrent import futures
# В реальном проекте эти файлы генерируются командой: python -m grpc_tools.protoc ...
# import complaint_service_pb2
# import complaint_service_pb2_grpc
import grpc

class ComplaintServiceServicer: # Наследует complaint_service_pb2_grpc.ComplaintServiceServicer
    """Реализация gRPC сервера"""
    
    def CreateComplaint(self, request, context):
        """Unary RPC: Создание жалобы"""
        print(f"[Server] Получен запрос на создание жалобы для: {request.news_url}")
        
        # Здесь бы вызвали фасад из Lab 4
        # complaint_id = facade.create_complaint(...)
        
        # return complaint_service_pb2.CreateComplaintResponse(
        #     complaint_id="CMP-999",
        #     message="Жалоба успешно создана через gRPC"
        # )
        pass

    def GetComplaint(self, request, context):
        """Unary RPC: Чтение жалобы"""
        print(f"[Server] Запрос на получение жалобы: {request.complaint_id}")
        
        # return complaint_service_pb2.ComplaintDto(
        #     id=request.complaint_id,
        #     news_url="http://fake-news.com",
        #     status="PENDING",
        #     ai_score=0
        # )
        pass

    def StreamPendingComplaints(self, request, context):
        """Server-side Streaming RPC: Стримминг новых жалоб модератору"""
        print("[Server] Клиент подключился к стриму новых жалоб...")
        
        # Имитируем появление новых жалоб в реальном времени (например, из RabbitMQ)
        for i in range(1, 4):
            time.sleep(1) # Ждем 1 секунду
            # yield complaint_service_pb2.ComplaintDto(
            #     id=f"CMP-STREAM-{i}",
            #     news_url=f"http://news.com/{i}",
            #     status="PENDING",
            #     ai_score=90
            # )
            print(f"[Server] Отправлена жалоба {i} в стрим")

def serve():
    """Запуск gRPC сервера"""
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # complaint_service_pb2_grpc.add_ComplaintServiceServicer_to_server(ComplaintServiceServicer(), server)
    # server.add_insecure_port('[::]:50051')
    # server.start()
    print("gRPC Сервер запущен на порту 50051...")
    # server.wait_for_termination()