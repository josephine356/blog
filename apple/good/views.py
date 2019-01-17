from django.shortcuts import render

# Create your views here.
def mac(request):
    '''
    Render the mac page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'good/mac.html', context)
def ipad(request):
    '''
    Render the ipad page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'good/ipad.html', context)
def iphone(request):
    '''
    Render the iphone page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'good/iphone.html', context)
def watch(request):
    '''
    Render the watch page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'good/watch.html', context)