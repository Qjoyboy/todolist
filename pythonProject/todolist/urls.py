from django.urls import path
from . import views
from .views import quest_activity

app_name = "todolist"
urlpatterns = [
    path("", views.QuestListView.as_view(), name='index'),
    path("view/<int:pk>/", views.QuestDetailView.as_view(), name='detail'),
    path("create/", views.QuestCreateView.as_view(), name='create'),
    path("edit/<int:pk>/", views.QuestUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", views.QuestDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', quest_activity, name='quest_activity'),
]