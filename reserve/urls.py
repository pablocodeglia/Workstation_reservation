from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reserve'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_reservations/', views.ReservationsListView.as_view(), name='my_reservations'),
    path('history/', views.history_view, name='history'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('delete_reservation/<id>', views.delete_reservation, name='delete_reservation'), 
    path('find_coworkers/', views.find_coworkers_view, name='find_coworkers'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
