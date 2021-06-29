from django.views.generic import TemplateView

from .models import Servico

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        return context

class ContatoView(TemplateView):
    template_name = 'contato.html'