from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView

from todolist.models import Quest


class IndexView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'latest_quest_list'

    def get_queryset(self):
        return Quest.objects.order_by("-pub_date")[:5]

class DetailView(DetailView):
    model = Quest
    template_name = 'todolist/quests.html'

class QuestCreateView(CreateView):
    model = Quest
    fields = ('title','description')
    success_url = reverse_lazy('todolist:index')

