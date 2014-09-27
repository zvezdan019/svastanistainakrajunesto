from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from models import Article



from django.core.urlresolvers import reverse
class ListContactView(ListView):

    model = Article
    template_name = 'article_list.html'
class CreateContactView(CreateView):

    model = Article
    template_name = 'edit_contact_article.html'

    def get_success_url(self):
        return reverse('article-list')
        
    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('article-novo')

        return context
        

class UpdateContactView(UpdateView):

    model = Article
    template_name = 'edit_contact_article.html'

    def get_success_url(self):
        return reverse('article-list') 
    
    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('article-edit', kwargs={'pk': self.get_object().id})

        return context   
        


class DeleteContactView(DeleteView):

    model = Article
    template_name = 'delete_article.html'

    def get_success_url(self):
        return reverse('article-list')