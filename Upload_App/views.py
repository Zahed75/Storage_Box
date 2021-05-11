from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Upload_App.models import Uploader

from .forms import EditForm
# Create your views here.

# @login_required
def file_list(request):
    uploader = Uploader.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Uploader.objects.filter(upload_title__icontains=search)
    # return render(request, 'stream_app/home.html', {'videos': videos, 'search': search, 'result': result})
    # context_object_name = 'Uploads'
    # model = Uploader
    template_name = 'Upload_App/index.html'
    context = {'Uploads': uploader, 'search': search, 'result': result}
    return render(request, template_name, context)


class CreateFile(LoginRequiredMixin,CreateView):
    model = Uploader
    template_name = 'Upload_App/create_file.html'
    fields = ('upload_title', 'file_details', 'thumbnail',)

    def form_valid(self, form):
        Uploader_obj = form.save(commit=False)
        Uploader_obj.author = self.request.user
        title = Uploader_obj.upload_title
        Uploader_obj.save()
        return HttpResponseRedirect(reverse('index'))

class MyFiles(LoginRequiredMixin, TemplateView):
    template_name = 'Upload_App/files.html'
    


@login_required
def edit_files(request, pk):
    uploader = Uploader.objects.get(pk=pk)
    form = EditForm(instance=uploader)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=uploader)
        if form.is_valid():
            form.save()
            form = EditForm(instance=uploader)
            return HttpResponseRedirect(reverse('Upload_App:my_files'))

    context = {'form': form}
    return render(request, 'Upload_App/edit_files.html', context)

# class UpdateFiles(LoginRequiredMixin,UpdateView):
#     model=Uploader
#     fields=(' upload_title','file_details','thumbnail')
#     template_name='Upload_App/edit_files.html'

#     def get_success_url(self,**kwargs):
#         return reverse_lazy('Upload_App:edit_files',kwargs={'pk':self.object.pk})