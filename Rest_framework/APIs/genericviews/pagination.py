from rest_framework.pagination import LimitOffsetPagination

class AuthorPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10
    
class BookPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10