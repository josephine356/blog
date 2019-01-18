from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)

def sign(request):
    '''
    Render the sign page
    '''
    return render(request, 'main/sign.html')
