# Заглушка портов
class ComplaintServicePort: pass 

class ComplaintServiceFacade(ComplaintServicePort):
    """Фасад, скрывающий сложность CQRS от инфраструктуры (контроллеров)"""
    
    def __init__(self, 
                 create_handler, 
                 add_review_handler, 
                 get_complaint_handler):
        self._create_handler = create_handler
        self._add_review_handler = add_review_handler
        self._get_complaint_handler = get_complaint_handler

    # ---------- COMMANDS (Изменяют состояние) ----------
    def create_complaint(self, command) -> str:
        return self._create_handler.handle(command)
        
    def add_human_review(self, command) -> None:
        self._add_review_handler.handle(command)

    # ---------- QUERIES (Читают состояние) ----------
    def get_complaint_by_id(self, query):
        return self._get_complaint_handler.handle(query)