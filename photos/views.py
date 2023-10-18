from django.shortcuts import render,redirect
from .models import Category, Photo

# Create your views here.
def gallary(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    category = Category.objects.all()
    context = {'category': category, 'photos':photos}
    return render(request,'photos/gallary.html',context)

def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photos': photos})

def addPhoto(request):
    category = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )

        return redirect('gallary')

    context = {'category': category}
    return render(request,'photos/add.html',context)