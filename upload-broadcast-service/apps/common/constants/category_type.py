from enum import Enum


class CategoryType(Enum):
    PERSONAL = 'Personal'
    PUBLIC = 'Public'
    NONE = 'None'

    @classmethod
    def choices(cls):
        return tuple((category.name, category.value) for category in cls)

    @classmethod
    def __contains__(cls, value):
        values = [status.value for status in CategoryType]
        return values.__contains__(value)
