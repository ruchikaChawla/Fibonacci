# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.


from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .models import FibonacciApp
from django.views import View
import time


def fibonacci(numeric):
    if numeric < 2:
        return 1

    else:
        numeric_1 = 1
        numeric_2 = 1

        for numeric in range(2, numeric):
            value = numeric_1 + numeric_2
            numeric_1 = numeric_2
            numeric_2 = value

        return numeric_2


class FibonacciAPIView(View):

    def get(self, request):

        number = request.GET.get('value')

        if number is None:
            return render(request, 'fib.html')

        else:
            start_time = time.time()
            numeric = int(number)
            output = fibonacci(numeric)
            end_time = time.time() - start_time
            latency = str(end_time)

            fibonacci_qs = FibonacciApp.objects.create(
                numeric=numeric,
                output=output,
                latency=latency
            )
            fibonacci_qs.save()

            data = {
                'numeric': numeric,
                'output': output,
                'latency': latency
            }

            return render(request, 'fib.html', data)



