from enum import Enum

class ItemStatus(int, Enum):
    published = 1
    unpublished = 2
    sold = 3
    reserved = 4
    deleted = 5