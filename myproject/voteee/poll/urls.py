from django.urls import path
from poll.views import index
urlpatterns = [
    path("first",index, name="first_view")
]