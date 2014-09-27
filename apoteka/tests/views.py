from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from models import Test

from django.core.urlresolvers import reverse
class ListContactView(ListView):

    model = Test
    template_name = 'test_list.html'
class CreateContactView(CreateView):

    model = Test
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('tests-list')
        


class UpdateContactView(UpdateView):

    model = Test
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('tests-list') 
    
    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('tests-edit', kwargs={'pk': self.get_object().id})

        return context   
        


class DeleteContactView(DeleteView):

    model = Test
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('tests-list')