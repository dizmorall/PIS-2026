import grpc
# import complaint_service_pb2
# import complaint_service_pb2_grpc

def run():
    # 1. Открываем канал связи с сервером
    # with grpc.insecure_channel('localhost:50051') as channel:
    #     stub = complaint_service_pb2_grpc.ComplaintServiceStub(channel)
        
        # 2. Вызов Unary RPC
        # print("--- Вызов CreateComplaint ---")
        # response = stub.CreateComplaint(complaint_service_pb2.CreateComplaintRequest(
        #     news_url="http://scam-site.com",
        #     reporter_id="user_123",
        #     reason_category="SCAM",
        #     reason_details="Требуют деньги"
        # ))
        # print(f"Ответ сервера: {response.complaint_id} - {response.message}")

        # 3. Вызов Server-side Streaming RPC
        # print("\n--- Подключение к StreamPendingComplaints ---")
        # responses = stub.StreamPendingComplaints(complaint_service_pb2.EmptyRequest())
        # for complaint in responses:
        #     print(f"Поступила новая жалоба в реальном времени: {complaint.id} (URL: {complaint.news_url})")
    print("[Client] Демонстрация клиента завершена")

if __name__ == '__main__':
    run()