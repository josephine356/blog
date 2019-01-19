from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from iphone.models import Iphone, Comment
from iphone.forms import IphoneForm
from django.db.models.query_utils import Q
from main.views import admin_required


def iphone(request):
    '''
    Render the iphone page
    '''
    iphones = {}
    for iphone in Iphone.objects.all():
        iphones.update({iphone:Comment.objects.filter(iphone=iphone)})
    context = {'iphones':iphones}
    return render(request, 'iphone/iphone.html', context)
@admin_required
def iphoneCreate(request):
    '''
    Create a new iphone instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the iphone page
    '''
    template = 'iphone/iphoneCreateUpdate.html'
    if request.method == 'GET':
        print(IphoneForm())
        return render(request, template, {'iphoneForm':IphoneForm()})
    
        # POST
    iphoneForm = IphoneForm(request.POST)
    if not iphoneForm.is_valid():
        return render(request, template, {'iphoneForm':iphoneForm})
    iphoneForm.save()
    messages.success(request, '文章已新增')
    return redirect('iphone:iphone')

def iphoneRead(request, iphoneId):
    '''
    Read an iphone
        1. Get the "iphone" instance using "iphoneId"; redirect to the 404 page if not found
        2. Render the iphoneRead template with the iphone instance and its
           associated comments
    '''
    iphone = get_object_or_404(Iphone, id=iphoneId)
    context = {
        'iphone': iphone,
        'comments': Comment.objects.filter(iphone=iphone)
    }
    return render(request, 'iphone/iphoneRead.html', context)
@admin_required
def iphoneUpdate(request, iphoneId):
    '''
    Update the iphone instance:
        1. Get the iphone to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    iphone = get_object_or_404(Iphone, id=iphoneId)
    template = 'iphone/iphoneCreateUpdate.html'
    if request.method == 'GET':
        iphoneForm = IphoneForm(instance=iphone)
        return render(request, template, {'iphoneForm':iphoneForm})

    # POST
    iphoneForm = IphoneForm(request.POST, instance=iphone)
    if not iphoneForm.is_valid():
        return render(request, template, {'iphoneForm':iphoneForm})

    iphoneForm.save()
    messages.success(request, '文章已修改') 
    return redirect('iphone:iphoneRead', iphoneId=iphoneId)
@admin_required
def iphoneDelete(request, iphoneId):
    '''
    Delete the iphone instance:
        1. Render the iphone page if the method is GET
        2. Get the iphone to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return redirect('iphone:iphone')

    # POST
    iphone = get_object_or_404(Iphone, id=iphoneId)
    iphone.delete()
    messages.success(request, '文章已刪除')  
    return redirect('iphone:iphone')

def iphoneSearch(request):
    '''
    Search for iphones:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    iphones = Iphone.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'iphone':iphones, 'searchTerm':searchTerm}
    return render(request, 'iphone/iphoneSearch.html', context)
