from Poll.models import Task
from django.views.generic import UpdateView, CreateView, DeleteView

# Create your views here.
class Home(CreateView):
    template_name = "index.html"
    model = Task
    fields = ['label']
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx['task'] = Task.objects.all()
        return ctx
    
class Edit(UpdateView):
    template_name = "edit.html"
    model = Task
    context_object_name = 'task'
    pk = id
    success_url = "./"
    fields = ['label']
    
class Delete(DeleteView):
    model = Task
    success_url = "/"
    pk = id