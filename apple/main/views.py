from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)
def add(request):
    '''
    Render the add page
    '''
    return render(request, 'main/add.html')

