class DomainException(Exception):
    """Базовый класс для доменных ошибок"""
    pass

class InvalidComplaintStatusException(DomainException):
    pass

class RuleViolationException(DomainException):
    pass