from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers

from .models import City, Location, Event

def to_json(query_set):
    return HttpResponse(serializers.serialize("json", queryset=query_set))


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['locations'] = Location.objects.all()
        context['events'] = Event.objects.all()
        return context

    def post(self, request):
        newEvent = Event(name=request.POST['name'])
        newEvent.save()
        return redirect('/')


class PartialEvents(ListView):
    model = Event
    template_name = "_events.html"
    context_object_name = "events"


class ApiEvents(View):
    def get(self, request):
        events = Event.objects.all()

        return to_json(events)


class CityDetail(DetailView):
    model = City
    template_name = 'city.html'
    slug_field = 'name'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug'].lower()
        try:
            return [city for city in City.objects.all() if city.to_slug() == slug][0]
        except:
            raise RuntimeError('City %s not found' % slug)
# def hello(request):
#     context = {}

#     if 'name' in request.session:
#         context['name'] = request.session['name']

#     return render(request, 'city.html', context)

            