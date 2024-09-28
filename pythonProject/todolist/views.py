from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from todolist.models import Quest


class QuestListView(generic.ListView):
    context_object_name = 'latest_quest_list'

    def get_queryset(self):
        return Quest.objects.order_by("-pub_date")[:5]

class QuestDetailView(DetailView):
    model = Quest
    template_name = 'todolist/quest_detail.html'

class QuestCreateView(CreateView):
    model = Quest
    fields = ('title','description')
    success_url = reverse_lazy('todolist:index')

class QuestUpdateView(UpdateView):
    model = Quest
    fields = ('title','description')
    success_url = reverse_lazy('todolist:index')

class QuestDeleteView(DeleteView):
    model = Quest
    success_url = reverse_lazy('todolist:index')


"""Документация"""


def quest_activity(request, pk):
    quest_item = get_object_or_404(Quest, pk=pk)
    if not quest_item.is_active:
        quest_item.is_active = True
    else:
        quest_item.is_active = False

    quest_item.save()
    return redirect(reverse('todolist:index'))
