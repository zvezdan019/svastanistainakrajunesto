from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from models import Cros

from django.core.urlresolvers import reverse
class ListContactView(ListView):

    model = Cros
    template_name = 'cros_list.html'
class CreateContactView(CreateView):

    model = Cros
    template_name = 'edit_contact_cros.html'

    def get_success_url(self):
        return reverse('cros-list')

        

class UpdateContactView(UpdateView):

    model = Cros
    template_name = 'edit_contact_cros.html'

    def get_success_url(self):
        return reverse('cros-list') 
    
    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('cros-edit', kwargs={'pk': self.get_object().id})

        return context   
        


class DeleteContactView(DeleteView):

    model = Cros
    template_name = 'delete_cros.html'

    def get_success_url(self):
        return reverse('cros-list')