# src/application/query/queries.py
from dataclasses import dataclass

@dataclass(frozen=True)
class GetComplaintByIdQuery:
    complaint_id: str

@dataclass(frozen=True)
class ListPendingComplaintsQuery:
    limit: int = 10
    offset: int = 0
