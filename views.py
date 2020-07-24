from django.shortcuts import render
from django.views import generic

from dashboard.apps.core.utils import log
from dashboard.apps.pages.experiments import models

import os

class IndexView(generic.TemplateView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'experiments/base.html'

class IndexView_2(generic.ListView):
    """
    IndexView:
    """
    module = 'IndexView'
    template_name = 'tables/base.html'

    data = models.table_data("test_1")
    print("PRINTING DATA NOW!!!!!!!!!: {}".format(data))

    def get_queryset(self):
        log(self.module, 'get_queryset', file=__file__)
        return self.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data
        return context

 
class PrepView(generic.TemplateView):
    """
    PrepView:
    """
    module = 'PrepView'
    template_name = 'experiments/prep.html'

def prep(request):
    path="E:\data-cladaq"  # insert the path to your directory   
    file_list =os.listdir(path)   
    return render(request, "experiments/prep.html", {'files': file_list})
