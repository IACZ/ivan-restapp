from django.urls import path, include
from libapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('publication-houses', views.PublicationViewSet, 'publication-houses')
# give the third attriute (base name) when u urself override the get_queryset()

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('', include(router.urls))
]


'''path('publication-houses/', views.PublicationHouseListCreate.as_view()),
    path('publication-houses/<int:pk>', views.PubRetUpdateDelete.as_view())'''