from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from watch.models import Watch, Comment
from watch.forms import WatchForm
from django.db.models.query_utils import Q
from main.views import admin_required



def watch(request):
    '''
    Render the watch page
    '''
    watchs = {}
    for watch in Watch.objects.all():
        watchs.update({watch:Comment.objects.filter(watch=watch)})
    context = {'watchs':watchs}
    return render(request, 'watch/watch.html', context)
@admin_required
def watchCreate(request):
    '''
    Create a new watch instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the watch page
    '''
    template = 'watch/watchCreateUpdate.html'
    if request.method == 'GET':
        print(WatchForm())
        return render(request, template, {'watchForm':WatchForm()})
    
        # POST
    watchForm = WatchForm(request.POST)
    if not watchForm.is_valid():
        return render(request, template, {'watchForm':watchForm})
    watchForm.save()
    messages.success(request, '文章已新增')
    return redirect('watch:watch')

def watchRead(request, watchId):
    '''
    Read an watch
        2. Render the iphoneRead template with the watch instance and its
           associated comments
    '''
    watch = get_object_or_404(Watch, id=watchId)
    context = {
        'watch': watch,
        'comments': Comment.objects.filter(watch=watch)
    }
    return render(request, 'watch/watchRead.html', context)
@admin_required
def watchUpdate(request, watchId):
    '''
    Update the watch instance:
        1. Get the watch to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    watch = get_object_or_404(Watch, id= watchId)
    template = 'watch/watchCreateUpdate.html'
    if request.method == 'GET':
        watchForm = WatchForm(instance=watch)
        return render(request, template, {'watchForm':watchForm})

    # POST
    watchForm = WatchForm(request.POST, instance=watch)
    if not watchForm.is_valid():
        return render(request, template, {'watchForm':watchForm})

    watchForm.save()
    messages.success(request, '文章已修改') 
    return redirect('watch:watchRead', watchId=watchId)
@admin_required
def watchDelete(request, watchId):
    '''
    Delete the watch instance:
        1. Render the watch page if the method is GET
        2. Get the watch to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return redirect('watch:watch')

    # POST
    watch = get_object_or_404(Watch, id=watchId)
    watch.delete()
    messages.success(request, '文章已刪除')  
    return redirect('watch:watch')

def watchSearch(request):
    '''
    Search for watchs:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    watchs = Watch.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'watchs':watchs, 'searchTerm':searchTerm} 
    return render(request, 'watch/watchSearch.html', context)
