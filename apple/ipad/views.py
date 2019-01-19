from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ipad.models import Ipad, Comment
from ipad.forms import IpadForm
from django.db.models.query_utils import Q


def ipad(request):
    '''
    Render the ipad page
    '''
    ipads = {}
    for ipad in Ipad.objects.all():
        ipads.update({ipad:Comment.objects.filter(ipad=ipad)})
    context = {'ipads':ipads}
    return render(request, 'ipad/ipad.html', context)

def ipadCreate(request):
    '''
    Create a new ipad instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the ipad page
    '''
    template = 'ipad/ipadCreateUpdate.html'
    if request.method == 'GET':
        print(IpadForm())
        return render(request, template, {'ipadForm':IpadForm()})
    
        # POST
    ipadForm = IpadForm(request.POST)
    if not ipadForm.is_valid():
        return render(request, template, {'ipadForm':ipadForm})
    ipadForm.save()
    messages.success(request, '文章已新增')
    return redirect('ipad:ipad')

def ipadRead(request, ipadId):
    '''
    Read an ipad
        1. Get the "ipad" instance using "ipadId"; redirect to the 404 page if not found
        2. Render the ipadRead template with the ipad instance and its
           associated comments
    '''
    ipad = get_object_or_404(Ipad, id=ipadId)
    context = {
        'ipad': ipad,
        'comments': Comment.objects.filter(ipad=ipad)
    }
    return render(request, 'ipad/ipadRead.html', context)

def ipadUpdate(request, ipadId):
    '''
    Update the ipad instance:
        1. Get the ipad to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    ipad = get_object_or_404(Ipad, id=ipadId)
    template = 'ipad/ipadCreateUpdate.html'
    if request.method == 'GET':
        ipadForm = IpadForm(instance=ipad)
        return render(request, template, {'ipadForm':ipadForm})

    # POST
    ipadForm = IpadForm(request.POST, instance=ipad)
    if not ipadForm.is_valid():
        return render(request, template, {'ipadForm':ipadForm})

    ipadForm.save()
    messages.success(request, '文章已修改') 
    return redirect('ipad:ipadRead', ipadId=ipadId)

def ipadDelete(request, ipadId):
    '''
    Delete the ipad instance:
        1. Render the ipad page if the method is GET
        2. Get the ipadd to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return redirect('ipad:ipad')

    # POST
    ipad = get_object_or_404(Ipad, id=ipadId)
    ipad.delete()
    messages.success(request, '文章已刪除')  
    return redirect('ipad:ipad')

def ipadSearch(request):
    '''
    Search for ipads:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    ipads = Ipad.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'ipads':ipads, 'searchTerm':searchTerm} 
    return render(request, 'ipad/ipadSearch.html', context)
