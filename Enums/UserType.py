from enum import Enum

class UserType(int, Enum):
    Admin = 1
    User = 2
    Producer = 3
    Manager = 4
    Actor = 5