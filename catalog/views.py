from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import PresentationFilter
from .forms import PresentationForm
from .models import Presentation
from .tables import PresentationTable


class PresentationListView(SingleTableMixin, FilterView):
    table_class = PresentationTable
    model = Presentation
    template_name = 'catalog.html'

    filterset_class = PresentationFilter

    def get_table_kwargs(self):
        return {'template_name': 'django_tables2/bootstrap.html'}


def modify(request, p_id):

    try:
        presentation = Presentation.objects.get(presentation_id=p_id) # exception, if presentation not exist
        if not request.user.is_authenticated:
            return HttpResponseForbidden(render_to_string('error.html', {'msg':'You are not logged in.'}))
        if presentation.creator != str(request.user).replace('_', ' ').title():
            return HttpResponseForbidden(render_to_string('error.html', {'msg':'You are only allowed to edit your own presentations.'}))
    except ObjectDoesNotExist:
        return HttpResponseBadRequest(render_to_string('error.html', {'msg':'Presentation id does not exist.'}))

    if request.method == 'POST':
        form = PresentationForm(request.POST)
        if form.is_valid():
            presentation.picture = form.cleaned_data['picture']
            presentation.title = form.cleaned_data['title']
            presentation.save()
            return HttpResponseRedirect(reverse('catalog'))
        return HttpResponseBadRequest(render_to_string('error.html', {'msg':'Form isn\'t valid.'}))

    form = PresentationForm(initial={'picture': presentation.picture, 'title': presentation.title})
    return render(request, 'modify.html', {'form': form, 'presentation': presentation})
