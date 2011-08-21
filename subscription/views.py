from django.views.defaults import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404

from .models import Subscription
from .forms import SubscriptionForm


def success(request, id, template='subscription/success.html'):
    subscriber = get_object_or_404(Subscription, pk=id)
    return render_to_response(template, {'subscriber': subscriber}, context_instance=RequestContext(request))

def new(request, template='subscription/form.html'):
    return render_to_response(template, {'form': SubscriptionForm()}, context_instance=RequestContext(request))

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render_to_response('subscription/form.html', {'form': form}, context_instance=RequestContext(request))
    
    subscriber = form.save()
    return redirect('subscription:success', id=subscriber.pk)