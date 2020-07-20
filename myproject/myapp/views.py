# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Pet
from django.http import Http404

# Create your views here.


def home(request):
    # return HttpResponse('<p>home view</p>')
    pets = Pet.objects.all()
    # send to the template
    return render(request, 'home.html', {
        'pets': pets,
    })


def pet_detail(request, pet_id):
    # return HttpResponse(f'<p>pet_detail with id {pet_id}</p>')
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    # send to the template
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
