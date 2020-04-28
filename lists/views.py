from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    #if request.method=='POST':
      #  return HttpResponse(request.POST['item_text'])
    #return render(request,'home.html')
    #item=Item()
    #item.text=request.POST.get('item_text','')
    #item.save()
    if request.method=='POST':
        #new_item_text=request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    #else:
      #  new_item_text=''
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})
    #return render(request,'home.html',{
    #'new_item_text': new_item_text,
    #})
    #return render(request,'home.html',{
    #    'new_item_text':request.POST.get('item_text',''),
     #   })

#    return HttpResponse('<html><title>To-Do lists</title></html>')
# Create your views here.
#home_page=None
#def home_page():
 #   pass
