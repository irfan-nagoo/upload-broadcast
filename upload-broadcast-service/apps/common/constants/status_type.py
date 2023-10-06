from enum import Enum


class StatusType(Enum):
    ACTIVE = 'Active'
    DELETED = 'Deleted'
    ERROR = 'Error'

    @classmethod
    def choices(cls):
        return tuple((status.name, status.value) for status in cls)

    @classmethod
    def __contains__(cls, value):
        values = [status.value for status in StatusType]
        return values.__contains__(value)
