from django.shortcuts import render
from itertools import groupby
import re


def index(request):
    return render(request, 'index.html')


def factorial(request):
    if request.method == 'POST':
        n = int(request.POST.get('number'))

        def calc_fact(n):
            if n < 1:
                return 1
            else:
                return n * calc_fact(n-1)

        fact = calc_fact(n)

    return render(request, 'index.html', locals())


def prime(request):
    if request.method == 'POST':
        n = int(request.POST.get('number'))
        primes = list(n for n in range(2, n)
                      if all(n % d for d in range(2, n)))

    return render(request, 'index.html', locals())


def fibonacci(request):
    if request.method == 'POST':
        n = int(request.POST.get('number'))

        a = 1
        b = 1
        result = []

        while len(result) < n:
            result.append(a)
            next_fib = a + b
            a = b
            b = next_fib

    return render(request, 'index.html', locals())


def encode(request):
    if request.method == 'POST':
        input_string = request.POST.get('rlf')

        # http://rosettacode.org/wiki/Run-length_encoding
        encoded_str = [(len(list(g)), k) for k, g in groupby(input_string)]
        encoded_str = ''.join(str(y) for x in encoded_str for y in x)

    return render(request, 'index.html', locals())


def decode(request):
    if request.method == 'POST':
        rlf_string = request.POST.get('rlf_decode')
        prepare_str_for_decode = re.findall('\d+\w', rlf_string)
        decoded_str = ''.join(x[-1]*int(x[:-1]) for x in prepare_str_for_decode)

    return render(request, 'index.html', locals())
