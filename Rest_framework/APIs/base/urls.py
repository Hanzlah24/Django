from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from . import views
urlpatterns = [
    path('',views.displayRoutes),
    path('books',views.books_list),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('books/<str:name>',views.BookDetail.as_view()),
]
