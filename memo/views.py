from django.shortcuts import render
from django.views import generic
from .models import Shelf
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied



class ListMemoView(LoginRequiredMixin,generic.ListView):
    template_name = 'memo/memo_list.html'
    model = Shelf
    context_object_name = 'Shelf'
    
    def get_queryset(self):
        queryset = Shelf.objects.filter(user=self.request.user)
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tag__icontains=tag)
        return queryset

class DetailMemoView(LoginRequiredMixin,generic.DetailView):
    template_name = 'memo/memo_detail.html'
    model = Shelf
    context_object_name = 'Shelf'


class CreateMemoView(LoginRequiredMixin,generic.CreateView):
    template_name = 'memo/memo_create.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'tag')
    success_url = reverse_lazy('memo:list-memo')

    def form_valid(self, form):
        form.instance.user = self.request.user  # ログイン中のユーザーを設定
        return super().form_valid(form)

class UpdateMemoView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'memo/memo_update.html'
    model = Shelf
    context_object_name = 'Shelf'
    fields = ('title', 'text', 'tag')
    success_url = reverse_lazy('memo:list-memo')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied('編集権限がありません。')
        return super(UpdateMemoView, self).dispatch(request, *args, **kwargs)

class DeleteMemoView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'memo/memo_delete.html'
    model = Shelf
    context_object_name = 'Shelf'
    success_url = reverse_lazy('memo:list-memo')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied('削除権限がありません。')
        return super(DeleteMemoView, self).dispatch(request, *args, **kwargs)
    

# class AddTagView(LoginRequiredMixin, generic.FormView):
#     template_name = 'memo/memo_addtag.html'
#     form_class = TagForm
#     success_url = reverse_lazy('memo:list-memo')

#     def form_valid(self, form):
#         tag = form.cleaned_data['tag']
#         Shelf.objects.create(tag=tag, user=self.request.user)
#         return super().form_valid(form)