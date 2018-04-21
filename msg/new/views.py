from django.shortcuts import render,redirect,get_list_or_404
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from new.models import Info
from new.form import InfoForm
from django.urls import reverse_lazy
# Create your views here.
# class AboutView(TemplateView):
#     template_name = 'about.html'

class CreateInfoView(CreateView):

    # redirect_field_name = 'new/about.html'

    form_class = InfoForm

    model = Info
    success_url = reverse_lazy('info_list')
    
class InfoListView(ListView):
    template_name = 'about.html'
    context_object_name = 'user_list'
    model = Info

    def get_queryset(self):
        return Info.objects.all()

class InfoDeleteView(DeleteView):
    model = Info
    success_url = reverse_lazy('info_list')

class InfoDetailView(DetailView):
    model = Info
