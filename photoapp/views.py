from django.shortcuts import render, redirect
from .models import CategoryModel, PhotoModel

def ViewGallary(request):
    category = request.GET.get('category')
    if category == None:
        images = PhotoModel.objects.all()
    else:
        images = PhotoModel.objects.filter(category__name = category)
    categories = CategoryModel.objects.all()
    # images = PhotoModel.objects.all()
    params = {'categories': categories, 'images':images}
    return render(request, 'photoapp/gallary.html', params)

def ViewImages(request,pk=None):
    image = PhotoModel.objects.get(id=pk)
    return render(request, 'photoapp/Images.html', {'image':image})

def addNewPhotos(request):
    categories = CategoryModel.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category']!= 'none':
            category = CategoryModel.objects.get(id=data['category'])
        elif data['new_category']!='':
            category, created = CategoryModel.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        image = PhotoModel.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('gallary')


    params = {'categories':categories}
     

    return render(request, 'photoapp/addnew.html', params)
