from dataclasses import dataclass

@dataclass
class ComplaintDashboardView:
    """
    Read Model (Денормализованная проекция).
    Специально спроектирована для быстрого отображения в UI модератора.
    Вместо списка ревью здесь хранится только их количество.
    """
    id: str
    news_url: str
    status: str
    # Денормализованные (предварительно вычисленные) поля:
    total_reviews_count: int 
    fake_votes_count: int
    last_updated_at: str

# Интерфейс репозитория только для чтения (обычно это NoSQL база вроде ElasticSearch 
# или отдельная таблица в PostgreSQL)
class ComplaintViewRepository:
    def save_view(self, view: ComplaintDashboardView): pass
    def get_by_id(self, complaint_id: str) -> ComplaintDashboardView: pass
    def get_dashboard_list(self) -> list: pass