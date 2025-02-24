from django.urls import path
from . import views

app_name = 'memo'
# path memo/が親URL
urlpatterns = [
    path('', views.ListMemoView.as_view(), name='list-memo'),
    path('memo/<int:pk>/detail/', views.DetailMemoView.as_view(), name='detail-memo'),
    path('memo/create/', views.CreateMemoView.as_view(), name='create-memo'),
    path('memo/<int:pk>/update/', views.UpdateMemoView.as_view(), name='update-memo'),
    path('memo/<int:pk>/delete/', views.DeleteMemoView.as_view(), name='delete-memo'),
]