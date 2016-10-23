from django.views import generic
from .models import Office

class OfficeListView(generic.ListView):
    model = Office
    template_name = 'office/offices.html'