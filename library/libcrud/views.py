from django.shortcuts import render, HttpResponseRedirect
from .models import Book
from .forms import BookRegister

def add_show(request):
    if request.method == 'POST':
        book_form = BookRegister(request.POST)
        if book_form.is_valid():
            book_form.save()
            book_form = BookRegister()
    else:
        book_form = BookRegister()
    book_data = Book.objects.all()
    return render(request, 'libcrud/Addshow.html',{'form':book_form, 'book':book_data})


def update_data(request,id):
    if request.method == 'POST':
        bdata = Book.objects.get(pk=id)
        formdata = BookRegister(request.POST, instance=bdata)
        if formdata.is_valid():
            formdata.save()
    else:
        bdata = Book.objects.get(pk=id)
        formdata = BookRegister(instance=bdata)
        return render(request,'libcrud/updatebook.html',{'form':formdata})


def delete_data(request,id):
    if request.method == 'POST':
        db = Book.objects.get(pk=id)
        db.delete()
        return HttpResponseRedirect('/')

